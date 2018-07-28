import tkinter as Tk


from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2TkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

# Create the root window
root = Tk.Tk()
root.wm_title("Embedding in Tk")

# Create a frame for the graph and the toolbar
t_frame = Tk.Frame(root, width=100, height=100)

# Create the figure
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# Make the figure into a canvas...
canvas = FigureCanvasTkAgg(fig, master=t_frame)  # A tk.DrawingArea.
canvas.draw()
# And pack the canvas
# canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
# canvas.get_tk_widget().pack(side=Tk.TOP)


# Add a toolbar
toolbar = NavigationToolbar2TkAgg(canvas, t_frame)
toolbar.update()
# canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas._tkcanvas.pack(side=Tk.BOTTOM)
canvas.get_tk_widget().pack(side=Tk.TOP)

t_frame.pack()



def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = Tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=Tk.TOP)

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
