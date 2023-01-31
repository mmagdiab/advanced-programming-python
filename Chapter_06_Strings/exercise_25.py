expression = input('Enter an algebraic expression: ')
new_expression = ''
for i in range(len(expression)):
    if (expression[i] == '(' or expression[i].isalpha()) and i-1 >= 0 and expression[i-1].isdigit():
        new_expression += '*'
    new_expression += expression[i]
print('The new expression: ', new_expression)
