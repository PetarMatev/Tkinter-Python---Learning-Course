from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is John Elder")

# shoving it into the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

# Event Loop
root.mainloop()
