class Stationery:
    title = ''

    def draw(self):
        print(f'Запуск отрисовки c помощью {self.title}')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        super().draw()
        print(f'Мы рисуем с помощью {self.title}')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        super().draw()
        print(f'Мы рисуем с помощью {self.title}')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        super().draw()
        print(f'Мы рисуем с помощью {self.title}')


p = Pen()
p.draw()

pnc = Pencil()
pnc.draw()

h = Handle()
h.draw()
