def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        yield a


for el in fact(7):
    print(el)
