from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Kitchen")
root.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')

# creating all of our images here:

my_img1 = ImageTk.PhotoImage(Image.open('Images/Kitchen 1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('Images/Kitchen 2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('Images/Kitchen 3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('Images/Kitchen 4.jpg'))

# we added all images into Python List

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward_button(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward_button(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back_button(image_number - 1))

    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back_button(image_number):

    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward_button(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back_button(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back_button, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward_button(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
