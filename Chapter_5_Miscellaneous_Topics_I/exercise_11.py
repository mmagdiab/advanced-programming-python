factorial = 1
n = eval(input('Enter the number n to calculate factorial: '))
for i in range(1,n+1):
   factorial *= i
print('Factorial is: ', factorial)