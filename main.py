from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500,300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial",20,"bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)
def clicked():
    my_label.config(text=input.get())

# Button
my_button = Button(text="Click Me", command=clicked)
my_button.grid(column=1, row=1)

# New Button
my_button2 = Button(text="Click Me",command=clicked)
my_button2.grid(column=2, row=0)

# Entry
input = Entry(width=15)
print(input.get())
input.grid(column=3,row=2)

window.mainloop()
