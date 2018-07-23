from tkinter import *

def callback():
    print("Called the callback!")


class StatusBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill='x')

    def set(self, format, *args):
        self.label.config(text=format.format(*args))
        self.label.update_idletasks()


root = Tk()

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Close", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

toolbar = Frame(root)
b = Button(toolbar, text="new", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill='x')

status = StatusBar(root)
status.pack(side=BOTTOM, fill='x')
status.set("{}; {}", "string1", "string2")

root.mainloop()
