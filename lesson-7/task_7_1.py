class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix

    def __str__(self):
        a = ''
        for el in self.__matrix:
            for el2 in el: a += str(el2).rjust(8) + ' '
            a += '\n'
        return a

    def __add__(self, other):
        result = []
        for sublist in zip(self.__matrix, other.__matrix):  # бежим по списку кортежей с элеменртами матрицы
            temp = []
            for numbers in zip(sublist[0], sublist[1]):  # каждый наш кортеж содержит только два элемента
                temp.append(sum(numbers))
            result.append(temp)
        return Matrix(result)


matrix_1 = Matrix([[100, 2, 30], [4, 50, 6], [80, 800, 90]]);
print(f'Матрица 1: \n{matrix_1}')
matrix_2 = Matrix([[555, 25, 5], [4, 460, 66], [77, 3, 500]]);
print(f'Матрица 2: \n{matrix_2}')
print(f'Сложение двух матриц: \n{matrix_1 + matrix_2}')
