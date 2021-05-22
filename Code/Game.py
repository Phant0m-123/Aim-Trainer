import asyncio
import random
import threading

import arcade
import keyboard

s_width = 1280
s_height = 720
s_title = "Aim Trainer"


cursorx = 0
cursory = 0
targetX = random.randint(250, 1616 - 10)
targetY = random.randint(10, 1080 - 74)
target = arcade.Sprite("../Assets/obj.png", center_x= targetX, center_y=targetY)
cursor = arcade.Sprite("../Assets/cursor.png", center_x= 100, center_y=100)
#collide = arcade.check_for_collision()


def draw_objects():
    target.draw()
    cursor.draw()


class gam(arcade.Window):
    def __init__(self, s_width, s_height, s_title):
        super().__init__(s_width, s_height, s_title, fullscreen=True, resizable=False, update_rate=1 / 165,
                         antialiasing=False,visible=True)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)
        self.clicked = False

    def on_draw(self):
        arcade.start_render()
        draw_objects()
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        cursor.center_x = x
        cursor.center_y = y
    def on_update(self, delta_time: float):
        global target, targetY,targetX
        global cursor
        target.update()
        cursor.update()
        collide = arcade.check_for_collision(target,cursor)
        if collide == True and self.clicked == True:
            target.center_y = random.randint(16, 1080 - 74)
            target.center_x = random.randint(266, 1616 - 10)
            self.clicked = False
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.Z or symbol == arcade.key.X:
            self.clicked = True


gam(s_width, s_height, s_title)
arcade.run()
