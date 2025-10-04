from tkinter import *
FONT = "Bahnschrift"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,columnspan=2)

# Buttons
generate_password_button = Button(text="Generate Password", command=None)
generate_password_button.grid(row=3, column=2,columnspan=2)
add_button = Button(text="Add", width=36, command=None)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()