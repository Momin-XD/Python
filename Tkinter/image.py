from tkinter import *
from PIL import Image,ImageTk

# Create main window
root = Tk()

# Width x Height
root.geometry('900x600')

# Add title
root.title("My First Tkinter App")


# restricting window size
root.minsize(200,200)
root.maxsize(1300,1200)

# Add an image
# photo = PhotoImage(file="image.png")

# Add image otherthen png
image = Image.open("bird.jpg")
image=image.resize((600,700))
photo = ImageTk.PhotoImage(image)

# Add a label
label = Label(text="Hello, Tkinter!")
label = Label(image=photo)
label.pack()

root.mainloop()