input_string="Name1: Han Age: 23 Guns: 2"



print(list(map(str,input_string.split())))

print('\n',list(map(str,input_string.split(':'))))

print('\n',list(map(str,input_string.strip())))

print('\n',list(map(str,input_string.strip().split())))