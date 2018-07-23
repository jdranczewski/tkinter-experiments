from tkinter import *
from tkinter import messagebox


def callback(event):
    frame.focus_set()
    print("Clicked at", event.x, event.y)


def key(event):
    print("Pressed", repr(event.char), event.keysym)

def close_window():
    if messagebox.askokcancel("Quit", "Do you actually want to quit?"):
        root.destroy()


root = Tk()
root.protocol("WM_DELETE_WINDOW", close_window)
frame = Frame(root, width=100, height=100)
# 1 for left, 2 for middle, 3 for right
frame.bind("<Button-1>", callback)
frame.bind("<Key>", key)
frame.pack()

root.mainloop()
