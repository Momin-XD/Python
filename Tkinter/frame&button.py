from tkinter import *

root=Tk()
root.geometry('600x400')

f1 = Frame(root,bg='grey',borderwidth=5,relief=GROOVE)
f1.pack(side='left',fill=Y)
button=Button(f1,text="click here!",fg="green")
button.pack()

label=Label(f1,text="framework")
label.pack(side="bottom")

f2 = Frame(root,bg='grey',borderwidth=5,relief=RAISED)
f2.pack(fill=X)

def name():
    print("my name is Maddy")

button=Button(f2,text="click here!",fg="purple",command=name)
button.pack()

root.mainloop()