from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text='Hello, Tkinter')
label.pack()

# Change configurations
label.config(
    text="Hello everyone! It's been a while since we last met. Great to see you again!")
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground='blue', background='yellow')
label.config(font=('Courier', 18, 'italic'))

root.mainloop()
