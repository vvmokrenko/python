import json

dict = {}
v_total_profit = 0
v_cur_profit = 0
v_cnt = 0
v_result_list = []
with open('text_7.txt', 'r+', encoding='utf-8') as f_obj:
    for line in f_obj:
        v_list = line.split()
        v_cur_profit = round(float(v_list[2]) - float(v_list[3]))
        if v_cur_profit >= 0:
            v_cnt += 1
            v_total_profit += v_cur_profit
        dict.update([(v_list[0] + ' ' + v_list[1], v_cur_profit)])

if v_cnt > 0:
    v_avg_profit = round(v_total_profit / v_cnt)
else:
    v_avg_profit = None

v_result_list.append(dict)
v_result_list.append({"average_profit": v_avg_profit})  # добавляем один элемент

with open('text_7.json', 'w', encoding='utf-8') as f_obj:
    json.dump(obj=v_result_list, indent=4, fp=f_obj, ensure_ascii=False)  # записываем красиво и читабельно
