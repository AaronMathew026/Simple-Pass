from tkinter import *
from tkinter import messagebox
FONT = "Bahnschrift"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_save(event=None):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?"):
        format = f"{website}|{email}|{password}\n"
        
        if website == "" or password == "" or email == "":
            messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
            return
        
        with open(file = "saved_logins.txt",mode="a") as f:
            f.write(format)
        print(website, email, password)
    else:
        return
    website_entry.delete(0,END)
    password_entry.delete(0,END)
    email_entry.focus()
    messagebox.showinfo(title="Success", message="Login details saved successfully!")
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Simple Pass")
window.config(padx = 50,pady= 50)

canvas = Canvas(width = 200,height=200)#
logo_image = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = logo_image)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "aaronmathew026@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,columnspan=2)

# Buttons
generate_password_button = Button(text="Generate Password", command=None)
generate_password_button.grid(row=3, column=2,columnspan=2)
add_button = Button(text="Add", width=36, command=password_save)
add_button.grid(row=4, column=1, columnspan=2)

# Bind the Enter/Return key to save the password. This will call
# `password_save` when the user presses Enter anywhere in the main window.
window.bind('<Return>', password_save)


window.mainloop()