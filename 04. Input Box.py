from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()

# default text
e.insert(0, "Enter Your Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

# Event Loop
root.mainloop()
