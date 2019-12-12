import tkinter as tk


class Button(tk.Frame):
    def __init__(self, text, width, height, onclick, parent, keyboard):
        self.holder = tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.onclick = onclick
        self.width = width
        self.height = height
        self.create_button(text)
        self.canvas.bind("<Enter>", self.set_focus)
        self.canvas.pack()
        self.parent = parent
        self.keyboard = keyboard
        keyboard.add_bind("<Button-1>", self.call_onclick)

    def call_onclick(self, event):
        if event.widget == self.canvas:
            self.onclick()

    def create_button(self, text):
        self.canvas.create_rectangle(2, 2, self.width+1, self.height+1)
        self.canvas.create_text(2 + (self.width / 2), (self.height / 2), text=text, width=self.width)

    def set_focus(self, event):
        self.canvas.focus_set()
