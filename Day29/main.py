from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    if website == "" or email == "" or password == "":
        messagebox.showinfo("Don't leave field empty")
    else :
        is_ok = messagebox.askokcancel("ok")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()
            input_password.delete(0, END)
            input_website.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
import PIL
from PIL import ImageTk
import convert_png_to_rgb
# convert_png_to_rgb.convert("logo.png", "logo.jpg", "#ffffff")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
im = PIL.Image.open("logo.jpg")
img = PIL.ImageTk.PhotoImage(im)
canvas.create_image(0,0, anchor=NW, image=img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)
input_email = Entry(width=35)
input_email.insert(0, "anhlnster@gmail.com")
input_email.grid(column=1, row=2, columnspan=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
input_password = Entry(width=21)
input_password.grid(column=1, row=3)
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)


add_button = Button(text="Add",width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()