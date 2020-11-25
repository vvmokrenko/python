dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def f_replace(p1):
    v_key = p1[0:p1.find(' ')]  # Отрезаем начало строки до пробела (это будет ключом словаря)
    v_value = dict.get(v_key)  # Вытаскиваем из словаря соответствие по ключу
    if v_value != None: return p1.replace(v_key, v_value)  # Если нашли по ключу, то меняем входную строку
    return p1  # если замена не нашлась, то не меняем строку


f_dest = open('output_4.txt', 'w', encoding='utf-8')
with open('text_4.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj: f_dest.write(f_replace(line))

#  закрываем файлик
if not f_dest.closed: f_dest.close()
