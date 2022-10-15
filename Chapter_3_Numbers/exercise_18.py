change = eval(input('Enter change: '))

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

nickels = change // 5
change %= 5

pennies = change // 1

print('Quarter: ', quarters)
print('Dimes: ', dimes)
print('Nickels: ', nickels)
print('Pennies: ', pennies)