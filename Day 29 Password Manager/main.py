from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    password_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website=website_entry.get()

    try:
        with open ("data.json",mode="r") as data_file:
             database=json.load(data_file)
             
    except FileNotFoundError:
        no_data_file=messagebox.showerror(title="Error", message="No Data File Found")

    else:
        if website.lower() in database:
            email=database[website]['email']
            password=database[website]['password']
            data_found=messagebox.showinfo(title=website.title(), message=f"E-mail: {email}\nPassword: {password}")  
        else:
            no_data_found=messagebox.showerror(title=website.title(), message=f"No details for {website} exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website=website_entry.get()
    email_username=email_username_entry.get()
    password=password_entry.get()
    new_data={
        website.lower():{
            "email": email_username,
            "password": password
        }}

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        empty_entry=messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("data.json",mode="r") as data_file:
                data= json.load(data_file)
        except FileNotFoundError:
            with open("data.json",mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)   
        else:
            data.update(new_data)

            with open("data.json",mode="w") as data_file:
                        json.dump(data, data_file, indent=4)    
        finally:              
            website_entry.delete(0, END)
            password_entry.delete(0, END)  

# ---------------------------- UI SETUP ------------------------------- #

windows= Tk()
windows.title("Password Manager")
windows.config(padx=50,pady=50)

canvas= Canvas(width=200, height=200,)
bg_image= PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1,row=0)

# ----- Labels ----- #

website_lable=Label(text="Website:")
website_lable.grid(column=0,row=1)

email_username_lable=Label(text="Email/Username:")
email_username_lable.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

# ----- Entries ----- #

website_entry= Entry(width=34)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_username_entry= Entry(width=53)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(0, "name@mail.com")

password_entry= Entry(width=34)
password_entry.grid(column=1,row=3)

# ----- Buttons ----- #

generate_button=Button(text="Generate Password", command=generate_password)
generate_button.config(width=14)
generate_button.grid(column=2, row=3)

add_button=Button(text="Add", width=45, command= save)
add_button.grid(column=1, row=4, columnspan=2)

search_button=Button(text="Search", command=find_password)
search_button.config(width=14)
search_button.grid(column=2, row=1)

windows.mainloop()
