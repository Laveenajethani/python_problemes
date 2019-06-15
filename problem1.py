import datetime
name=input('enter your name :')
age=int(input('enter your age: '))
now=datetime.datetime.now()
print(name," will turn 95 in ",(95-age)+now.year)
