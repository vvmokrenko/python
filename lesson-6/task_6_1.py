import time


class TrafficLight:
    __color = ''
    colorkey = {'red': '\033[31m', 'yellow': '\033[33m', 'green': '\033[32m'}

    def _switchon(self, color, delay):
        self.s = 0  # кол-во секунд задержки
        TrafficLight.__color = color
        while self.s < delay:
            self.s += 1
            print(f"{TrafficLight.colorkey.get(color)}Light is {TrafficLight.__color}")
            time.sleep(1)

    def running(self):
        self._switchon("red", 7)
        self._switchon("yellow", 2)
        self._switchon("green", 4)


t = TrafficLight()
t.running()
