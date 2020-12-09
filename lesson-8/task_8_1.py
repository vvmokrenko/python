import datetime


class IncorrectLenStr(Exception):
    def __init__(self, txt):
        self.__txt = txt


class Data:
    def __init__(self, dstr):  # dstr это дата в формате dd-mm-yyyy
        print(f"Пользователь ввел: {dstr}")
        self.parse_dstr(dstr)

    @classmethod
    def parse_dstr(cls, dstr):
        try:
            if len(dstr) != 10:
                raise IncorrectLenStr('Длина введенной строки не равна 10, что не соответствует формату DD-MM-YYYY')
            cls.__dd = int(dstr[0:2])
            cls.__mm = int(dstr[3:5])
            cls.__yyyy = int(dstr[6:10])
            print(f"Разбили на следующие части: DD={cls.__dd}, MM={cls.__mm}, YYYY={cls.__yyyy}")
            cls.validate_date(cls.__dd, cls.__mm, cls.__yyyy)
        except ValueError:
            print('Ошибка преобразования! Вводимая строка не соответствует формату DD-MM-YYYY.')
        except IncorrectLenStr as x:
            print(x)

    @staticmethod
    def validate_date(dd, mm, yyyy):
        try:
            d = datetime.date(yyyy, mm, dd)
            print('Введенное значение является истинной датой')
        except ValueError:
            print('Ошибка преобразования! Вводиая строка не соответствует истинной дате.')


dstr = input('Введите строку в формате DD.MM.YYYY: ')

my_d = Data(dstr)
