def f_sum_max(a, b, c):
    """
    Функция возвращает сумму двух наибольших аргументов
    :param a,b,c: number
    :return: number
    """
    try:
        l = [a, b, c]
        l.sort(reverse=True)
        return l[0] + l[1]
    except:
        return


while True:
    v_input = input('Введите три числа, используя пробел в качестве разделителя: ')
    v_list_input = v_input.split()  # строку преобразуем в список, используя пробел как разделитель
    v_input_float = [float(x) for x in v_list_input]
    v_val = f_sum_max(*v_input_float)
    if (v_val is None):
        print('Ошибка. Повторите ввод')
    else:
        print(f'Сумма двух наибольших из {v_list_input} равна {v_val}')
        break
