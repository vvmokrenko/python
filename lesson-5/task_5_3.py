tot_sal = 0
i = 0
list_fio = []
try:
    with open('text_3.txt', 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            i += 1
            cur_sal = float(line.split()[1])
            tot_sal += cur_sal
            if cur_sal < 20000: list_fio.append(line.split()[0])
    print(f'Сотрудники, имеющие оклад менее 20000: {tuple(list_fio)}')
    print(f'Средний доход сотрудников: {round(tot_sal / i, 2)}')
except IOError:
    print('Произошла ошибка вводв-вывода!')
