import json
from tkinter import *
from tkinter import messagebox
import random
alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
           'P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d',
           'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
           't','u','v','w','x','y','z']
symbol_list = ['@','#','$','%','^','&','*','(',')','!']
password_list = []

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    global password_list
    password_list = []
    password_letters = [random.choice(alphabets) for _ in range(5)]
    password_numbers = [random.randint(0,9) for _ in range(5)]
    password_symbols = [random.choice(symbol_list) for _ in range(5)]
    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    password_str = ""
    for char in password_list:
        password_str += str(char)
    input_password.insert(0, password_str)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
   is_ok = messagebox.askokcancel(web_name.get(),message=f"These are detail you entered:"
                                                  f" \n Email:{email_name.get()}: \n Password:{password.get()}")
   new_data = {
       web_name.get():{
       "Email":email_name.get(),
        "Password":password.get()
        }
   }
   if is_ok:
       try:
           with open("my_passwords.json", 'r') as f:
               data = json.load(f)
       except FileNotFoundError:
           with open("my_passwords.json", "w") as file:
               json.dump(new_data, file, indent=4)
       else:
           data.update(new_data)
           with open("my_passwords.json", "w") as file:
               json.dump(data, file, indent=4)
       finally:
           input_web.delete(0, len(web_name.get()))
           input_password.delete(0, len(password.get()))
def search():
    website=input_web.get()
    is_found=False
    with open("my_passwords.json","r") as file:
        data=json.load(file)
        for item in data:
            if item==website:
                is_found=True
                break
        if is_found:
            messagebox.showinfo(website,f"Email: {data[item]['Email']}\nPassword: {data[item]['Password']}")
        else:
            messagebox.showerror("search error","This website data is not in our database")
# ---------------------------- UI SETUP ------------------------------- #

# ---------------------------------setup window---------------------------------------


window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70, bg="white")

# --------------------------------Logo image-----------------------------------


canvas = Canvas(width=190, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=2)

# ---------------------------------------labels---------------------------------------

website_label = Label(text="Website: ", bg="white", font="arial")
website_label.grid(row=3, column=1)

email_label = Label(text="Email/Username", bg="white", font="arial")
email_label.grid(row=4, column=1)

password_label = Label(text="Password", bg="white", font="arial")
password_label.grid(row=5, column=1)

# --------------------------Entries-------------------------------------------------


web_name = StringVar()
input_web = Entry(width=30, borderwidth=2, textvariable=web_name)
input_web.grid(column=2, row=3)
input_web.focus()

email_name = StringVar()
input_email = Entry(width=50, borderwidth=2, textvariable=email_name)
input_email.grid(column=2, row=4, columnspan=2)
input_email.insert(0,"abdul.qadeer4122@gmail.com")

password = StringVar()
input_password = Entry(width=30, borderwidth=2, textvariable=password)
input_password.grid(column=2, row=5)

# --------------------------------------Buttons-------------------------------------------------

search_button=Button(text="Search",bg="white",borderwidth=2,width=16,command=search)
search_button.grid(column=3,row=3)

generate_password_button = Button(text="Generate password", width=16, bg="white",command=password_generator)
generate_password_button.grid(column=3, row=5)

add_button = Button(text="Add", width=43, bg="white",command=save_password)
add_button.grid(column=2, row=6, columnspan=2)

window.mainloop()
