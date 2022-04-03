from tkinter import *

window = Tk()
window.title("Mile to Kilometer CONVERTER")
window.minsize(width=300, height=200)
window.config(padx=8, pady=8)


def calculate_click(e):
    mile = float(miles_input.get())
    km = round(mile * 1.609344, 2)
    result_label["text"] = str(km)


def calculate(e):
    mile = float(miles_input.get())
    km = round(mile * 1.609344, 2)
    result_label["text"] = str(km)


# GUI
miles_input = Entry()
miles_input.grid(column=1, row=0)
# Bind to calculate function


mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result_label = Label(text="")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_click)
calculate_button.grid(column=1, row=2)

window.bind("<Return>", calculate_click)
window.mainloop()
