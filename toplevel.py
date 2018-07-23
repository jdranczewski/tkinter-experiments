from tkinter import *

root = Tk()
w_one = Label(root, text="Main")
w_one.pack()

top = Toplevel()
w_two = Label(top, text="Toplevel")
w_two.pack()

root.mainloop()
