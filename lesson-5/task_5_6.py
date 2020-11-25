from functools import reduce


def f_replace(prev_el, el):
    #  замещает пробелами все, кроме цифр
    if el.isdigit():
        return prev_el + el
    else:
        return prev_el + ' '


def f_sum(prev_el, el):
    return int(prev_el) + int(el)


dict = {}
with open('text_6.txt', 'r+', encoding='utf-8') as f_obj:
    for line in f_obj:
        v_list = line.split(':')
        list_numbers = reduce(f_replace, v_list[1]).split()
        sum_numbers = reduce(f_sum, list_numbers)
        dict.update([(v_list[0], int(
            sum_numbers))])  # !!!ПОЧЕМУ-ТО НАДО ПРИВОДИТЬ В INT, ХОТЯ F_SUM УЖЕ ДОЛЖНА БЫЛА ПРИВЕСТИ К INT!!!

print(dict)
