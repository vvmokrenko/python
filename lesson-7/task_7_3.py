"""класс клетка"""


class Cell:
    def __init__(self, cell):
        self.cell = cell  # количество ячеек в клетке

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell) if self.cell > other.cell else print('Разность д.б. больше нуля!')

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell) if self.cell > other.cell else print('Правый параметр меньше левого!')

    def make_order(self, row):  # row - кол-во ячекк в ряду
        result = ''
        for i in range(1, self.cell + 1):
            result += ('*\n' if (i % row == 0) else '*')
        return result


cell_1 = Cell(11)
print('Cell_1 distribution:\n' + cell_1.make_order(5))
cell_2 = Cell(15)
print('Cell_2 distribution:\n' + cell_2.make_order(7))
cell_3 = cell_1 + cell_2
print('Cell_1 + Cell_2 distribution:\n' + cell_3.make_order(6))
cell_4 = cell_2 - cell_1
print('Cell_2 - Cell_1 distribution:\n' + cell_4.make_order(6))
cell_5 = cell_2 // cell_1
print('Cell_2 // Cell_1 distribution:\n' + cell_5.make_order(6))
