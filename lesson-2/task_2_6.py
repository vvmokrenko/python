v_int = 0
v_list_total = []
while True:
    v_int = v_int + 1
    v_input = input(
        f'Введите информацию о товаре номер {v_int} в формате <название, цена, количество, ед>. Введите 0 для выхода: ')
    if v_input == '0': break
    # контроль достаточности входных данных
    if (v_input.count(',') != 3):
        v_int = v_int - 1
        continue
    v_list_input = v_input.split(',')
    # проверка на числа для атрибутов цена и количество
    if not (v_list_input[1].strip().isdigit() and v_list_input[2].strip().isdigit()):
        v_int = v_int - 1
        continue
    v_list_total.append(
        (v_int, {"название": v_list_input[0], "цена": v_list_input[1].strip(), "количество": v_list_input[2].strip(),
                 "ед": v_list_input[3]}))

# формируем новый словарь
v_name = []
v_price = []
v_amount = []
v_unit = []
v_output_dict = {}
for val in v_list_total:
    v_name.append(val[1].get('название'))
    v_price.append(val[1].get('цена'))
    v_amount.append(val[1].get('количество'))
    v_unit.append(val[1].get('ед'))
v_output_dict = dict(название=v_name, цена=v_price, количество=v_amount, ед=v_unit)
print(v_output_dict)
