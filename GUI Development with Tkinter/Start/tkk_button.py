from tkinter import *
from tkinter import ttk

# Create a window and add a button to it
root = Tk()

button = ttk.Button(root, text='Click me')
button.pack()

# Button text property
print(button['text'])
button['text'] = 'Press me'
button.config(text='Push me')

# All button properties
print(button.config())

root.mainloop()

# Underlying Tk names for root and button
print(root)
print(button)
