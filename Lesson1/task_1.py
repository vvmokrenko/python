v_int = 10
v_str = 'Test string'
v_bool = 1 and 0
# print to the screen
print('v_int=' + str(v_int))
print('v_str=' + v_str)
print('v_bool=' + str(bool(v_bool)))

# ask user to type some numbers ans strings
v_int = int(input('Please, type a number from 0 up to 100: '))
v_str = input('Please, type a string: ')
v_int2 = int(input('Please, type a negative number: '))
v_str2 = input('Please, type one more string: ')
# show values
print(f'You have entered the following: {v_int}, {v_str}, {v_int2}, {v_str2}')
