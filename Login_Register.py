from tkinter import *
import sqlite3
import math
import random
import smtplib
from tkinter import messagebox
from subprocess import call

# create databse and table
con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    username text, 
                    password text,
                    email text
                )
            ''')
con.commit()

# create window
root = Tk()
root.geometry('500x450')
root.title('Login Registration form')
root.resizable(False, False)

# variable to hold entry widget data
fullname = StringVar()
username = StringVar()
password = StringVar()
username_lo = StringVar()
password_lo = StringVar()
email = StringVar()
otp = StringVar()


# insert data on our record
def insert_record():
    count = 0
    warn = ''
    mail = email.get()

    if fullname.get() == '':
        warn = "Name can't be empty"
    else:
        count += 1

    if username.get() == '':
        warn = "Username can't be empty"
    else:
        count += 1

    if email.get() == '':
        warn = "Email - id can't be empty"
    else:
        count += 1

    if password.get() == '':
        warn = "Password can't be empty"
    else:
        count += 1

    if count == 4:
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :username, :password, :email)", {
                'name': fullname.get(),
                'username': username.get(),
                'password': password.get(),
                'email': email.get()

            })
            con.commit()
            otpverficitation(mail)
        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)


# select data from records
def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            usern = row[1]
            passwo = row[2]

    except Exception as ep:
        messagebox.showerror('', ep)
    count = 0
    if username_lo.get() == "":
        warn = "Username can't be empty"
    else:
        count += 1

    if password_lo.get() == "":
        warn = "Password can't be empty"
    else:
        count += 1

    if count == 2:
        if usern == username_lo.get() and passwo == password_lo.get():
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            call(["python", "..\main.py"])

        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)


def login():
    f = Frame(root, height=450, width=500, bg='#292826')
    Label(f, text='Login', font=("Open Sans", 30, "bold"), bg='#292826', fg='#f9d342').place(x=200, y=80)
    Label(f, text='(Fill all form field to go to next step)', font=("Open Sans", 9, "bold"), fg='#a68c28',bg='#292826').place(x=145, y=160)
    Label(f, text='Username', font=("Open Sans", 12, "bold"), fg='#f9d342', bg='#292826').place(x=150, y=195)
    user = Entry(f, textvariable=username_lo, font=('Open Sans', 10, 'normal'), width=30)
    user.place(x=150, y=220)
    Label(f, text='Password', font=("Open Sans", 12, "bold"), fg='#f9d342', bg='#292826').place(x=150, y=245)
    passw = Entry(f, textvariable=password_lo, font=('Open Sans', 10, 'normal'), width=30, show="*")
    passw.place(x=150, y=270)
    Button(f, text='Log in', font=("Open Sans", 12, "bold"), bg='#292826', fg='#f9d342', command=login_response).place(x=220, y=320)
    Label(f, text="Don't have account", font=("Open Sans", 10, "bold"), fg='#a68c28', bg='#292826').place(x=145, y=390)
    Button(f, text='Register Here', font=("Open Sans", 8, "bold"), bg='#292826', fg='#f9d342', command=registration).place(x=280,y=390)
    f.place(x=0, y=0)


def registration():
    f = Frame(root, height=450, width=500, bg='#292826')
    Label(f, text='Registration', font=("Open Sans", 30, "bold"), bg='#292826', fg='#f9d342').place(x=140, y=20)

    Label(f, text='Full Name', font=("Open Sans", 12, "bold"), fg='#f9d342', bg='#292826').place(x=150, y=115)
    Entry(f, textvariable=fullname, font=('Open Sans', 10, 'normal'), width=30).place(x=150, y=140)

    Label(f, text='Username', font=("Open Sans", 12, "bold"), fg='#f9d342', bg='#292826').place(x=150, y=165)
    Entry(f, textvariable=username, font=('Open Sans', 10, 'normal'), width=30).place(x=150, y=190)

    Label(f, text='Email Id', font=("Open Sans", 12, "bold"), fg='#f9d342', bg='#292826').place(x=150, y=215)
    Entry(f, textvariable=email, font=('Open Sans', 10, 'normal'), width=30).place(x=150, y=240)

    Label(f, text='Password', font=("Open Sans", 12, "bold"), fg='#f9d342', bg='#292826').place(x=150, y=265)
    Entry(f, textvariable=password, font=('Open Sans', 10, 'normal'), width=30).place(x=150, y=290)

    Button(f, text='Register', font=("Open Sans", 12, "bold"), bg='#292826', fg='#f9d342', command=insert_record).place(x=210, y=340)

    Label(f, text="Already have account", font=("Open Sans", 10, "bold"), fg='#a68c28', bg='#292826').place(x=140,y=400)
    Button(f, text='Login Here', font=("Open Sans", 8, "bold"), bg='#292826', fg='#f9d342', command=login).place(x=290, y=400)
    f.place(x=0, y=0)


def otpverficitation(mail):
    global OTP
    digits = "0123456789"
    OTP = ""

    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    # print(OTP)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('fitvoid01@gmail.com', 'fitvoid@123')
    subject = 'Your OTP is: '
    body = OTP

    msg = f"Subject : {subject} \n\n {body}"

    server.sendmail('fitvoid01@gmail.com', f'{mail}', msg)

    print('Mail has been send')

    f = Frame(root, height=450, width=500, bg='#292826')
    Label(f, text='OTP Verification', font=("Open Sans", 30, "bold"), bg='#292826', fg="#f9d342").place(x=100, y=80)

    Label(f, text='(OTP sent, please check your mail)', font=("Open Sans", 10, "bold"), fg='#a68c28',bg='#292826').place(x=135, y=140)

    Label(f, text='Enter OTP:', font=("Open Sans", 12, "bold"), fg="#f9d342", bg='#292826').place(x=147, y=200)
    Entry(f, textvariable=otp, font=('Open Sans', 10, 'normal'), width=30).place(x=150, y=230)

    Button(f, text='Verify', font=("Open Sans", 12, "bold"), bg='#292826', fg="#f9d342",command=lambda: verify(otp.get())).place(x=152, y=270)
    Button(f, text='Resend', font=("Open Sans", 12, "bold"), bg='#292826', fg="#f9d342").place(x=230, y=270)
    f.place(x=0, y=0)


def verify(entryotp):
    global OTP

    if entryotp == OTP:
        messagebox.showinfo('confirmation', 'Record Saved')
        login()
    else:
        messagebox.showerror('Wrong', 'Please Enter Valied OTP')


login()
root.mainloop()