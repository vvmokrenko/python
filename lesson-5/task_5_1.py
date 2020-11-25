with open('my_first_file.txt', 'w') as f_obj:
    while True:
        str = input('Введите строку, которая будет записана в файл: ');
        if str == '':  # признак окончания ввода - пустая строка
            break
        else:
            print(str, file=f_obj)
