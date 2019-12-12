from Widgets.AnimatedCanvas import AnimatedCanvas


class Entity(AnimatedCanvas):
    def __init__(self, movement_size, x, y, animation):
        self.holder = AnimatedCanvas.__init__(animation, animation.parent, animation.frames, animation.time, animation.x, animation.y)
        self.movement_size = movement_size
        self.x = x
        self.y = y
        self.animation = animation
        if animation is not None:
            animation.place(x=x, y=y)
            self.animation.set_y(y)
            self.animation.set_x(x)

    def start_animation(self):
        self.animation.start_animation()

    def stop_animation(self):
        self.animation.stop_animation()

    def change_movement_size(self, movement_size):
        self.movement_size = movement_size

    def change_animation(self, animation):
        self.animation = animation
        if animation is not None:
            animation.place(x=self.x, y=self.y)

    # the movement function will call on these to make things easier
    def move_right(self):
        self.x = self.x + self.movement_size
        self.animation.set_x(self.x)

    def move_left(self):
        self.x = self.x - self.movement_size
        self.animation.set_x(self.x)

    def move_up(self):
        self.y = self.y - self.movement_size
        self.animation.set_y(self.y)

    def move_down(self):
        self.y = self.y + self.movement_size
        self.animation.set_y(self.y)
