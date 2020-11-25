my_output = lambda p1, p2: print(f'Кол-во слов в строке № {p1} равно {p2}')
with open('my_second_file.txt', 'r', encoding='utf-8') as f_obj:
    list = f_obj.readlines()
    print(f'Содержимое файла: {list})
    print(f'Количество строк в файле, включая пустые: {len(list)}')
    for i, val in enumerate(list, 1):
        my_output(i, len(val.split()))
