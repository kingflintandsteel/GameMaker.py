import tkinter as tk


class AnimatedCanvas(tk.Frame):
    def __init__(self, parent, gif_frames, time, x, y):
        self.holder = tk.Frame.__init__(self, parent)
        self.parent = parent
        self.frames = gif_frames
        self.frames_iterator = iter(self.frames)
        self.current_frame = next(self.frames_iterator)
        self.label = tk.Label(self, image=self.current_frame)
        self.label.pack()
        self.time = time
        self.animated = False
        self.x = x
        self.y = y

    def start_animation(self):
        if not self.animated:
            self.animated = True
            self.update_animation_internal()

    def stop_animation(self):
        self.animated = False
        self.update_animation_internal()

    def update_animation(self, flipper):
        if flipper is False:
            return
        self.current_frame = next(self.frames_iterator, "loop")
        if self.current_frame == "loop":
            self.frames_iterator = iter(self.frames)
            self.current_frame = next(self.frames_iterator)
        self.label.configure(image=self.current_frame)
        self.after(self.time, self.update_animation, self.animated)

    def update_animation_internal(self):
        self.update_animation(self.animated)

    def set_x(self, x):
        self.x = x
        self.place(x=self.x, y=self.y)

    def set_y(self, y):
        self.y = y
        self.place(x=self.x, y=self.y)
