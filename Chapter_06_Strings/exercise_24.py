value = input('Enter value to be derived: ')
result = ''
result += value[value.index('^')+1:]
result += value[:value.index('^')+1]
power = eval(value[value.index('^')+1:])
result += str(power-1)
print('result: ', result)
