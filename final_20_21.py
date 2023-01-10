"""
Question 1: Students' data is stored in a text file named "students.txt". Separated by commas,
each student record contains the student ID, student name, then student numeric grade.
Write a Python program to do the following:
a) Read the data from a text file named "students.txt".
b) Split students' records into lines and store them as a list of strings.
c) Build a list of lists to simulate a two-dimensional array. In each row of the array,
index zero will contain student ID, index one will contain student name, index two will contain student numeric grade,
index three will contain student rate (Excellent, Very Good, Good, Pass, or Fail).
(N.B. Your program is supposed to calculate the student rate of appreciation due to university rules.)
d) Create a Python dictionary to calculate the frequency of each rate of appreciation of the students,
then print this dictionary in a tabular form.
"""
# a
data = open('students.txt')
# b
lines = [line.strip() for line in data]
# c
student_records = [line.split(',') for line in lines]
for record in student_records:
    if int(record[2]) >= 85:
        record.append('Excellent')
    elif int(record[2]) >= 75:
        record.append('Very Good')
    elif int(record[2]) >= 65:
        record.append('Good')
    elif int(record[2]) >= 50:
        record.append('Pass')
    else:
        record.append('Fail')
# d (another approach to use student student_records.count(grade))
d = {'Excellent': len([record for record in student_records if record[3] == 'Excellent']),
     'Very Good': len([record for record in student_records if record[3] == 'Very Good']),
     'Good': len([record for record in student_records if record[3] == 'Good']),
     'Pass': len([record for record in student_records if record[3] == 'Pass']),
     'Fail': len([record for record in student_records if record[3] == 'Fail'])}

print('{:>10s} | {:>10s}'.format('Grade', 'Frequency'))
for grade in d:
    print('{:>10s} | {:>10d}'.format(grade, d[grade]))

"""
Question 2: One way to encrypt a message is to rearrange the characters.
TO encrypt a string message, your algorithm will pick out the characters at even indices,
put them first in the encrypted string, and follow them by the characters at odd indices.
Write a program that asks the user to enter a string and use this method to encrypt the string.
Your program must contain two different functions for encryption and decryption.
"""


def encrypt(message):
    return message[::2] + message[1::2]


def decrypt(encrypted_message):
    if len(encrypted_message) < 3: # Must be at least 3 char
        return encrypted_message
    message_half = len(encrypted_message)//2
    decrypted_message = ''
    for i in range(message_half):
        decrypted_message += encrypted_message[i] + encrypted_message[message_half+1+i]
    # if the message is odd, at the char exactly in the middle
    decrypted_message += encrypted_message[message_half]
    return decrypted_message


some_message = input('Enter your message:')
result = encrypt(some_message)
print(result)
de_result = decrypt(result)
print(de_result)

"""
Question 3: Write a Python program that uses a class called DATE,
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


today = input('Enter today\'s date in the format dd-mm-yyyy: ').split('-')
birth = input('Enter birth date in the format dd-mm-yyyy: ').split('-')

today = TodayDate(int(today[2]), int(today[1]), int(today[0]))  # Or better use split.
birth = BirthDate(int(birth[2]), int(birth[1]), int(birth[0]))

calculate_age(today, birth)

"""
Question 4: Write a program in Python that displays a window to the user that asks them to enter an integer N and
displays its factorial N !
"""
from tkinter import *

def callback():
    user_input = eval(entry.get())
    if user_input < 0:
        label_result.configure(text='Cannot get factorial of a negative number.')
        return
    factorial = 1
    for i in range(2, user_input+1):
        factorial *= i
    label_result.configure(text='The factorial of {} is {}'.format(user_input, factorial))


root = Tk()

label = Label(text='Enter value of n', font=('arial', 16))
label_result = Label(font=('arial', 16))
entry = Entry(font=('arial', 16), width=20)
button = Button(text='Validate', font=('arial', 16), width=20, command=callback)

label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
label_result.grid(row=1, column=1, padx=10, pady=10)
button.grid(row=2, column=1, padx=10, pady=10)


mainloop()
