from tkinter import *
import tkSimpleDialog
from tkinter import messagebox


class MyDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        Label(master, text="First:").grid(row=0)
        Label(master, text="Second:").grid(row=1)
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.var = IntVar()
        self.cb = Checkbutton(master, text="Hardercopy", variable=self.var)
        self.cb.grid(row=2, columnspan=2, sticky=W)
        return self.e1

    def validate(self):
        try:
            first = int(self.e1.get())
            second = int(self.e2.get())
            return 1
        except ValueError:
            messagebox.showerror("Error", "Both values need to be integers!")
            return 0

    def apply(self):
        self.result = (self.e1.get(), self.e2.get(), self.var.get())


def showMyDialog(parent):
    d = MyDialog(root)
    print(d.result)
    return d.result


root = Tk()

Button(root, text="MyDialog", command=lambda: showMyDialog(root)).pack()
root.mainloop()
