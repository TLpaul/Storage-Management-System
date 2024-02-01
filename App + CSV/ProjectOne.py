import tkinter as tk
from tkinter import messagebox
import re
import csv


storage_text = None # this is the window on the bottom of the app to display the texts
window = None # This is the window you're using

# Dictionaries to store storage, quanity, first name, last name, phone number, and email
storage_items = {}
quantity = {}
first_name = {}
last_name = {}
phone_number = {}
email = {}

def delete_items(itemID):
    """
    Delete an item from the storage system.

    Parameters:
    - itemID (int): The unique identifier of the item to be deleted.

    Clears the text box at the bottom and checks if the item exists in the storage system.
    If the item exists, it is deleted along with associated information (quantity, first name, last name, phone number, email).
    If the item does not exist, a message is displayed indicating that it is not in the system.

    Displays a messagebox with information about the deletion or the non-existence of the item.

    Example:
    delete_items(42)  # Deletes the item with ID 42 from the storage system.

    """
    #clear the text box at the bottom
    storage_text.delete(1.0, tk.END)

    #check to see if it exists and if not to send a message that it does not exist
    if itemID in storage_items:
        del storage_items[itemID]
        del quantity[itemID]
        del first_name[itemID]
        del last_name[itemID]
        del phone_number[itemID]
        del email[itemID]

        #send a message and say that it was deleted
        messagebox.showinfo("Item Deleted", f"Item {itemID} has been deleted.")

    else:
        #send a message and say that it does not exist
        messagebox.showinfo("Item Not Found", f"Item {itemID} is not in the system.")


#use this to read the csv file
def read_csv():

    """
    Read data from a CSV file and update the storage system.

    Clears the text box at the bottom, opens the 'ProjectStorage.csv' file, and creates a CSV reader.
    Iterates over rows in the CSV file, extracting values using column names.
    Updates the storage system with the extracted information.

    Updates:
    - storage_items
    - quantity
    - first_name
    - last_name
    - phone_number
    - email

    Displays a messagebox to notify the user that the storage has been updated.

    Example:
    read_csv()  # Reads data from 'ProjectStorage.csv' and updates the storage system.

    """

    #clear the text box at the bottom
    storage_text.delete(1.0, tk.END)
    # Open the CSV file
    with open('ProjectStorage.csv', 'r') as file:
        # Create a CSV reader
        csv_reader = csv.DictReader(file)

        # Iterate over rows
        for row in csv_reader:
            #find value from rows using the column name
            itemID = row['itemID']
            product = row['Product']
            Quantity = row['Quantity']
            FirstName = row['First Name']
            LastName = row['Last Name']
            PhoneNumber = row['Phonenumber']
            Email = row['Email']

            # store in the directiry
            storage_items[itemID] = product
            quantity[itemID] = Quantity
            first_name[itemID] = FirstName
            last_name[itemID] = LastName
            phone_number[itemID] = PhoneNumber
            email[itemID] = Email
            
    #let user know that the storage has been updated
    messagebox.showinfo("Storage Notification", "Storage has been uploaded.")

#use this to read the csv file
def write_csv():

    """
    Write data to a CSV file based on the current storage system.

    Clears the text box at the bottom, opens the 'ProjectStorage.csv' file for writing, and creates a CSV writer.
    Writes the header and iterates over items in the storage system to write data rows in the CSV file.

    Writes:
    - 'itemID'
    - 'Product'
    - 'Quantity'
    - 'First Name'
    - 'Last Name'
    - 'Phonenumber'
    - 'Email'

    Displays a messagebox to notify the user that the storage has been updated.

    Example:
    write_csv()  # Writes data from the current storage system to 'ProjectStorage.csv'.

    """

    #clear the text box at the bottom
    storage_text.delete(1.0, tk.END)
    # Open the CSV file
    with open('ProjectStorage.csv', 'w', newline='') as file:
        # Create a CSV writer
        writer = csv.writer(file)
        header = ['itemID','Product','Quantity','First Name','Last Name','Phonenumber','Email']
        writer.writerow(header)
       
       #forloop to run through and write in the file 
        for itemID, product in storage_items.items():
            # Create a list representing the row
            row = [itemID, storage_items[itemID], quantity[itemID], first_name[itemID], last_name[itemID], phone_number[itemID], email[itemID]]
            writer.writerow(row)             

            
    #let user know that the storage has been updated
    messagebox.showinfo("Storage Notification", "Storage has been updated.")

