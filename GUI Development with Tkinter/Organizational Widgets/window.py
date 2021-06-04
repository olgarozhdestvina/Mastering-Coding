from tkinter import *

root = Tk()

# Add another window
window = Toplevel(root)
window.title('Another window')

# Position
window.lower()
# Place the window right above the root
window.lift(root)

# State
window.state('zoomed')  # fit the screen
window.state('withdrawn')  # hide the window
window.state('iconic')  # add an icon to the taskbar
window.state('normal')  # change from iconic
print(window.state())
window.state('normal')  # change from zoomed
print(window.state())

# Moving to and from the taskbar
window.iconify()
window.deiconify()

# Geometry
window.geometry('666x444+50+200')  # widthxheight+x+y
# if the window is resizable in x and y directions
window.resizable(False, False)
# limit resize
window.resizable(True, True)
window.maxsize(666, 444)
window.minsize(66, 44)

# Destroy the window
window.destroy()

root.mainloop()
