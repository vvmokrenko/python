while True:
    v_month = int(input('Введите номер месяца от 1 до 12: '))
    if v_month >= 1 and v_month <= 12:
        break
v_list = ['зиме', 'зиме', 'весне', 'весне', 'весне', 'лету', 'лету', 'лету', 'осени', 'осени', 'осени', 'зиме']
v_dict = {1: 'зиме', 2: 'зиме', 3: 'весне', 4: 'весне', 5: 'весне', 6: 'лету',
          7: 'лету', 8: 'лету', 9: 'осени', 10: 'осени', 11: 'осени', 12: 'зиме'}

#  Решение для листа
print(f'Месяц с номером {v_month} относится к {v_list[v_month - 1]}')
#  Решение для словаря
print(f'Месяц с номером {v_month} относится к {v_dict.get(v_month)}')
