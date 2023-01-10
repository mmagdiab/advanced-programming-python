"""
Given two dates entered as strings in the form mm/dd/yyyy where the years are between
1901 and 2099, determine how many days apart they are. Here is a bit of information that
may be useful: Leap years between 1901 and 2099 occur exactly every four years, starting at
1904. February has 28 days, 29 during a leap year. November, April, June, and September
each have 30 days. The other months have 31 days.
"""

# I will change format to dd/mm/yyyy

_30_day_month = [4, 6, 9, 11]
leap_years = [str(year) for year in range(1904, 2099, 4)]

first_date = input('Enter 1st date in format dd/mm/yyyy: ').split('/')
second_date = input('Enter 2nd date in format dd/mm/yyyy: ').split('/')

sorted_dates = [first_date, second_date]
sorted_dates.sort(key=lambda x: (x[2], x[1], x[0]), reverse=True)
# now newer date is in index 0

# Transfer day, month, year to int
newer_date = [int(i) for i in sorted_dates[0]]
old_date = [int(i) for i in sorted_dates[1]]

total_days = 0

# add days remaining in old_date (year)

for month in range(old_date[1], 13):  # old_date[1] -> earlier date month
    if month == 2:
        if old_date[2] in leap_years:  # if the rear is leap year
            total_days += 29 - old_date[0]  # then 29 day (total february days in leap year)
        else:
            total_days += 28
    elif month in _30_day_month:
        total_days += 30
    else:
        total_days += 31


# sum years in between

for year in range(old_date[2]+1, newer_date[2]):
    if year in leap_years:
        total_days += 366
    else:
        total_days += 365

# add days passed in newer_date (year)

for month in range(0, newer_date[1] + 1):  # newer_date[1] -> newer date month
    if month != newer_date[1]:
        if month == 2:
            if newer_date[2] in leap_years:  # if the rear is leap year
                total_days += 29  # then 29 day (total february days in leap year)
            else:
                total_days += 28
        elif month in _30_day_month:
            total_days += 30
        else:
            total_days += 31
    else: # if the current month is equal to new date month
        total_days += newer_date[0]

print(total_days)
