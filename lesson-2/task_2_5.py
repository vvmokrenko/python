v_rating = [7, 5, 3, 3, 2]
while True:
    v_int = int(input('Введите натуральное число как новый элемент рейтинга или 0 для выхода: '))
    if v_int == 0: break
    #  Отдельная логика для первого и последнего элемента списка
    if v_rating[0] < v_int:
        v_rating.insert(0, v_int)
        v_i = 0;
    elif v_rating[len(v_rating) - 1] >= v_int:
        v_rating.append(v_int)
        v_i = len(v_rating) - 1
    else:
        for i in range(len(v_rating)):
            if v_rating[i] >= v_int and v_rating[i + 1] < v_int:
                v_rating.insert(i + 1, v_int)
                v_i = i + 1
                break  # прерывание цикла for
    print(f'Добавили элемент в индекс {v_i}. Новый рейтинг: {v_rating}')
