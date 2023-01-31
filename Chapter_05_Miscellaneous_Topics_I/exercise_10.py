highest_1 = 0
highest_2 = 0
lowest_1 = 10000000000
lowest_2 = 10000000000
warning_flag = 0
total = 0

for i in range(10):
    score = eval(input('Enter score: '))
    total += score
    if (score > 100):
         warning_flag = 1
    if (score > highest_1):
        highest_1 = score
        highest_2 = highest_1
    elif (score > highest_2):
        highest_2 = score

    if (score < lowest_1):
        lowest_1 = score
        lowest_2 = lowest_1
    elif (score < lowest_2):
        lowest_2 = score

print('The highest score is: ', highest_1)
print('The lowest score is: ', lowest_1)

print('The average is: ', total/10)

print('The second largest score: ', highest_2)
if (warning_flag == 1):
    print('The user entered a value > 100 1')

print('The average without the 2 lowest scores is: ', (total - lowest_1 - lowest_2)/8)