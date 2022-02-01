from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Message Box!")
root.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=400)
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_button = Button(root, text="Click Me!", command=slide).pack()

mainloop()
