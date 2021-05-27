from tkinter import *
from tkinter import ttk

# Most of the below commands only work in the shell

# Create a clickable button
root = Tk()

entry = ttk.Entry(root, width=30)
entry.pack()
print(entry.get())

# Insert text
entry.insert(0, 'Enter your password')
print(entry.get())

# Delete the first char
entry.delete(0, 1)
print(entry.get())

# Delete everything
entry.delete(0, END)
print(entry.get())

# Display content with * sign
entry.config(show='*')

# Entry states
entry.state(['disabled'])
entry.state(['!disabled'])
entry.state(['readonly'])

root.mainloop()
