class Road():
    weight = 25  # вес 1 кв.м толщиной 1 см.
    height = 5  # высота полотна в см.

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self):
        return round(self._length * self._width * Road.weight * Road.height / 1000)


r = Road(5000, 6)

print(f'Суммарный все полотна длиной {r._length} метров и шириной {r._width} метров равно {r.get_weight()} тонн(ы)')
