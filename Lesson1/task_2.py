v_input_sec = int(input("Please type a number in seconds: "))
# convert the number into hh:mm:ss format
v_hour = int(v_input_sec / 3600)
v_min = int((v_input_sec - v_hour * 3600) / 60)
v_sec = v_input_sec - v_hour * 3600 - v_min * 60
# show result
print(
    f'You have entered the value: {v_input_sec} seconds. It will be {v_hour:02}:{v_min:02}:{v_sec:02} in "hh:mm:ss" format')
