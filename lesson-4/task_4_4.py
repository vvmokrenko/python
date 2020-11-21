list_in = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_out = [val for val in list_in if (list_in.count(val) == 1)]
print(list_out)
