#!/usr/bin/python3
op='''
press 1 cat  -A show all data
press 2 cat  -e  display $ at end of each line 
press 3 cat  -n display line numbers
'''

print(op)
n=input("enter your choice")

if(n=='1'):
  i=input("enter your file name")
  f=open('i','r')
  data=f.read()
  print(data)
  f.close()

elif(n=='2'):
  i=input("enter your file name")
  f=open('i','r')
  data=f.read()
  a=data.split('\n')
  for i in a:
    print(i+"$")

elif(n=='3'):
  i=input("enter your file name")
  f=open('i','r')
  data=f.read()
  a=data.split('\n')
  l=1
  for i in a:
     print(str(l)+" "+i)
     l=l+1 

else:
    print("Invalid output")



