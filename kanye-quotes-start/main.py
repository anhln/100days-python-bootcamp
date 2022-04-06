from tkinter import *
import requests
from PIL import ImageTk, Image


URL_KANYE_API = "https://api.kanye.rest/"

def get_quote():
    res = requests.get(URL_KANYE_API)
    if res.status_code == 200:
        quote = res.json()["quote"]
        canvas.itemconfig(quote_text, text=quote)
    else:
        raise Exception("Can not get any quote!")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = ImageTk.PhotoImage(Image.open("background.png"))
# background_img = PhotoImage(file="background.jpg")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = ImageTk.PhotoImage(Image.open("kanye.png"))
# kanye_img = PhotoImage(file="kanye.jpg")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()