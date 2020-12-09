from abc import ABC, abstractmethod  # класс Офисное обрудование будет абстрактным


class InvalidOperation(Exception):
    def __int__(self, txt):
        self.__txt = txt


class InvalidEquipment(Exception):
    def __int__(self, txt):
        self.__txt = txt


class InvalidDept(Exception):
    def __int__(self, txt):
        self.__txt = txt


class NotEnough(Exception):
    def __int__(self, txt):
        self.__txt = txt


# СКЛАД
class Warehouse:

    def __init__(self):
        # инициализация подразделений. Каждое подразделение будет принимать оборудование в определенном количестве. В начале все пусто
        self.__depts = {1: {}, 2: {}, 3: {}}
        # список допустимых операций на складе - добавить на склда, распределить со склада
        self.__operations = {1: 'put', 2: 'push'}
        # Список оборудования на складе
        # self.__listEquip = {1: 0, 2: 0, 3: 0}
        self.__listEquip = {}

    # получение имени подразделения по его индексу
    @classmethod
    def getDeptName(cls, index):
        return "Подразделение " + str(index)

    # поступление на склад
    def put(self, e):
        ind = e.getIndex()
        current_value = self.__listEquip.setdefault(ind, 0)
        self.__listEquip[ind] = current_value + e.getAmount
        print(f'Положили на склад оборудование {ind} количеством {e.getAmount}')
        print(f'{self}')

    #  распределение со склада в подразделение
    def push(self, e, where):
        ind = e.getIndex()
        current_value = self.__listEquip.get(ind, 0)  # По умолчанию 0
        self.__listEquip[ind] = current_value - e.getAmount  # осталось на складе
        current_value_dept = self.__depts[where].setdefault(ind, 0)  # по умолчанию 0 в подразделении
        self.__depts[where][ind] = current_value_dept + e.getAmount  # ушло в подразделение
        print(f'Распределили со склада оборудование {ind} количеством {e.getAmount}')
        print(f'{self}')

    # проверка достаточности на складе объема оборудования для его распределения
    def checkEnoughEqiup(self, e):
        ind = e.getIndex()
        current_value = self.__listEquip.get(ind, 0)  # По умолчанию 0
        v = current_value - e.getAmount
        if v < 0:
            raise NotEnough('На складе столько нет оборудования!')
        return v

    # проверка допустимости действий на складе
    @classmethod
    def ValidateOperation(cls, oper):
        if oper not in str(cls().__operations.keys()):
            raise InvalidOperation('На складе не понимают, что Вы хотите!')
        return int(oper)
        # Проверка допустиости действий на складе

    # проверка, что индекс подразделения в корректном диапазоне
    @classmethod
    def ValidateDept(cls, no):
        if no not in str(cls().__depts.keys()):
            raise InvalidDept('Некорректный номер подразделения!')
        return int(no)

    # основной метод выбора операции с офисным обородуванием
    def MakeOperation(self):
        try:
            v = input(
                'Введите операцию с оборудованием: (1 - Добавить на склад, 2 - Распределить по подразделениям, 0 - выход): ')
            if v == '0':  # если поступил 0, то выход
                return 0
            else:
                v = self.ValidateOperation(v)
                if v == 1:
                    # какое оборудование добавляем
                    try:
                        v = input('Какое обрудование Вы хотите добавить (1 - Принтеры, 2 - Сканеры, 3 - Ксероксы): ')
                        e = OfficeEquipment.ValidateEquipment(v)
                        self.put(e)
                    except InvalidEquipment as err:
                        print(err)
                elif v == 2:
                    # какое оборудование распредедляем
                    try:
                        v = input(
                            'Какое обрудование Вы хотите распределить (1 - Принтеры, 2 - Сканеры, 3 - Ксероксы): ')
                        e = OfficeEquipment.ValidateEquipment(v)
                        c = self.checkEnoughEqiup(e)
                        d = input('В какое подразделение Вы хотите распределить (1 - Подр1, 2 - Подр2, 3 - Подр3): ')
                        d = Warehouse.ValidateDept(d)
                        self.push(e, d)
                    except (InvalidEquipment, InvalidDept, NotEnough) as err:
                        print(err)
                return v
        except InvalidOperation as err:
            print(err)

    #  Перегрузка для красивого вывода состояние склада и данных по подразделениям
    def __str__(self):
        # Данные по оборудованию
        o = {}
        for key, value in self.__listEquip.items():
            # print('str', key, value)
            name = OfficeEquipment.getEquipName(key)
            o.setdefault(name, value)
        # Данные по подразделениям
        s = {}
        for key, value in self.__depts.items():
            name = Warehouse.getDeptName(key)
            s1 = {}
            for key1, value1 in value.items():  # Пример value как словаря
                name1 = OfficeEquipment.getEquipName(key1)
                s1.setdefault(name1, value1)
            s.setdefault(name, str(s1))
        return 'Состояние склада: \033[33m\033[1m' + str(o) + '\n\033[0mСостояние подразделений: \033[32m\033[1m' + str(s) + '\033[0m\n' + '-' * 120

    # Движок
    def start(self):
        v = 0
        while True:
            v = self.MakeOperation()
            if v == 0:
                print('Пользователь запросил выход из программы')
                break


# ОФИСНОЕ ОБОРУДОВАНИЕ
class OfficeEquipment(ABC):
    equip = {}  # Справочник оборудования.

    def __init__(self):
        OfficeEquipment.equip.setdefault(self._index,
                                         # Можно использовать полное имя self._name
                                         self.getShortName() # или сокращенное
                                         )
        while True:
            try:
                self._amount = int(input('Введите количество оборудования: '))
                if self._amount < 0:
                    raise ValueError
            except ValueError:
                print('Недопустимое значение для количества!')
            else:
                break

    # Получение имени обуродования по его индексу
    @classmethod
    def getEquipName(cls, index):
        # print('ads', cls.equip, index, type(index))
        return cls.equip[index]

    # Получение количества обуродования
    @property
    def getAmount(self):
        return self._amount

    # Возвращает индекс оборудования
    def getIndex(self):
        return self._index

    # Возвращает имя оборудования
    def getName(self):
        return self._name

    # Проверка коректности выбора оборудования
    @classmethod
    def ValidateEquipment(cls, choice):
        try:
            i = int(choice)
            if i == 1:
                e = Printer()
            elif i == 2:
                e = Scaner()
            elif i == 3:
                e = Xerox()
            else:
                raise InvalidEquipment('Некорректный тип оборудования!')
        except (ValueError, InvalidEquipment):
            raise InvalidEquipment('Некорректный тип оборудования!')
        else:
            return e

    @abstractmethod
    def getShortName(self):
        pass

# ПРИНТЕР
class Printer(OfficeEquipment):
    def __init__(self):
        self._index = 1
        self._name = 'Принтер'
        super().__init__()

    @staticmethod
    def getShortName():
        return 'Прн.'


# СКАНЕР
class Scaner(OfficeEquipment):
    def __init__(self):
        self._index = 2
        self._name = 'Сканер'
        super().__init__()

    @staticmethod
    def getShortName():
        return 'Скн.'


# КСЕРОКС
class Xerox(OfficeEquipment):
    def __init__(self):
        self._index = 3
        self._name = 'Ксерокс'
        super().__init__()

    @staticmethod
    def getShortName():
        return 'Кср.'

# запускаем процесс работы склада
w = Warehouse()
w.start()
