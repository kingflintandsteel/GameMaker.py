class MainKeyboard:
    def __init__(self, window):
        self.window = window
        self.mouse_clicks = []
        self.window.bind_all("<Button-1>", self.check_clicks)
        self.window.holder.pack()

    def add_bind(self, event, bind_function):
        if "Button" in event:
            self.add_mouse_listener(bind_function)
        else:
            self.window.bind_all(event, bind_function)

    def add_mouse_listener(self, bind_function):
        self.mouse_clicks.append(bind_function)

    def check_clicks(self, event):
        for bind_function in self.mouse_clicks:
            bind_function(event)


def start_keyboard(window):
    keyboard = MainKeyboard(window)
    return keyboard
