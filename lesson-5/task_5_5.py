from functools import reduce
from random import randrange


def my_concat_line(p1):
    # Генерируем числа через пробел количеством p1
    v = ''
    for val in range(p1): v += str(randrange(100)) + ' '
    return v.rstrip()


def my_sum(prev_el, el):
    return int(prev_el) + int(el)


with open('output_5.txt', 'r+', encoding='utf-8') as f_obj:
    f_obj.truncate(0)
    f_obj.write(my_concat_line(5))  # Генерируем числа через пробел количеством 5
    f_obj.seek(0, 0)  # Возвращаемся на начало строки
    v_list = f_obj.readline().split()
    print(f'Сумма чисел {v_list} равна {reduce(my_sum, v_list)}')
