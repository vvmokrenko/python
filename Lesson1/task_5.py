v_revenue = int(input("Введите значение выручки фирмы: "))
v_costs = int(input("Введите значение издержек фирмы: "))

if v_revenue > v_costs:
    print('Ваша фирма работает с прибылью')
    v_profit = (v_revenue - v_costs) * 100 / v_revenue
    print(f'Рентабельность вашей фирмы {v_profit:.2f}%')
    v_worker = int(input("Введите количество сотрудиков фирмы: "))
    print(f'Прибыль вашей фирмы в расчете на одного сотрудника {(v_revenue - v_costs) / v_worker:.2f}')
elif v_revenue < v_costs:
    print('Ваша фирма работает с убытком')
else:
    print('Ваша фирма работает с нулевой прибылью')
