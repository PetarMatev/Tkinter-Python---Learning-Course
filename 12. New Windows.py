from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Message Box!")
root.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')


def open():
    global my_img
    top = Toplevel()
    top.title("My Second Window!")
    top.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')
    label = Label(top, text="Hello World!")
    my_img = ImageTk.PhotoImage(Image.open('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg'))
    my_label = Label(top, image=my_img).pack()
    label.pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()
