def f_sum(*args):
    global v_total  # nonlocal нельзя объявить, так как нет объемлющей функции
    v_iter = 0
    v_exit = False  # обязательно инициализируем
    for i, val in enumerate(args):
        if val.lower() == 'q':
            v_exit = True
            break
        else:
            v_iter += float(val)
    v_total += v_iter
    return (v_iter, v_exit)  # возвращаем кортеж, т.к. нам нужны два результата


i = 0  # номер итерации ввода от пользователя
v_total = 0  # инициализация глобальной переменной, используемой в функции
while True:
    i += 1
    v_input = input(f'{i}. Введите через пробел несколько чисел и нажите пробел (q - выход): ')
    v_list_input = v_input.split()  # строку преобразуем в список, используя пробел как разделитель
    v_out = f_sum(*v_list_input)
    print(f'{i}. Сумма чисел {v_total}({v_out[0]})')
    if v_out[1] == True: break  # если передали q то выход
