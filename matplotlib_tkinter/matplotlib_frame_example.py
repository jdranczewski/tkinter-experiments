import tkinter as Tk
import matplotlib_frame
from scipy import sin, cos, linspace

root = Tk.Tk()

gf = matplotlib_frame.GraphFrame(root)
gf.pack(side=Tk.TOP)

space = linspace(0, 10, 100)
gf.subplot.plot(space, cos(space))
line, = gf.subplot.plot(space, sin(space))


def change_data():
    line.set_data(space, cos(space))
    gf.draw()


b = Tk.Button(root, text="Change data", command=change_data)
b.pack()

root.mainloop()
