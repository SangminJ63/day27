from tkinter import *

window = Tk()
window.title("Mile to Kilometer")
window.minsize(250, 100)
window.config(padx=20, pady=20)

FONT = ("Verdana", 10, "bold")

# Input
my_input = Entry(width=10)
my_input.grid(column=1, row=0)

# Label
label1 = Label(text="is equal to", font=FONT)
label1.grid(column=0, row=1)

label2 = Label(text="Miles", font=FONT)
label2.grid(column=2, row=0)

label3 = Label(text="Km", font=FONT)
label3.grid(column=2, row=1)


def converter():
    converted = round(float(float(my_input.get()) * 1.609), 2)
    label4 = Label(text=str(converted), font=FONT)
    label4.grid(column=1, row=1)


# Button
my_button = Button(text="Calculate", command=converter)
my_button.grid(column=1, row=2)

window.mainloop()
