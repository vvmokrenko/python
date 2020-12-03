from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_cons(self):
        pass


class Coat(Clothes):
    def __init__(self, name, V):
        self.__name = name
        self.__V = V

    @property
    def fabric_cons(self):
        return f'Расход ткани пальто "{self.__name}" равен {round(self.__V / 6.5 + 0.5, 1)}'


class Suit(Clothes):
    def __init__(self, name, H):
        self.__name = name
        self.__H = H

    @property
    def fabric_cons(self):
        return f'Расход ткани костюма "{self.__name}" равен  {str(round(2 * self.__H + 0.3, 1))}'


c1 = Coat("Dolce", 50)

c2 = Coat("Versace", 46)

c3 = Suit("Большевичка", 52)

c4 = Suit("Онегин", 48)

print(c1.fabric_cons)
print(c2.fabric_cons)
print(c3.fabric_cons)
print(c4.fabric_cons)
