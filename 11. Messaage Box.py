from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box!")
root.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')


def popup():
    response = messagebox.askquestion("This is my popup!", "Hello World!")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()
