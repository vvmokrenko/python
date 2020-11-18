def isint(s):
    """
    Функция проверяет, что аргумент целое число
    :param s: any
    :return: boolean
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def f_power_way1(a, b):
    """
    Возведение в стпень через оператор **
    :param a:
    :param b:
    :return:
    """
    try:
        return a ** b
    except:
        return


def f_power_way2(a, b):
    """
    Возведение в степень через цикл
    :param a:
    :param b:
    :return:
    """
    val = 1
    try:
        for i in range(0, abs(int(b))): val *= 1 / a
        return val
    except:
        return


while True:
    v_input = input('Введите через пробел действительное положительное число и целое отрицательное число: ')
    v_list_input = v_input.split()  # строку преобразуем в список, используя пробел как разделитель

    if not (v_list_input[0].isdigit() and float(v_list_input[0]) > 0):  # проверка на положительное число
        print('Ошибка. Первый параметр не является положительным числом. Повторите ввод')
    elif not (isint(v_list_input[1]) and int(v_list_input[1]) < 0):  # проверка на целое отрицательное число
        print('Ошибка. Второй параметр не является целым отрицательным числом. Повторите ввод')
    else:
        v_input_float = [float(x) for x in v_list_input]
        v_val1 = f_power_way1(*v_input_float)
        v_val2 = f_power_way2(*v_input_float)
        if ((v_val1 is None) or (v_val2 is None)):
            print('Ошибка. Повторите ввод')
        else:
            print(f'Способ 1. Возвдение числа {v_input_float[0]} в степень {v_input_float[1]} равно {v_val1}')
            print(f'Способ 1. Возвдение числа {v_input_float[0]} в степень {v_input_float[1]} равно {v_val2}')
            break
