"""
Write a Python program that uses a class called DATE,
a class called TodayDate, and a class called Person BirthDate.
The class DATE would be the parent class for the other two classes and
should include two fields namely day, month, and year. The user will be allowed to enter the date of today and
his birth_date, and the program would use a function called Calculate Age to calculate and print the age of the user
in a suitable format.
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class TodayDate(Date):
    def __int__(self, year, month, day):
        super().__init__(year, month, day)


class BirthDate(Date):
    def __int__(self, year, month, day):
        super().__init__(year, month, day)


def calculate_age(today_date, birth_date):
    years_alive = today_date.year - birth_date.year
    months_alive = today_date.month - birth_date.month
    days_alive = today_date.month - birth_date.month

    if days_alive < 0:
        if months_alive > 0:  # Break 1 month into days
            months_alive -= 1
            days_alive += 30
        elif years_alive > 0:  # if no months, break a year into 11 month and 30 days
            months_alive += 11
            days_alive += 30
        else:  # if no years available the date in future
            print('The entered date is invalid')
            return

    if months_alive < 0:
        if years_alive > 0:  # break a year into 12 month
            months_alive += 12
            years_alive -= 1
        else:  # if no years available the date in future
            print('The entered date is invalid')
            return

    print('You are alive for {} years, {} months and {} days'.format(years_alive, months_alive, days_alive))


today = input('Enter today\'s date in the format dd-mm-yyyy: ')
birth = input('Enter birth date in the format dd-mm-yyyy: ')

today = TodayDate(int(today[6:]), int(today[3:5]), int(today[:2]))  # Or better use split.
birth = BirthDate(int(birth[6:]), int(birth[3:5]), int(birth[:2]))

calculate_age(today, birth)
