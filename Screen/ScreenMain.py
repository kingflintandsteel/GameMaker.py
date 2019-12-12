import tkinter as tk


class MainScreen(tk.Tk):
    def __init__(self, title, width=200, height=200, fullscreen=False):
        super().__init__()
        self.winfo_toplevel().title(title)
        self.w = width
        self.h = height
        self.fullscreen = fullscreen
        self.maxh = self.h
        self.maxw = self.w
        if fullscreen:
            self.overrideredirect(True)
            self.maxh = self.winfo_screenheight()
            self.maxw = self.winfo_screenwidth()
            self.geometry('%dx%d+0+0' % (self.maxw, self.maxh))
        self.set_min_size(self.w, self.h)
        self.set_max_size(self.maxw, self.maxh)
        self.holder = tk.Frame(self, width=self.w, height=self.h)
        self.holder.bind("<Enter>", self.set_focus)
        self.holder.pack(fill="both", expand=1)
        self.holder.lift()

    def set_min_size(self, width, height):
        self.w = width
        self.h = height
        self.minsize(width=width, height=height)

    def set_max_size(self, width, height):
        self.maxw = width
        self.maxh = height
        self.maxsize(width=self.maxw, height=self.maxh)

    def set_focus(self, event):
        self.holder.focus_set()

    def place_widget(self, x, y, widget):
        widget.place(x=x, y=y)


def start_screen(width, height):
    main = MainScreen("Hello World", width=width, height=height)
    return main
