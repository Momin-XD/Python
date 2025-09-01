from tkinter import *
import tkinter.messagebox as tmsg

def getvals():
    with open("Travler.txt",'a') as f:
        f.write(f"{nameval.get()}\t,{phoneval.get()}\t,{genderval.get()}\t,{emergencyval.get()}\t,{paymentval.get()}\t,{var.get()}\t,{foodserviceval.get()}\n")
    tmsg.showinfo("Confirmation Box",f"Your will have {var.get()} service and pament method is {paymentval.get()}")

    print("Done!")

root = Tk()

root.geometry('600x400')
root.title("MK Travles Form")

# labeling text for the form
label=Label(root,text="Welcome to MK Travels",font='comicsansms 12 bold', pady=5)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
payment=Label(root,text="Pament Mode")

# pack text for the form
label.grid(row=0,column=3)
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)

# tkinter variable for the form
nameval= StringVar()
phoneval= StringVar()
genderval= StringVar()
emergencyval= StringVar()
paymentval= StringVar()
foodserviceval= IntVar()

# entries for the form
nameentry= Entry(root,textvariable=nameval)
phoneentry= Entry(root,textvariable=phoneval)
genderentry= Entry(root,textvariable=genderval)
emergencyentry= Entry(root,textvariable=emergencyval)
paymententry= Entry(root,textvariable=paymentval)

# packing the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)


# check box
foodservice = Checkbutton(text="Want to prebook you meal",variable=foodserviceval)
foodservice.grid(row=6,column=3)


# Radio button
# var=IntVar()
var=StringVar()
var.set("Radio")
label = Label(root,text="Which Service you prefer ").grid(row=7,column=3)
radio = Radiobutton(root, text="Vip",variable=var,value="Vip")
radio.grid(row=8,column=3)
radio = Radiobutton(root, text="Premium",variable=var,value="Premium")
radio.grid(row=9,column=3)
radio = Radiobutton(root, text="Regular",variable=var,value="Regular")
radio.grid(row=10,column=3)



# applying button
button = Button(text="Submit the details", command=getvals)
button.grid(row=11,column=3)
root.mainloop()
