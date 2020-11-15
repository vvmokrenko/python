v_input = input('Введите несколько слов разделённых пробелами: ')
v_list_input = v_input.split()  # строку преобразуем в список, используя пробел как разделитель

for i, val in enumerate(v_list_input, 1):
    print(f'Элемент № {i} содержит значение {val[:10]}')
