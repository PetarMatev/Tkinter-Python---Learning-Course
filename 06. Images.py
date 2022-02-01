from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Kitchen")
root.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen.png')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open('Images/Kitchen.png'))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
