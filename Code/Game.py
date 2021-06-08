import asyncio
import random
import time
import arcade
from PIL import Image


s_width, s_height = arcade.window_commands.get_display_size()
s_title = "Aim Trainer"


"""image = Image.open("../Assets/quit_screen.png")
img_final = image.resize((s_width,s_height))
img_final.save('quitscreen.png')"""
cursorx = 0
cursory = 0
targetX = int(random.randint((s_width/4)-26,(s_width/4)*3+26))
targetY = int(random.randint(26,s_height-26))
target = arcade.Sprite("../Assets/obj.png", center_x= targetX, center_y=targetY)
cursor = arcade.Sprite("../Assets/cursor.png", center_x= 100, center_y=100)
quit_button = arcade.Sprite("../Assets/quit.png", center_x=(s_width/8)*7.5, center_y=s_height-50)
quit_press = False
score = 0
hitsound = arcade.load_sound("../Assets/hit.mp3")
goodbye = arcade.load_sound("../Assets/goodbye.mp3",True)
#bye = arcade.Sprite("../Assets/quit_screen.png",center_x=(s_width/2),center_y=(s_height/2))


def draw_objects():
    quit_button.draw()
    arcade.draw_text(f"Score = {score}",10,s_height-76,arcade.color.RED_ORANGE,38)
    arcade.draw_rectangle_outline((s_width/2),(s_height/2),((s_width/4)*3),s_height,arcade.color.RED_ORANGE,10)
    target.draw()
    cursor.draw()
#async def bye(a):
    #if a == True:
        #bye.draw()

class gam(arcade.Window):
    def __init__(self, s_width, s_height, s_title):
        super().__init__(s_width, s_height, s_title, fullscreen=True, resizable=False, update_rate=1 / 165,
                         antialiasing=True,visible=True)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)
        self.clicked = False
        #self.draw = False

    def on_draw(self):
        arcade.start_render()
        draw_objects()
        #asyncio.run(bye(self.draw))
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        cursor.center_x = x
        cursor.center_y = y
    def on_update(self, delta_time: float):
        global target, targetY,targetX
        global cursor, score, quit_press, quit_button, bye
        target.update()
        cursor.update()
        collide = arcade.check_for_collision(target,cursor)
        if collide == True and self.clicked == True:
            hitsound.play()
            target.center_y = random.randint(26,s_height-26)
            target.center_x = random.randint((s_width/4)-26,(s_width/4)*3+26)
            self.clicked = False
            score+=1
        self.quit = arcade.check_for_collision(quit_button,cursor)
        if self.quit == True and quit_press == True:
            arcade.close_window()
            goodbye.play()
            time.sleep(4.75)
            exit()
    def on_key_release(self, symbol, modifiers):
        collide = arcade.check_for_collision(target,cursor)
        if collide == True:
            if symbol == arcade.key.Z or symbol == arcade.key.X :
                self.clicked = True
    def on_mouse_press(self, x: float, y: float, button, modifiers: int):
        global quit_press, quit_button
        self.quit = arcade.check_for_collision(quit_button, cursor)
        if self.quit == True:
            if button == arcade.MOUSE_BUTTON_LEFT:
                quit_press = True
    #def set_minimum_size(self, width: 1280, height: 720):


gam(s_width, s_height, s_title)
arcade.run()
