#!/usr/bin/python3
import datetime
import pyttsx3
import pip
current_time=datetime.datetime.now()
name=input("enter your name")
add=input("do you want to add two numberes")
if add==YES:
 print("enter two numberes")
 num1=input("enter first number")
 num2=input("enter second number")
 add_numberes(num1,num2)
s=input("do want to sort a list?")
if s==YES:
  l=[]
  temp=input()
  l.append(temp)
  sorting(l)
def your_name(name):
   dir(pyttsx3)
   sound_driver=pyttsx3.init()
   sound_driver.say(name)
   sound_driver.runWait()
def greet(current_time):
    if now.hour<12 and now.hour>5:
       print('goodmorning')
    elif now.hour>12 and now.hour<16:
        print("GOOD afternoon")
    elif now.hour>16 and now.hour<20:
         print("good evening")
    elif now.hour>20 and now.hour<5: 
         print("good night")  