def add_item(itemID, product,Quantity,FirstName,LastName,PhoneNumber,Email):

    """
    Add an item to the storage system.

    Clears the text box at the bottom and performs validation checks on input parameters.
    Checks for completeness, validity of itemID, quantity, first and last names, product name, email, and phone number.
    Ensures itemID is unique and not already in use.
    Uses regular expression for validating the phone number.
    Displays appropriate messages in case of validation errors.

    Parameters:
    - itemID (str or int): The unique identifier for the item.
    - product (str): The product name.
    - Quantity (str): The quantity of the item.
    - FirstName (str): The first name associated with the item.
    - LastName (str): The last name associated with the item.
    - PhoneNumber (str): The phone number associated with the item (in xxx-xxx-xxxx format).
    - Email (str): The email address associated with the item.

    Example:
    add_item(123, "Laptop", "5", "John", "Doe", "123-456-7890", "john.doe@example.com")
    # Adds an item with the specified details to the storage system.

    """

    #clear the text box at the bottom
    storage_text.delete(1.0, tk.END)

    # Check if itemID and product are not blank
    if not itemID or not product or not FirstName or not LastName or not PhoneNumber or not Email:
        messagebox.showinfo("Incomplete Information", "Please fill out the entire information.")
        return
    
    # Check if itemID contains only digits
    if not itemID.isdigit():
        messagebox.showinfo("Invalid ItemID", "Please enter a valid integer for itemID.")
        return
    
    # Check if quanity contains only digits
    if not Quantity.isdigit():
        messagebox.showinfo("Invalid Quanity", "Please enter a valid integer for quanity.")
        return
    
    # Check if FirstName contains only letters
    if not FirstName.isalpha():
        messagebox.showinfo("Invalid First Name", "Please enter a valid first name with only letters.")
        return

    # Check if LastName contains only letters
    if not LastName.isalpha():
        messagebox.showinfo("Invalid Last Name", "Please enter a valid last name with only letters.")
        return
    
    # Check if product name contains only letters
    if not product.isalpha():
        messagebox.showinfo("Invalid Product Name", "Please enter a valid product name with only letters.")
        return
    
    # Check if email contains only allowed characters
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.")

    # Check if email contains '@' and ends with '.com'
    if '@' not in Email or not Email.endswith('.com'):
        message = "Invalid email format. Please use the correct email format (e.g., user@example.com)."
        messagebox.showinfo("Invalid Email Address", message)
        return

    # Check if '@' and '.' are used only in specific positions
    if Email.count('@') != 1 or Email.count('.') != 1 or Email.index('@') > Email.index('.'):
        message = "Invalid email format. Please use the correct email format (e.g., user@example.com)."
        messagebox.showinfo("Invalid Email Address", message)
        return

    # Check if email contains only allowed characters before '@' and after '.'
    local_part, domain_part = Email.split('@')
    if not all(char in allowed_chars for char in local_part) or not all(char in allowed_chars for char in domain_part):
        message = "Invalid characters in the email address. Please use only letters, numbers, @, and '.'."
        messagebox.showinfo("Invalid Email Address", message)
        return

    
    #make sure we have not used that id yet
    if (itemID in storage_items):
        message = "ItemID you entered is already in use. Try again"
        messagebox.showinfo("Invalid ItemID", message)
        return
    
    # validating the phone number here using regex
    if not re.match(r'^\d{3}-\d{3}-\d{4}$', PhoneNumber):
        messagebox.showinfo("Invalid Phone Number", "Please enter a valid phone number in xxx-xxx-xxxx format.")
        return

    # Add item logic using itemID and product
    storage_items[itemID] = product
    first_name[itemID] = FirstName
    last_name[itemID] = LastName
    phone_number[itemID] = PhoneNumber
    email[itemID] = Email
    quantity[itemID] = Quantity

    # Display message to the user
    messagebox.showinfo("Item Added", f"Item {itemID} has been added successfully.")


