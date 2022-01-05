from tkinter import *

gui = Tk()
gui.configure(background='#292826')
gui.title("Expense Manager")
gui.geometry("500x600")

font1 = "-family {Open Sans bold} -size 15"
font2 = "-family {Open Sans bold} -size 11"
font3 = "-family {Open Sans Semibold} -size 10"

def openNewWindow():
    newWindow = Toplevel(gui)
    newWindow.configure(background='#292826')
    newWindow.title("Budget Plan")
    newWindow.geometry("500x600")
    l_inv = Label(newWindow, text="Recommended Budget Plan", font=font1, bg="#f9d342", fg="#292826")#292826
    l_inv.pack(fill='x')

    def investment(m):  # 20%
        inv = int(m * 0.1)
        inv2 = int(m * 0.2)
        if str(invest.get()).upper() == 'Y':
            l_inv = Label(newWindow, text=f"Invest -> Rs. {inv}", font=font1, bg="#f9d342", fg="#292826")
            l_inv.pack(fill='x', padx=10, pady=10)
            l_save = Label(newWindow, text=f"Savings -> Rs. {inv}", font=font1, bg="#f9d342", fg="#292826")
            l_save.pack(fill='x', padx=10, pady=10)
        else:
            l_save = Label(newWindow, text=f"Savings -> Rs. {inv2}", font=font1, bg="#f9d342", fg="#292826")
            l_save.pack(fill='x', padx=10, pady=10)

    def groceries(m):  # 40%
        gr = int(m * 0.4)
        l_groc = Label(newWindow, text=f"Groceries -> Rs. {gr}", font=font1, bg="#f9d342", fg="#292826")
        l_groc.pack(fill='x', padx=10, pady=10)

    def course(m):  # 30%
        co = int(m * 0.3)
        l_co = Label(newWindow, text=f"Course Material -> Rs. {co}", font=font1, bg="#f9d342", fg="#292826")
        l_co.pack(fill='x', padx=10, pady=10)

    def fun(m):  # 10%
        ft = int(m * 0.1)
        l_ft = Label(newWindow, text=f"Entertainment -> Rs. {ft}", font=font1, bg="#f9d342", fg="#292826")
        l_ft.pack(fill='x', padx=10, pady=10)

    def trans(m):  # 10%
        ft = int(m * 0.1)
        l_ft = Label(newWindow, text=f"Transport -> Rs. {ft}", font=font1, bg="#f9d342", fg="#292826")
        l_ft.pack(fill='x', padx=10, pady=10)

    def b_plan():
        m = int(money.get()) - int(loan.get())
        a = str(type.get())
        if a == "Dayscholar":
            investment(m)
            groceries(m)
            course(m)
            trans(m)
        elif a == "Hostler":
            investment(m)
            groceries(m)
            course(m)
            fun(m)
    b_plan()


type_label = Label(gui, text="Dayscholar or Hostler", font=font1, bg="#f9d342", fg="#292826")
type = Entry(gui,bg="#fffbf2")

money_label = Label(gui, text="Total Budget", font=font1, bg="#f9d342", fg="#292826")
money = Entry(gui,bg="#fffbf2")

invest_label = Label(gui, text="Invest(Y/N)", font=font1, bg="#f9d342", fg="#292826")
invest = Entry(gui,bg="#fffbf2")

loan_label = Label(gui, text="Loan/Mandatory expense", font=font1, bg="#f9d342", fg="#292826")
loan = Entry(gui,bg="#fffbf2")

Submit = Button(gui, text="Submit",font=font2, fg="#f9d342", bg="#292826",command=openNewWindow)

type_label.grid(row=0, column=0, pady=5, padx=20)
type.grid(row=0, column=1, pady=5, padx=20)
money_label.grid(row=1, column=0, pady=5, padx=20)
money.grid(row=1, column=1, pady=5, padx=20)
invest_label.grid(row=2, column=0, pady=5, padx=20)
invest.grid(row=2, column=1, pady=5, padx=20)
loan_label.grid(row=3, column=0, pady=5, padx=20)
loan.grid(row=3, column=1, pady=5, padx=20)
Submit.grid(row=4, column=1, pady=20, padx=20)

gui.mainloop()