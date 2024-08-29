# This program says hello and asks for my name.
print('Hello, world!')
print('What is your name?')    # ask for their name
myName = input()
print('The length of your name is:')
print(len(myName))

birth_month = input ('What month is your birthday?')


if birth_month == 'August':
    print('Happy Birthday Month')

else:
    print ('Your birthday is not in this month')

from datetime import date 

today = date.today ()
print (today)
this_month = today.month
print (this_month)