# Function to show the most recent items
def most_recent_items():

    """
    Display the most recently added items in the storage system.

    Clears the text widget before updating.
    Creates a list of item details in reverse order based on the storage system.
    Prints the most recent items in the text widget.

    Displays:
    - itemID
    - Product
    - Quantity
    - Full Name (concatenation of first and last names)
    - Phone Number
    - Email

    Example:
    most_recent_items()  # Displays the most recently added items in the storage system.

    """

    # Clear the text widget before updating
    storage_text.delete(1.0, tk.END)
    
    #store the reverse order in this 
    recent_list = []

    #use this loop to save into a list then print the list out backwards
    for itemID, product in storage_items.items():
        
        recent_list.append("\nitemID : "+itemID +"\nProduct: "+ storage_items[itemID] +"\nQuanity: "+quantity[itemID]+"\nFull Name: "+first_name[itemID]+" "+last_name[itemID]+ "\nPhone Number: "+phone_number[itemID]+ "\nEmail: "+email[itemID]+"\n")
    
    #use this to reverse the list
    recent_list.reverse()
    storage_text.insert(tk.END, "Most Recent Stored Storage:\n")

    #use this for loop to print out the list
    for itemID in recent_list:
        storage_text.insert(tk.END, itemID)
    
    storage_text.insert(tk.END, "\n")

# Function to display stored storage
def show_items():

    """
    Display all stored items in the storage system.

    Clears the text widget before updating.
    Prints the details of each stored item, including itemID, product, quantity,
    full name (concatenation of first and last names), phone number, and email address.

    Example:
    show_items()  # Displays all stored items in the storage system.

    """

    # Clear the text widget before updating
    storage_text.delete(1.0, tk.END)
    
    # Display stored storage in the text widget
    storage_text.insert(tk.END, "Stored storage:\n\n")
    for itemID, product in storage_items.items():
        storage_text.insert(tk.END, f"itemID: {itemID}\nProduct: {storage_items[itemID]}\nQuantity: {quantity[itemID]}\nFull Name: {first_name[itemID]} {last_name[itemID]}\nPhone Number: {phone_number[itemID]}\nEmail Address: {email[itemID]}\n\n")
    storage_text.insert(tk.END, "\n")

def finding_item(itemID):

    """
    Find and display details for a specific item in the storage system.

    Clears the text widget before updating.
    Validates that itemID contains only digits.
    Searches for the item in the storage system based on itemID.
    Displays the details of the found item if it exists, otherwise, displays a message.

    Parameters:
    - itemID (str or int): The unique identifier for the item to be found.

    Example:
    finding_item(42)  # Finds and displays details for the item with itemID 42.

    """

    # Clear the text widget before updating
    storage_text.delete(1.0, tk.END)

    # Check if itemID contains only digits
    if not itemID.isdigit():
        messagebox.showinfo("Invalid ItemID", "Please enter a valid integer for itemID.")
        return

    # Search through the dictionary
    if itemID in storage_items:
        storage_text.insert(tk.END, f"Item found:\n\nitemID: {itemID}\nProduct: {storage_items[itemID]}\nQuantity: {quantity[itemID]}\nFull Name: {first_name[itemID]} {last_name[itemID]}\nPhone Number: {phone_number[itemID]}\nEmail Address: {email[itemID]}\n\n")
    else:
        storage_text.insert(tk.END, f"Item not found for itemID: {itemID}")
    storage_text.insert(tk.END, "\n")


  
