meal_price = eval(input('Enter meal price: '))
tip_percentage = eval(input('Enter tip percentage: '))

tip_amount = meal_price * (tip_percentage/100)
total_bill = meal_price + tip_amount
print('Tip amount: ', tip_amount)
print('Total bill: ', total_bill)