# The GraphFrame class implements a matplotlib graph in an easy to use way.
# It inherits from tkinter's Frame and thus behaves like any other widget,
# but it also exposes a single subplot (self.subplot) which can be used
# like any other subplot in normal matplotlib Python code. A convenient
# toolbar can also be attached to the graph.
# init arguments are the parent frame, the figure's size, its dpi, a boolean
# variable that allows for simple binding of matplotlib's default key bindings,
# and a boolean variable that determines whether to show a toolbar.

import tkinter as Tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2TkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class GraphFrame(Tk.Frame):
    def __init__(self, parent, figsize=(5, 4), dpi=100, bind_keys=False, show_toolbar=False):
        # Cal the init function of tkinter's Frame
        Tk.Frame.__init__(self, parent)
        # Create a matplotlib Figure
        self.fig = Figure(figsize=figsize, dpi=dpi)
        # Create a matplotlib subplot
        self.subplot = self.fig.add_subplot(111)
        # Create and draw a canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        # Add a toolbar if needed
        if show_toolbar:
            toolbar = NavigationToolbar2TkAgg(self.canvas, self)
            toolbar.update()
        # Pack the canvas in the Frame
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        # Bind keyboard shortcuts
        if bind_keys:
            def on_key_press(event):
                key_press_handler(event, self.canvas, toolbar)
            self.canvas.mpl_connect("key_press_event", on_key_press)

    # Redraw the canvas to show new data (if updated)
    def draw(self):
        self.canvas.draw()
