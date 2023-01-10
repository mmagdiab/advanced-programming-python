"""
The file high_temperatures.txt contains the average high temperatures for each day of
the year in a certain city. Each line of the file consists of the date, written in the month/day
format, followed by a space and the average high temperature for that date. Find the 30-day
period over which there is the biggest increase in the average high temperature.
"""
# Read line and replace / with whitespace
# So after splitting, we will have a list of lists (each list [month, day, temp]
lines = [line.strip().replace('/', ' ') for line in open('high_temperatures.txt')]
line_data = [line.split(' ') for line in lines]

# Sort data based on month then on days
line_data.sort(key=lambda x: (x[0], x[1]))

# get a list of only temps
temps = [data[2] for data in line_data]

highest_temp_period = [0] * 30

for i in range(len(temps)-30):
    if sum(temps[i:i+30]) > sum(highest_temp_period):
        highest_temp_period = temps[i:i+30]

print(highest_temp_period)
