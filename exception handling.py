'''
from tkinter import *
root=Tk()
root.mainloop()
'''
from withdraw import*
amt=int(input("enter ur amt"))
try:
     withdraw(amt)
     expect :'Invalidfund'as e:
     print(e)
