# Пример запуска скрипта из терминала:
# python.exe task_4_1.py 200 400 15000.25
from sys import argv

v_script, v_hours, v_rate, v_bonus = argv
print(f'Заработная плата сотрудника = {round((float(v_hours) * float(v_rate)) + float(v_bonus), 2)}')
