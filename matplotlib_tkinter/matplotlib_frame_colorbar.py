# An example showing how to use the GraphFrame class
import tkinter as Tk
import matplotlib_frame
from scipy import sin, cos, mgrid

# Create the root window
root = Tk.Tk()

# Create a GraphFrame and pack it inside of root
gf = matplotlib_frame.GraphFrame(root, show_toolbar=True)
gf.pack(side=Tk.TOP, fill=Tk.BOTH)

# Plot a functions
N = 37
x, y = mgrid[:N, :N]
Z = (cos(x*0.2) + sin(y*0.3))
imshow = gf.subplot.imshow(Z, cmap='Blues', interpolation='none')
gf.fig.colorbar(imshow, ax=gf.subplot, use_gridspec=False)

# Start the mainloop
root.mainloop()
