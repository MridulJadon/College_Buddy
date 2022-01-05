from tkinter import *

gui = Tk()
gui.configure(background='#292826')
gui.title("CGPA Calculator")
gui.geometry("630x600")

font1 = "-family {Open Sans bold} -size 15"
font2 = "-family {Open Sans bold} -size 10"
font3 = "-family {Open Sans Semibold} -size 10"

l1 = Label(gui, text="Enter the total number of subjects", font=font1, bg="#f9d342", fg="#292826")
l1.grid(row=0, column=1)

box_num = Entry(gui,bg="#fffbf2")
box_num.grid(row=1, column=1, pady=10)

def gpa_calc(credits,grade_point,g):
    if grade_point == "S":
        grade_point = 10
    elif grade_point == "A":
        grade_point = 9
    elif grade_point == "B":
        grade_point = 8
    elif grade_point == "C":
        grade_point = 7
    elif grade_point == "D":
        grade_point = 6
    elif grade_point == "E":
        grade_point = 5
    elif grade_point == "F":
        grade_point = 4

    return int(g) + (int(credits) * int(grade_point))

def total_cred(credits,c):
    return int(c) + int(credits)

def cgpa(gpa, tc):
    return gpa/tc

tb=[]
def textboxes():
    a = int(box_num.get())
    for i in range(5, a+5):
        for j in range(3):
            text_box= Entry(gui)
            text_box.grid(row=i, column=j, pady=20, padx=5)
            tb.append(text_box)

def getval():
    a = len(tb)
    i = 0
    g = 0
    c = 0
    while i<a:
        cred = str(tb[i+1].get())
        grd = str(tb[i+2].get()).upper()
        g = gpa_calc(cred,grd,g)
        c = total_cred(cred,c)
        i = i+3
    ans = cgpa(g,c)
    l4 = Label(gui, text=f"Your CGPA is: {ans}", font=font1, bg="#f9d342", fg="#292826")
    l4.grid(column=1)

b1 = Button(gui, text="Submit",font=font2, fg="#f9d342", bg="#292826",command=textboxes)
b1.grid(row=2, column=1)

l2 = Label(gui, text="Subject", font=font1, bg="#f9d342", fg="#292826")
l2.grid(row=3, column=0, pady=10, padx=30)
l3 = Label(gui, text="Credits", font=font1, bg="#f9d342", fg="#292826")
l3.grid(row=3, column=1, pady=10, padx=30)
l4 = Label(gui, text="Grade", font=font1, bg="#f9d342", fg="#292826")
l4.grid(row=3, column=2, pady=10, padx=35)

calculate = Button(gui, text="Calculate",font=font2, fg="#f9d342", bg="#292826",command=getval)
calculate.grid(row=4, column=1, pady=10)
# box_text = Label(gui, text="Enter subject_name, number_of_credits, grade_obtained", font=font1, bg="#f9d342", fg="#292826")
# box_text.pack(fill='x',pady=5)

gui.mainloop()
