from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()
root.geometry('455x233')
root.title("Slider")

# myslider = Scale(root,from_=5, to=100).pack()

def func():
    tmsg.showinfo("Age",f"Your age is {myslider2.get()}")


Label(root,text="Select your age").pack()
myslider2 = Scale(root,from_=5, to=100, orient=HORIZONTAL)
myslider2.pack()
Button(root, text="Confirm", command=func).pack()




root.mainloop()