from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Message Box!")
root.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')
root.geometry("400x400")


def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

checkbox = Checkbutton(root, text="Would you like to SuperSize your order? Check Here!", variable=var,
                       onvalue="SuperSize", offvalue="RegularSize")
checkbox.deselect()
checkbox.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

mainloop()
