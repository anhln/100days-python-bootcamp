import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text = "I Am a Label")
my_label.pack()

my_label["text"] = "New text"

def button_click():
    print("I got clicked")
    my_label["text"] = input.get()

button = tkinter.Button(text="Click Me", command=button_click)
button.pack()

#Entry
input = tkinter.Entry()
input.pack()


window.mainloop()