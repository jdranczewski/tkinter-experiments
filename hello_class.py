from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit, cursor='X_cursor'
            )
        self.button.pack(side=LEFT)
        self.hi_there = Button(
            frame, text="HELLO", command=self.say_hi
            )
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("Hello, World!")

root = Tk()
all = App(root)

root.mainloop()
