#Question 1
def factorial(n):
    result = 1 
    for i in range(1 , n + 1):
        result *= i
    return result

def pow_2(n , pow):
    x = n 
    for i in range(pow - 1):
        n *= x
    return n


X = eval(input("Enter X: "))
Y = 0 
for i in range(1 , 11):
    Y += pow_2(X , i) / factorial(i)

print(round(Y , 2))

#Question 2
d = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
     {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
     {'name': 'Princess', 'phone': '555-3141', 'email': ''},
     {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]

def phone_end(num):
    persons = []
    for i in d:
        if i['phone'][-1] == str(num):
            persons.append(i['name'])
    return persons

def null_emails():
    persons = []
    for i in d:
        if i['email'] == '':
            persons.append(i['name'])
    return persons

def email_signiture(signuture):
    persons = []
    for i in d:
        if i['email'][len(i['email']) - len(signuture):] == signuture:
            persons.append(i['name'])
    return persons

#Question 3
class Password_manager:
    def __init__(self):
        self.last_password = []
    def get_password(self):
        return self.last_password[-1]
    def set_password(self,password):
        if password not in self.last_password:
            self.last_password.append(password)
            return "Password was set"
        else:
            return "Please Enter New Password"
    def is_correct(self,password):
        return self.get_password() == password

password = Password_manager()

print(password.set_password("Ahmed"))
print(password.get_password())
print(password.set_password("Ahmed"))
print(password.is_correct("Ahmed"))
print(password.is_correct("Ahm"))

#Question 4
from tkinter import *

root = Tk()
root.geometry('400x150')

def callback():
    num = int(entry.get())
    ans = sum(range(1 , num + 1))
    result.config(text=f'1 + 2 + ... + {num} = {ans}')

label1 = Label(text="Enter value of integer N: ")
label1.grid(row=0,column=0,padx=10,pady=10)

entry = Entry()
entry.grid(row=0,column=1,padx=10,pady=10)

result = Label()
result.grid(row=1,column=1,padx=10,pady=10)

button = Button(text="Validate" , command=callback)
button.grid(row=2,column=1,padx=10,pady=10)

mainloop()