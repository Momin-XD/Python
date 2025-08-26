from tkinter import *

def Change():
    root.geometry(f"{widthval.get()}x{heightval.get()}")


root = Tk()
root.geometry('900x700')

width=Label(text="Width").grid(row=1,column=1)
height=Label(text="Height").grid(row=2,column=1)

widthval=StringVar()
heightval=StringVar()

widthentry=Entry(root,textvariable=widthval).grid(row=1,column=2)
heightentry=Entry(root,textvariable=heightval).grid(row=2,column=2)

button = Button(text="Change the size of window", command=Change).grid(row=3,column=3)

root.mainloop()