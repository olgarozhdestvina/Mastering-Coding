from tkinter import *
from tkinter import ttk

root = Tk()

# Check button
checkbutton = ttk.Checkbutton(root, text='SPAM?')
checkbutton.pack()

# Create a tkinter string variable
spam = StringVar()
spam.set('SPAM!!!')
print(spam.get())  # revoke the text

checkbutton.config(variable=spam, onvalue='SPAM please', offvalue='Booo SPAM')

# Radio button
breakfast = StringVar()
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value='Eggs').pack()
ttk.Radiobutton(root, text='Toast', variable=breakfast, value='Toast').pack()
ttk.Radiobutton(root, text='Coffee', variable=breakfast, value='Coffee').pack()
ttk.Radiobutton(root, text='Porridge', variable=breakfast,
                value='Porridge').pack()

# Change the text displayed for the check button
# depending on the selected radio button
checkbutton.config(textvariable=breakfast)

root.mainloop()
print(breakfast.get())
print(spam.get())
