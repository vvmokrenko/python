v_list = ['строка1', 100, 60.05, False, tuple('this is tuple'), set({1, 1, 2, 3}),
          {'строка3', 12}, None, {'key1': 1, 2: 3.45, 6: None},
          b'text', bytearray(b'text'), [12, 56]
          ]
# выводим информация из списка
for i, val in enumerate(v_list, 1):  # пусть первый элемент списка имеет индекс, равный 1
    print(f'Элемент № {i}, значение которого равно {val}, имеет тип {type(val)}')
