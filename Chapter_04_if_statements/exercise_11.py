current_hour = eval(input('Enter hour: '))
am_pm = eval(input('am (1) or pm (2)? '))
hours_ahead = eval(input('How many hours ahead? '))

if (am_pm == 1 and current_hour == 12):
    current_hour = 0

if (am_pm == 2 and current_hour != 12):
    current_hour += 12

current_hour += hours_ahead
current_hour %= 24
if (current_hour > 12):
    current_hour -= 12
    am_pm = 2
else:
    am_pm = 1

print('New hour: ', current_hour, end='')
if (am_pm == 1):
    print(' am', end='')
else:
    print(' pm', end='')