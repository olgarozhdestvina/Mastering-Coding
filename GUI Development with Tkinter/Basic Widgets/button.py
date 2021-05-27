from tkinter import *
from tkinter import ttk
import os

# Create a clickable button
root = Tk()
button = ttk.Button(root, text='Press me')
button.pack()

# Add a function on-click
def callback():
    print('Pressed!')

button.config(command=callback)

# Simulate button click
button.invoke()

# Disable the button
button.state(['disabled'])
# check if it is in the disabled state
print('Disabled -> ', button.instate(['disabled']))

# Enable the button
button.state(['!disabled'])
# check if it is in the enabled state
print('Enabled -> ', button.instate(['!disabled']))

# Add an image to the button
logo_path = os.getcwd() + '\\Basic Widgets\\python_logo.gif'
logo = PhotoImage(
    file=logo_path)
button.config(image=logo, compound='left')

# Resize the image
small_logo = logo.subsample(5, 5)
button.config(image=small_logo)

root.mainloop()
