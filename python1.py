import tkinter as tk
from tkinter import ttk
from datetime import datetime

def check_date():
    # Get date from entry field
    date = entry1.get()

    # Check if date is in a valid format
    try:
        # Parse the date
        formatted_date = datetime.strptime(date, "%d/%m/%y")
        return True
    except ValueError:
        return False

def check_sum():
    # Get number from entry field
    number = entry3.get()

    # Check if number is a valid number
    try:
        # Parse the number
        formatted_number = int(number)
        return True
    except ValueError:
        return False

# Function to sort the Treeview by column
def sort_treeview(tree, col, descending):
    data = [(tree.set(item, col), item) for item in tree.get_children('')]
    data.sort(reverse=descending)
    for index, (val, item) in enumerate(data):
        tree.move(item, '', index)
    tree.heading(col, command=lambda: sort_treeview(tree, col, not descending))

# Create the main window
root = tk.Tk()
root.title("Data table")
root.iconbitmap(r'E:/Icon.ico')
# Create three entry fields for the data
entry1 = ttk.Entry(root)
entry2 = ttk.Combobox(root,values=('картошка', 'морковка', 'капуста', 'укроп'))
entry3 = ttk.Entry(root)

label1 = ttk.Label(text="Date")
label2 = ttk.Label(text="Category")
label3 = ttk.Label(text="Sum")

label1.pack()
entry1.pack()

label2.pack()
entry2.pack()

label3.pack()
entry3.pack()

# define columns

columns = ('Дата', 'Категория', 'Сумма')

tree = ttk.Treeview(root, columns=columns, show='headings')
# Configure column headings and sorting functionality
for col in columns:
    tree.heading(col, text=col, command=lambda c=col: sort_treeview(tree, c, False))
    tree.column(col, width=100)



tree.pack()

# Work with data
data = []

def add_row():
    if check_date():
        if check_sum():
            data = [entry1.get(), entry2.get(), entry3.get()]
            # Insert the data into the treeview
            tree.insert('', 'end', values=data)

            # Clear the entry fields
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            entry3.delete(0, tk.END)
        else:
            entry3.delete(0, tk.END)
            entry3.insert(0,"9999")
    else:
        entry1.delete(0, tk.END)
        entry1.insert(0,"31/12/23")

def delete_row():
    index = tree.focus()
    tree.delete(index)

# Create the buttonы
add_row_button = ttk.Button(text="Add Row", command=add_row)
add_row_button.pack()

delete_row_button = ttk.Button(text="Delete Row", command=delete_row)
delete_row_button.pack()




# Run the main loop
root.mainloop()