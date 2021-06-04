from tkinter import *
from tkinter import ttk


root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()

# Add Tabs to the notebook
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text='One')
notebook.add(frame2, text='Two')

# Add a button to the first tab
ttk.Button(frame1, text='Click me').pack()

# Insert a new tab
frame3 = ttk.Frame(notebook)
notebook.insert(0, frame3, text='Now I am One')

# Remove the last tab
notebook.forget(0)

# Add the removed tab again
notebook.add(frame3, text='Guess who is back')

# Check the position of selected tab
print(notebook.select())
print(notebook.index(notebook.select()))

# Select a tab
notebook.select(2)
print(notebook.index(notebook.select()))

# Tab state
notebook.tab(0, state='disabled')
notebook.tab(1, state='hidden')
notebook.tab(1, state='normal')

# Check tab properties
print(notebook.tab(2, 'text'))
print(notebook.tab(1))

root.mainloop()
