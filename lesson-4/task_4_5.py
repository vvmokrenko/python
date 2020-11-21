from functools import reduce

f_mlt = lambda p1, p2: p1 * p2
list = [i for i in range(100, 1001, 2)]
print(reduce(f_mlt, list))
