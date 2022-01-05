from tkinter import *
from tkinter import messagebox

tasks_list = []

counter = 1


def inputError():

    if enterTaskField.get() == "":

        messagebox.showerror("Input Error")

        return 0

    return 1


def clear_taskNumberField():

    taskNumberField.delete(0.0, END)


def clear_taskField():

    enterTaskField.delete(0, END)

def insertTask():
    global counter

    value = inputError()

    if value == 0:
        return

    content = enterTaskField.get() + "\n"

    tasks_list.append(content)

    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

    counter += 1

    clear_taskField()

def delete():
    global counter

    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return

    number = taskNumberField.get(1.0, END)

    if number == "\n":
        messagebox.showerror("input error")
        return

    else:
        task_no = int(number)

    clear_taskNumberField()

    tasks_list.pop(task_no - 1)

    counter -= 1

    TextArea.delete(1.0, END)

    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])


# Driver code
if __name__ == "__main__":

    gui = Tk()
    gui.configure(background="#292826")
    gui.title("To-Do List")
    gui.geometry("500x600")

    font1 = "-family {Open Sans bold} -size 15"
    font2 = "-family {Open Sans bold} -size 10"
    font3 = "-family {Open Sans Semibold} -size 10"

    enterTask = Label(gui, text="Enter Your Task", font=font1, bg="#f9d342", fg="#292826")
    enterTaskField = Entry(gui,bg="#fffbf2")

    Submit = Button(gui, text="Submit",font=font2, fg="#f9d342", bg="#292826", command=insertTask)

    TextArea = Text(gui, height=5, width=25, font=font3,bg="#fffbf2")
    taskNumber = Label(gui, text="Delete Task", font=font1, bg="#f9d342", fg="#292826")
    taskNumberField = Text(gui, height=1, width=2, font=font3,bg="#fffbf2")

    delete = Button(gui, text="Delete",font=font2,fg="#f9d342", bg="#292826", command=delete)
    Exit = Button(gui, text="Exit",font=font2, fg="#f9d342", bg="#292826", command=exit)

    enterTask.pack(fill='x')
    enterTaskField.pack(fill='x', pady=10, padx=10)
    Submit.pack(fill='x', padx=210)
    TextArea.pack(fill='x', pady=20, padx=10)
    taskNumber.pack(fill='x')
    taskNumberField.pack(fill='x', pady=10, padx=220)
    delete.pack(fill='x', padx=210)
    Exit.pack(fill='x', padx=210, pady=30)

    gui.mainloop()