def open_create_item_window():

    """
    Open a window for creating and adding a new item to the storage system.

    Clears the text widget at the bottom.
    Creates a new top-level window titled "Create Item" with entry widgets for itemID, product, quantity,
    first name, last name, phone number, and email. Also, includes a submit button to add the new item.

    Example:
    open_create_item_window()  # Opens a window for creating and adding a new item to the storage system.

    """

    #clear the text box at the bottom
    storage_text.delete(1.0, tk.END)

    # Function to open the Create Item window
    create_item_window = tk.Toplevel(window)
    create_item_window.title("Create Item")

    # Set the window size to 400x200
    create_item_window.geometry("400x500")

    # Create entry widgets for itemID and product
    label_itemID = tk.Label(create_item_window, text="itemID:", fg="blue")
    entry_itemID = tk.Entry(create_item_window, fg="blue", width=30)
    
    label_product = tk.Label(create_item_window, text="Product Name:", fg="blue")
    entry_product = tk.Entry(create_item_window, fg="blue", width=30)

    label_quantity = tk.Label(create_item_window, text="Quantity:", fg="blue")
    entry_quantity = tk.Entry(create_item_window, fg="blue", width=30)

    # Create entry widgets for first and last name
    label_first_name = tk.Label(create_item_window, text="First Name:", fg="blue")
    entry_first_name = tk.Entry(create_item_window, fg="blue", width=30)
    
    label_last_name = tk.Label(create_item_window, text="Last Name:", fg="blue")
    entry_last_name = tk.Entry(create_item_window, fg="blue", width=30)

    # Create entry widgets for phone number and email
    label_phone_number = tk.Label(create_item_window, text="Phone Number (xxx-xxx-xxxx):", fg="blue")
    entry_phone_number = tk.Entry(create_item_window, fg="blue", width=30)
    
    label_email = tk.Label(create_item_window, text="Email:", fg="blue")
    entry_email = tk.Entry(create_item_window, fg="blue", width=30)


    # Create a Submit button
    submit_button = tk.Button(create_item_window, text="Submit", command=lambda: add_item(entry_itemID.get(), entry_product.get(),entry_quantity.get(), entry_first_name.get(), entry_last_name.get(),entry_phone_number.get(),entry_email.get()))

    # Pack the widgets
    label_itemID.pack(pady=5)
    entry_itemID.pack(pady=5)

    label_product.pack(pady=5)
    entry_product.pack(pady=5)

    label_quantity.pack(pady=5)
    entry_quantity.pack(pady=5)

    label_first_name.pack(pady=5)
    entry_first_name.pack(pady=5)

    label_last_name.pack(pady=5)
    entry_last_name.pack(pady=5)

    label_phone_number.pack(pady=5)
    entry_phone_number.pack(pady=5)

    label_email.pack(pady=5)
    entry_email.pack(pady=5)

    submit_button.pack(pady=10)

# Function to handle finding an item
def find_item_window():

    """
    Open a window for finding details about a specific item in the storage system.

    Clears the text widget at the bottom.
    Creates a new top-level window titled "Find Item" with an entry widget for itemID and a submit button.
    The submit button triggers the `finding_item` function to search and display details for the specified item.

    Example:
    find_item_window()  # Opens a window for finding details about a specific item in the storage system.

    """

    #clear the text box at the bottom
    storage_text.delete(1.0, tk.END)

    # Create a Toplevel window for finding an item
    find_item_window = tk.Toplevel(window)
    find_item_window.title("Find Item")

    # Set the window size to 300x100
    find_item_window.geometry("300x100")

    # Create an itemID widget for finding
    label_itemID = tk.Label(find_item_window, text="ItemID:", fg="blue")
    entry_itemID = tk.Entry(find_item_window)
    label_itemID.pack()
    entry_itemID.pack()

    # Create a button to submit the item finding
    submit_button = tk.Button(find_item_window, text="Submit", command=lambda: finding_item(entry_itemID.get()))
    submit_button.pack()

    # Function to handle finding an item
def delete_items_window():

    """
    Open a window for deleting a specific item from the storage system.

    Clears the text widget at the bottom.
    Creates a new top-level window titled "Delete Item" with an entry widget for itemID and a submit button.
    The submit button triggers the `delete_items` function to remove the specified item from the storage system.

    Example:
    delete_items_window()  # Opens a window for deleting a specific item from the storage system.

    """

    #clear the text box at the bottom
    storage_text.delete(1.0, tk.END)

    # Create a Toplevel window for finding an item
    find_item_window = tk.Toplevel(window)
    find_item_window.title("Delete Item")

    # Set the window size to 300x100
    find_item_window.geometry("300x100")

    # Create an itemID widget for finding
    label_itemID = tk.Label(find_item_window, text="ItemID:", fg="blue")
    entry_itemID = tk.Entry(find_item_window)
    label_itemID.pack()
    entry_itemID.pack()

    # Create a button to submit the item finding
    submit_button = tk.Button(find_item_window, text="Submit", command=lambda: delete_items(entry_itemID.get()))
    submit_button.pack()

