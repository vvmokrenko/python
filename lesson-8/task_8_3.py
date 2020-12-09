class CustomValueError(Exception):
    def __init__(self, txt):
        self.__txt = txt


class CollectNumbers:
    __result = []

    @classmethod
    def play(cls):
        while True:
            try:
                s = input('Введите число или слово "stop" для выхода: ')
                # Допускаем отрицательные числа и дроби
                # Для этого можно исппользовать replace заменяя символы "." и "-"
                if s.upper() == 'STOP': break
                if not ((s.replace('-','')).replace('.','')).isdigit():
                    raise CustomValueError('Некорректное число!')
                cls.__result.append(s)
            except CustomValueError as x:
                print(x)

        print(f'Итоговый список чисел: {cls.__result}')

CollectNumbers.play()