def f_div(a, b):
    """
    Функция возвращает резльтат деления a на b.
    :param a: делимое
    :param b: делитель
    :return: результат деления, None - ошибка деления на ноль.
    """
    try:
        c = a / b
        print(f'{a}/{b} = {c}')
        return c
    except ZeroDivisionError:
        return


while True:
    v_input_str = input(f'Введите два числа через пробел: ').split()
    v_input_float = [float(x) for x in v_input_str]
    v_val = f_div(v_input_float[0], v_input_float[1])
    if (v_val is None):
        print('Ошибка. Повторите ввод')
    else:
        break
