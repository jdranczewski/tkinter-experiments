import tkinter as Tk
import matplotlib_frame
from scipy import sin, cos, linspace

# Create the root window
root = Tk.Tk()

# Create a GraphFrame and pack it inside of root
gf = matplotlib_frame.GraphFrame(root, show_toolbar=True)
gf.pack(side=Tk.TOP)

# Plot two functions
space = linspace(0, 10, 100)
gf.subplot.plot(space, cos(space))
line, = gf.subplot.plot(space, sin(space))

# Add a button for changing data
def change_data():
    line.set_data(space, cos(space))
    # Note that the canvas needs to be redrawn after a data change
    gf.draw()
b = Tk.Button(root, text="Change data", command=change_data)
b.pack()

# Start the mainloop
root.mainloop()
