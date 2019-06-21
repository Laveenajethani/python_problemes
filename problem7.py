#!usr/bin/python3
option='''
press 1 for touch : create a new file
press 2  for touch -n  : create number of files
press 3 for touch -m  : show file modification
'''
import os
import time
print(option)
p=input("enter your choice option")
def mkfile():
     f=open('new.txt','w+')
     f.close()
def number_of_files(n):
      for i in range(n):
         file_name='new'+i+'.txt'
         f=open('file_name','w+')
         f.close()
def modify_file(file_name):
      modified = os.path.getmtime(file_name)
      print("Date modified:"+time.ctime(modified))
if p=="1":
     mkfile()
elif p=="2":
      n=input("enter the number of file which you want to  create")
      number_of_file(n)
elif p=="3":
    file_name=input("enter file  name")
    modify_file(file_name)
else:
   print("invalid option ....")
~
