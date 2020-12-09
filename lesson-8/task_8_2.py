class CustomDivisionByZero(Exception):
    def __init__(self, txt):
        self.__txt = txt

class ExecuteDiv:

    @staticmethod
    def customDiv(a, b):
        try:
            if b == 0: raise CustomDivisionByZero('Делить на ноль нельзя! Введите другое число в качестве делителя.');
            r = a / b
            print(f'Результат выполнения деления {a} на {b} равен {r}')
        except CustomDivisionByZero as x:
            print(x)


a = float ( input("Введите делимое: ") )
b = float ( input("Введите делитель: ") )
ExecuteDiv.customDiv(a, b)
