from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('733x366')
root.title('Pycharm')

def myfunc():
    print("This is the practice program")


def help():
    # tmsg.showinfo("Help","God will help you soon")
    tmsg.askokcancel("padhai","Thoda or padhoge")

# non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label='File',command=myfunc)
# mymenu.add_command(label='Exit',command=quit)
# root.config(menu=mymenu)



mainmenu = Menu(root)

m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label='New Text File',command=myfunc)
m1.add_command(label='New Window',command=myfunc)
m1.add_separator()
m1.add_command(label='Open File',command=myfunc)
m1.add_command(label='Open Folder',command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='File',menu=m1)


m2 = Menu(mainmenu,tearoff=1)
m2.add_command(label='Undo',command=myfunc)
m2.add_command(label='Redo',command=myfunc)
m2.add_separator()
m2.add_command(label='Cut',command=myfunc)
m2.add_command(label='Copy',command=myfunc)
m2.add_command(label='Paste',command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Edit',menu=m2)


m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label='Help',command=help)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Help',menu=m2)

root.mainloop()