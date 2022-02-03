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

# Create Edit Function to update a Record

def update():
    # Create a database or connect to one
    connection = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = connection.cursor()

    record_id = delete_box.get()
    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
    
        WHERE oid = :oid""",
        {
            'first': first_name_editor.get(),
            'last': last_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid':record_id
        })


    # Commit changes
    connection.commit()
    # Close Connection
    connection.close()

    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Edit a Record")
    editor.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')
    editor.geometry("400x200")

    # Create a database or connect to one
    connection = sqlite3.connect("address_book.db")
    # Create cursor
    cursor = connection.cursor()


    record_id = delete_box.get()
    #  Query the datbase
    cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = cursor.fetchall()


    # Create Global Variables for text box names
    global first_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Text Boxes.
    first_name_editor = Entry(editor, width=30)
    first_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # Create Text Box Labels
    first_name_label = Label(editor, text="First Name")
    first_name_label.grid(row=0, column=0, pady=(10, 0))
    last_name_label = Label(editor, text="Last Name")
    last_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Loop Through Results

    for record in records:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])



    # Create a Save Button to Save edited Recored
    edit_button_editor = Button(editor, text="Save Record", command=update)
    edit_button_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

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
    query_label.grid(row=12, column=0, columnspan=2)

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
delete_box_label = Label(root, text="Select ID")
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

# Create an Update Button
edit_button = Button(root, text="Edit Record", command=edit)
edit_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

# Commit changes
connection.commit()

# Close Connection
connection.close()

root.mainloop()
