class ComplexNumber:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __add__(self, other):
        a = self.__a + other.__a
        b = self.__b + other.__b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        a = (self.__a * other.__a) - (self.__b * other.__b)
        b = (self.__b * other.__a) + (self.__a * other.__b)
        return ComplexNumber(a, b)

    def __str__(self):
        # форматирвоание красивого вывода
        o = ' + '
        b = self.__b
        if b < 0:
            o = ' - '
            b = abs(b)

        if b != 1:
            return f'({self.__a}{o}{b}j)'
        else:
            return f'({self.__a}{o}j)'


c1 = ComplexNumber(5, 3)
c2 = ComplexNumber(2, 4)
print(f'Результат сложения чисел {c1} и {c2} равен {c1 + c2}')
print(f'Результат умножнния чисел {c1} и {c2} равен {c1 * c2}')
c1 = ComplexNumber(5, -3)
c2 = ComplexNumber(-2, 4)
print(f'Результат сложения чисел {c1} и {c2} равен {c1 + c2}')
print(f'Результат умножнния чисел {c1} и {c2} равен {c1 * c2}')