def main():
    global storage_text  # Declare storage_text as a global variable
    
    window = tk.Tk()
    # Set the window size to full screen
    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
    # Set the background color to light blue
    window.configure(bg="steel blue")



    # Increase the font size of the label text
    font_settings = ("Script MT Bold", 30)  # Font family: Helvetica, Font size: 16
    greeting = tk.Label(text="Storage Management", fg="white", bg="lightblue", width=20, height=3, font=font_settings,relief=tk.RIDGE,borderwidth=5, highlightthickness=2,)
    greeting.pack()

    # Load from ssv file button
    load_items_button = tk.Button(
        text="Load Previous Session",
        width=25,
        height=1,
        bg="navy",
        fg="white",
        font=("Script MT Bold", 13),
        relief=tk.RIDGE,
        borderwidth=5, 
        highlightthickness=2,
        command=read_csv
    )

    # Pack the button to the top
    load_items_button.pack(side=tk.TOP, pady=10)

    # Account creation button
    item_creation_button = tk.Button(
        text="Create Item",
        width=25,
        height=1,
        bg="navy",
        fg="white",
        font=("Script MT Bold", 13),
        relief=tk.RIDGE,
        borderwidth=5, 
        highlightthickness=2,
        command=open_create_item_window  # Set the command to open the Create Item window
    )

    # Pack the button to the top
    item_creation_button.pack(side=tk.TOP, pady=10)

    # Show storage button
    show_item_button = tk.Button(
        text="Show Storage",
        width=25,
        height=1,
        bg="navy",
        fg="white",
        font=("Script MT Bold", 13),
        relief=tk.RIDGE,
        borderwidth=5, 
        highlightthickness=2,
        command=show_items  # Set the command option to the show_items function
    )

    # Pack the button to the Left side
    show_item_button.pack(side=tk.TOP, pady=10)

    # Show storage button
    find_item_button = tk.Button(
        text="Find Item",
        width=25,
        height=1,
        bg="navy",
        fg="white",
        font=("Script MT Bold", 13),
        relief=tk.RIDGE,
        borderwidth=5, 
        highlightthickness=2,
        command=find_item_window
    )

    # Pack the button to the Left side
    find_item_button.pack(side=tk.TOP, pady=10)

    # Show storage button
    delete_item_button = tk.Button(
        text="Delete Item",
        width=25,
        height=1,
        bg="navy",
        fg="white",
        font=("Script MT Bold", 13),
        relief=tk.RIDGE,
        borderwidth=5, 
        highlightthickness=2,
        command=delete_items_window
    )

    # Pack the button to the Left side
    delete_item_button.pack(side=tk.TOP, pady=10)

    # Show storage button
    recent_item_button = tk.Button(
        text="Most Recent Products",
        width=25,
        height=1,
        bg="navy",
        fg="white",
        font=("Script MT Bold", 13),
        relief=tk.RIDGE,
        borderwidth=5, 
        highlightthickness=2,
        command=most_recent_items
    )

    # Pack the button to the Left side
    recent_item_button.pack(side=tk.TOP, pady=10)


    # save current session
    save_session_button = tk.Button(
        text="Save Current Session",
        width=25,
        height=1,
        bg="navy",
        fg="white",
        font=("Script MT Bold", 13),
        relief=tk.RIDGE,
        borderwidth=5, 
        highlightthickness=2,
        command=write_csv
    )

    # Pack the button to the Left side
    save_session_button.pack(side=tk.TOP, pady=10)



    # Text widget to display storage
    storage_text = tk.Text(window, height=10, width=60)
    storage_text.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
