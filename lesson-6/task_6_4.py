class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):

        if direction == 'left':
            print(f'Машина {self.name} повернула налево')
        else:
            print(f'Машина {self.name} повернула направо')

    def showspeed(self):
        print(f'Скорость машины {self.name} равна {self.speed}')


class TownCar(Car):
    def showspeed(self):
        s = ''
        if self.speed > 60: s = ' Вы превысили скорость!'
        print(f'Скорость равна {self.speed}.{s}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def showspeed(self):
        if self.speed > 40: s = ' Вы превысили скорость!'
        print(f'Скорость равна {self.speed}.{s}')


class PoliceCar(Car):
    pass


t = TownCar(40, 'yellow', 'Skoda', False)
t.go()
t.showspeed()
t.turn('left')
t.stop()

s = TownCar(120, 'red', 'Audi', False)
s.go()
s.showspeed()
s.turn('')
s.stop()

w = TownCar(30, 'black', 'Cat', False)
w.go()
w.showspeed()
w.turn('right')
w.stop()

p = TownCar(90, 'white', 'BMW', True)
p.go()
p.showspeed()
p.turn('')
p.stop()
