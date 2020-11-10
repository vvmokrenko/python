v_int = int(input("Please type a positive number: "))
# find largest figure
v_largest_figure = v_int % 10
v_new_int = v_int // 10
while v_new_int > 0:
    v_figure = v_new_int % 10
    v_new_int = v_new_int // 10
    if v_figure > v_largest_figure:
        v_largest_figure = v_figure
# show result
print(f'largest figure from {v_int} is {v_largest_figure}')
