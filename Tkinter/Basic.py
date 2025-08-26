'''
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Add a button
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

# Run the GUI loop
root.mainloop()
'''


from tkinter import *
from PIL import Image,ImageTk

# Create main window
root = Tk()

# Width x Height
root.geometry('900x600')

# Add title
root.title("My First Tkinter App")


# restricting window size
# root.minsize(200,200)
# root.maxsize(1200,1200)

# Add an image
# photo = PhotoImage(file="image.png")

# Add image otherthen png
# image = Image.open("bird.jpg")
# photo = ImageTk.PhotoImage(image)

# Add a label
# label = Label(text="Hello, Tkinter!")
# label = Label(image=photo)
# label.pack()


# More label attributes
# text   - adds Text
# bd     - background
# fg     - foreground
# font   - sets the Font
# padx   - x padding
# pady   - y padding
# relief - border styling

# label=Label(text="Tkinter is a binding to the Tk GUI toolkit for Python. \nIt is the standard Python interface to the Tk GUI toolkit,[1] and is Python's de facto standard GUI.\n[2] Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python.",bg="light green", fg="Blue", font ="ariel 15", padx=113,pady=34,borderwidth=15,relief=SUNKEN)

# # IMPORTANT pack attribute
# # anchor = pasition
# # side=top,bottom,left, right
# # fill=x or y
# # padx
# # pady
# label.pack(anchor="center",fill=X)


# Run the GUI loop
root .mainloop()