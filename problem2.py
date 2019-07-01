from googlesearch import search
import time
data=input("enter the data which you want to search")
url=[]
for i in search(data,stop=10):
   print(i)
   time.sleep(1)
   url.append(i)
