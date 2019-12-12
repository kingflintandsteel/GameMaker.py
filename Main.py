from Screen import ScreenMain as sm
from Keyboard import KeyboardMain as km
from Widgets import Button, AnimatedCanvas, Entity
from images import ImageManager


main_screen = sm.start_screen(700, 700)
animation = AnimatedCanvas.AnimatedCanvas(main_screen, ImageManager.grab_frames("walking.gif", 24), 50, 0, 0)
entity_test = Entity.Entity(10, 150, 0, animation)


def function3():
    entity_test.start_animation()


def function4():
    entity_test.stop_animation()


def movement(event):
    if event.keycode == 32:
        entity_test.stop_animation()
    if event.keycode == 39:
        entity_test.move_right()
    elif event.keycode == 38:
        entity_test.move_up()
    elif event.keycode == 37:
        entity_test.move_left()
    elif event.keycode == 40:
        entity_test.move_down()


main_keyboard = km.start_keyboard(main_screen)
button = Button.Button("Start Animation", 100, 50, function3, main_screen, main_keyboard)
main_screen.place_widget(25, 100, button)
button = Button.Button("Stop Animation", 100, 50, function4, main_screen, main_keyboard)
main_screen.place_widget(575, 100, button)
main_keyboard.add_bind("<KeyPress>", movement)
main_screen.after(0, entity_test.start_animation())

if __name__ == '__main__':
    main_screen.mainloop()
