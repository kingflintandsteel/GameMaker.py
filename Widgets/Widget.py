import tkinter as tk


class Widget(tk.Frame):
    def __init__(self):
        pass

    def set_parent(self, parent):
        tk.Frame.__init__(self, parent)
