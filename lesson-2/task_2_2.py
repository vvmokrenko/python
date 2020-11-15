v_input = input('Введите элементы списка через запятую: ')
v_list_input = v_input.split(',')  # строку преобразуем в список, используя запятую как разделитель
v_list_output = v_list_input.copy()  # просто присваивание использовать нельзя

for i, val in enumerate(v_list_input):
    if (i % 2) != 0:
        v_list_output[i - 1] = v_list_input[i]
        v_list_output[i] = v_list_input[i - 1]

# результат
print(f'Исходный список {v_list_input} преобразован в новый {v_list_output}')
