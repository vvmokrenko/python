list_in = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_out = [el for i, el in enumerate(list_in) if i > 0 and el > list_in[i - 1]]
print(list_out)
