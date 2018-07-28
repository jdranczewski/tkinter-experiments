import tkinter as Tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2TkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class GraphFrame(Tk.Frame):
    def __init__(self, parent, figsize=(5, 4), dpi=100, bind_keys=False):
        Tk.Frame.__init__(self, parent)
        self.fig = Figure(figsize=figsize, dpi=dpi)
        self.subplot = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=1)
        if bind_keys:
            def on_key_press(event):
                key_press_handler(event, self.canvas, toolbar)
            self.canvas.mpl_connect("key_press_event", on_key_press)

    def draw(self):
        self.canvas.draw()
