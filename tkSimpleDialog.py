from tkinter import *

class Dialog(Toplevel):
    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent)
        # Make the window not show up in the window manager
        self.transient(parent)
        # Set the title
        if title:
            self.title(title)
        self.parent = parent
        # Initiate self.result just in case
        self.result = None
        # Create the main frame to put elements into
        body = Frame(self)
        # Create the elements and get the initial focus element
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        # Create the buttons
        self.buttonbox()
        # Make the dialog modal
        self.grab_set()
        # Set the initial focus depending on whether self.body() returned sth
        if not self.initial_focus:
            self.initial_focus = self
        self.initial_focus.focus_set()
        # If dialog is closed, call cancel
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        # Position the window close to parent
        self.geometry("+{}+{}".format(parent.winfo_rootx()+50, parent.winfo_rooty()+50))
        # Make the main window wait
        self.wait_window(self)

    # Override to create body
    def body(self, master):
        pass

    # Create the buttons
    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()
            return
        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()

    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    # Override to validate
    def validate(self):
        return 1

    def apply(self):
        pass
