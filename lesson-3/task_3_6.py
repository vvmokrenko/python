int_func = lambda s: s.capitalize()


def lat_alphabet(*args):
    """
    Функция проверки, что все символы входного итератора - маленькие латинские буквы
    :param args: итератор
    :return: True - все символы - маленькие латинские буквы
    """
    v_res = True
    for val in args:
        v_ord = ord(val)
        if not (v_ord >= 97 and v_ord <= 122):
            v_res = False
            break
    return v_res


v_input = input('Введите через пробел несколько слов в нижнем регистре: ')
v_list_input = v_input.split()  # строку преобразуем в список, используя пробел как разделитель
v_output = []
for val in v_list_input:
    is_latin_word = lat_alphabet(*val)
    if is_latin_word: v_output.append(int_func(val))

print(f'Отфильтрованный и преобразованный список слов: {v_output}')
