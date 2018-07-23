from tkinter import *
from tkinter import messagebox

root = Tk()

b = Button(root, text="showinfo", command=lambda:
    messagebox.showinfo("Info", "This box contains information!"))
b.pack()
b = Button(root, text="showwarning", command=lambda:
    messagebox.showwarning("Warning", "This box contains a warning!"))
b.pack()
b = Button(root, text="showerror", command=lambda:
    messagebox.showerror("Error", "This box contains an error!"))
b.pack()
b = Button(root, text="askquestion", command=lambda:
    print(messagebox.askquestion("Question", "This box asks a question!")))
b.pack()
b = Button(root, text="askokcancel", command=lambda:
    print(messagebox.askokcancel("Question", "This box asks a question!")))
b.pack()
b = Button(root, text="askyesno", command=lambda:
    print(messagebox.askyesno("Question", "This box asks a question!")))
b.pack()
b = Button(root, text="askyesnocancel", command=lambda:
    print(messagebox.askyesnocancel("Question", "This box asks a question!")))
b.pack()
# You get the idea

root.mainloop()
