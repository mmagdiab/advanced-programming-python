"""
Dictionaries provide a convenient way to store structured data. Here is an example dictionary:
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
Write a program that reads through any dictionary like this and prints the following:
(a) All the users whose phone number ends in an 8
(b) All the users that don’t have an email address listed
"""

d = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
     {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
     {'name': 'Princess', 'phone': '555-3141', 'email': ''},
     {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]

a_result = [user for user in d if user['phone'][-1] == '8']
b_result = [user for user in d if user['email'] == '']

print(a_result)
print(b_result)
