
from datetime import date, datetime, timedelta
from termcolor import colored
from tabulate import tabulate


w = open("C:\\Taca\\pythonproba.txt", "a")
w.write("Taca je bila ovde!\n")
w.close()

myList = []
with open("C:\\Taca\\pythonproba.txt", "r") as r:
    for i in r:
        myList.append(i)

print(myList)

w = open("C:\\Taca\\pythonproba.txt", "w")
w.close()

with open("C:\\Taca\\pythonproba.txt", "a") as a:
    for i in myList:
        a.writelines(i)
        
        
        


    
    
  
    
    

