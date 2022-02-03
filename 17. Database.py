from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

# Database

root = Tk()
root.title("Message Box!")
root.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')
root.geometry("400x400")

# Create a database or connect to one
connection = sqlite3.connect("address_book.db")

# Create cursor
cursor = connection.cursor()

'''
# Create Table
cursor.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''


# Create a Function to Delete a Record
def delete():
    # Create a database or connect to one
    connection = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = connection.cursor()

    # Delete a Record
    cursor.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    # Commit changes
    connection.commit()

    # Close Connection
    connection.close()


# Create Submit Function for database

def submit():
    # Create a database or connect to one
    connection = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = connection.cursor()

    # Insert Into Table.
    cursor.execute('INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)',
                   {
                       'first_name': first_name.get(),
                       'last_name': last_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get()
                   })

    # Commit changes
    connection.commit()

    # Close Connection
    connection.close()

    # Clear The Text Boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create Query Function

def query():
    # Create a database or connect to one
    connection = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = connection.cursor()

    #  Query the datbase
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    # print(records)

    # Loop Through Results
    print_record = ''
    for record in records:
        print_record += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=11, column=0, columnspan=2)

    # Commit changes
    connection.commit()

    # Close Connection
    connection.close()


# Create Text Boxes.
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0, pady=(10, 0))
last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_button = Button(root, text="Add Record to Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a Query Button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create A Delete Button
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

# Commit changes
connection.commit()

# Close Connection
connection.close()

root.mainloop()
