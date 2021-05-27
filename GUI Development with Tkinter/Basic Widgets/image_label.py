from tkinter import *
from tkinter import ttk
import os


root = Tk()
logo_path = os.getcwd() + '\\Basic Widgets\\python_logo.gif'
label = ttk.Label(root, text='Python')
label.pack()

# Displaying image along with text
label.config(background='blue', foreground='yellow')
label.config(font=('Courier', 15, 'bold italic'))
logo = PhotoImage(
    file=logo_path)
label.config(image=logo)
label.config(compound='left')

# Storing logo
label.img = logo
label.config(image=label.img)

root.mainloop()
