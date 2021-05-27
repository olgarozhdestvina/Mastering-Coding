from tkinter import *
from tkinter import ttk

root = Tk()

progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar.pack()

# Operation is in progress (in indeterminate mode)
progressbar.config(mode='indeterminate')
progressbar.start()
progressbar.stop()

# (in determinate mode)
progressbar.config(mode='determinate', maximum=11.0, value=6.5)
progressbar.config(value=10.2)

# Increase the progressbar by 1
# when it exceeds the max, it wraps around
progressbar.step()


# Adding a scale for progressbar
scale_value = DoubleVar()
progressbar.config(variable=scale_value)
scale = ttk.Scale(root, orient=HORIZONTAL, length=400,
                  variable=scale_value, from_=0.0, to=11.0)
scale.pack()
scale.set(2.9)

root.mainloop()
print(scale_value.get())
