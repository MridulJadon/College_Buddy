from tkinter import *
from PIL import Image,ImageTk
import mysql.connector as msc
from subprocess import call

def notepad():

 call(["python", r"..\Notepad.py"])

def todoList():

 call(["python", r"..\To_Do_list.py"])

def gmap():

 call(["python", r"..\Map.py"])

def CG_calc():

 call(["python", r"..\CGPA_Calculator.py"])

def EM():

 call(["python", r"..\Expense_Manager.py"])


gui=Tk()
gui.title("College Buddy")
gui.configure(background="#292826")
gui.geometry("1000x600")

font1 = "-family {Open Sans bold} -size 15"
font2 = "-family {Open Sans bold} -size 40"
font3 = "-family {Open Sans Semibold} -size 10"

l1=Label(gui,text="COLLEGE BUDDY", bg="#f9d342", fg="#292826",anchor='n')
l1.configure(font=font2)
l1.pack(fill='x')
b1=Button(gui,text="Notepad",command=notepad, fg="#f9d342", bg="#2e2d2a")
b1.configure(font=font1)
b1.pack(fill='x',padx=10,pady=10)
b1=Button(gui,text="To-Do List",command=todoList, fg="#f9d342", bg="#2e2d2a")
b1.configure(font=font1)
b1.pack(fill='x',padx=10,pady=10)
b1=Button(gui,text="Guide Map",command=gmap, fg="#f9d342", bg="#2e2d2a")
b1.configure(font=font1)
b1.pack(fill='x',padx=10,pady=10)
b1=Button(gui,text="CGPA Calculator",command=CG_calc, fg="#f9d342", bg="#2e2d2a")
b1.configure(font=font1)
b1.pack(fill='x',padx=10,pady=10)
b1=Button(gui,text="Expense Manager",command=EM, fg="#f9d342", bg="#2e2d2a")
b1.configure(font=font1)
b1.pack(fill='x',padx=10,pady=10)

gui.mainloop()
