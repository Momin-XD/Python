from tkinter import *

root=Tk()
root.geometry('600x400')

user=Label(root,text="Username: ")
password=Label(root,text="Password: ")
user.grid()
password.grid()

userval=StringVar()
passval=StringVar()

userentry= Entry(root,textvariable=userval)
passentry= Entry(root,textvariable=passval)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)


button=Button(root,text="Submit").grid()


root.mainloop()