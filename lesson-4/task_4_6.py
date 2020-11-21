from itertools import count
from itertools import cycle

# Выводим 5 элементов последовательности, начиная с числа 3
seq_1 = count(3)
for i in range(5): print(next(seq_1))

# Выводим элементы итератора типа цикл до тех пор, пока не встретиться символ "n"
el = ''
seq_2 = cycle("phyton")
while el != 'n':
    el = next(seq_2)
    print(el)
