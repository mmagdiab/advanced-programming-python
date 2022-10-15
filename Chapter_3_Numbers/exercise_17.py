year = eval(input('Enter a year: '))
count = 0

for i in range(1601, year):
    if ((i // 4) * 4 == i) and ((i // 400) * 400 < i):
        count += 1
print(count)