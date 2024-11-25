from tkinter import * # classes and constants
from tkinter import messagebox # method so not included with the * import
from random import choice, shuffle, randint
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # password_list = []

    choice_letter = [choice(letters) for char in range(randint(8, 10))]
    choice_symbol = [choice(symbols) for char in range(randint(2, 4))]
    choice_number = [choice(numbers) for char in range(randint(2, 4))]

    # Also do this,Angela solution
    # choice_letter = [random.choice(letters) for char in range(nr_letters)]
    # choice_symbol = [random.choice(symbols) for char in range(nr_symbols)]
    # choice_number = [random.choice(numbers) for char in range(nr_numbers)]
    #

    password_list = choice_symbol + choice_number + choice_letter

    # list comprehension above has replaced these for loops
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    shuffle(password_list)

    # this replaces the below for loop
    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    #print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password

        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Are you sure?", message="Please don't leave fields empty!")
    else:
        try:
            with open("data.json.old", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json.old", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json.old", "w") as data_file:
                # updating old data with new data
                data.update(new_data)
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Are you sure?", message="Enter website to search for")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        else:
            if website in data:
                password = data[website]["password"]
                messagebox.showinfo(title="Website Entry", message=f"website:{website}\n"
                                                                   f"password:{password}")
            else:
                messagebox.showinfo(title="Sorry", message="No details for the website exist")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
# x and y for image. half of canvas size if need to be in the middle
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:", font=FONT_NAME)
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", font=FONT_NAME)
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT_NAME)
password_label.grid(column=0, row=3)

# entries
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "dan@gmail.com")
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=13 , command=find_password)
search_button.grid(column=2, row=1)




window.mainloop()