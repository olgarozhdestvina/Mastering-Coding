from tkinter import *
from tkinter import ttk

root = Tk()
paned_widow = ttk.Panedwindow(root, orient=HORIZONTAL)
paned_widow.pack(fill=BOTH, expand=True)

# Add two frames to the paned window
frame1 = ttk.Frame(paned_widow, width=100, height=200, relief=RIDGE)
frame2 = ttk.Frame(paned_widow, width=400, height=66, relief=RIDGE)
paned_widow.add(frame1, weight=1)
paned_widow.add(frame2, weight=4)

# Insert the 3rd frame between frame1 and frame2
frame3 = ttk.Frame(paned_widow, width=55, height=400, relief=RIDGE)
# Not resizable since there is no weight
paned_widow.insert(1, frame3)

# Remove the frame at the position 1 (but it doesn't delete it, it still can be used)
paned_widow.forget(1)

root.mainloop()
