class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'оклад': wage, 'премия': bonus}  # Инициализируем словарь


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('оклад') + self._income.get('премия')


w = Position('Иван', 'Иванов', 20000, 5000)
print(f'{w.get_full_name()} имеет доход, равный {w.get_total_income()}')

w = Position('Петр', 'Петров', 30000, 8000)
print(f'{w.get_full_name()} имеет доход, равный {w.get_total_income()}')
