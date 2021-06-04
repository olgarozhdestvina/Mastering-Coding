from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)
frame.pack()

# Frame configs
frame.config(height=300, width=200)  # border is flat (no border by default)
# boarer = raised, sunken, solid, ridge, groove
frame.config(relief=SUNKEN)

# Add button to the frame
ttk.Button(frame, text='Click me').grid()
frame.config(padding=(40, 30))

# Add a labeled frame below
ttk.LabelFrame(root, height=100, width=300, text='My frame').pack()

root.mainloop()
