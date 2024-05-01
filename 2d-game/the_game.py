import time
import pyglet
from pyglet import shapes
from DIPPID import SensorUDP
from PIL import Image
import os

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)
WINDOW_WIDTH = 593
WINDOW_HEIGHT = 480
GOAL_AREA = (255,255,255)
OUT_AREA = (0,0,0)
SENSOR_SENSITIVITY = 8 #can be changed to change difficulty something around 5-15 is usable
START_X = 10
START_Y = 10
PLAYER_SIZE = 10
global_string = "rules.png"


#still learning python and didnt know how to have mutable variables, chatgpt gave me this
def change_global_string(new_value):
    global global_string
    global_string = new_value

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
square = shapes.Rectangle(x=START_X, y=START_Y, width=PLAYER_SIZE, height=PLAYER_SIZE, color=(255, 0, 0))
square.anchor_x = PLAYER_SIZE//2
square.anchor_y = PLAYER_SIZE//2


def load_background(img):
    background = pyglet.image.load(img)
    background = pyglet.sprite.Sprite(background)
    background.draw()

#chatgpt for how to get pixel coordinates, this checks what color the player is on,
# if its black he is lost, if its white he won, this mean maps can easily/quickly be drawn in paint
def get_pixel_value(image_path, x, y):
    image = Image.open(image_path)
    flipp_y = WINDOW_HEIGHT-y-1
    pixel_value = image.getpixel((x, flipp_y))
    if pixel_value == GOAL_AREA:
        change_global_string("win.png")
        square.x = START_X
        square.y = START_Y
    elif pixel_value == OUT_AREA:
        change_global_string("lose.png")
        square.x = START_X
        square.y = START_Y

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        os._exit(0)
    if symbol == pyglet.window.key.X:
        change_global_string("level1.jpg")
    if symbol == pyglet.window.key.C:
        change_global_string("level2.jpg")
    if symbol == pyglet.window.key.V:
        change_global_string("level3.jpg")
    if symbol == pyglet.window.key.B:
        change_global_string("level4.jpg")#its actually  not impossible :)
    if symbol == pyglet.window.key.R:
        change_global_string("rules.png")

#stops player from going out of bounds
def check_border():
    if square.y < 0: square.y += 5
    if square.y > WINDOW_HEIGHT: square.y -= 5
    if square.x < 0: square.x += 5
    if square.x > WINDOW_WIDTH: square.x -= 5



@window.event
def on_draw():
    window.clear()
    load_background(global_string)
    # I know its ugly D: checks if we have data and some level is running to get move square/start game
    if sensor.has_capability('accelerometer')and global_string!="rules.png" and global_string!="win.png" and global_string!="lose.png":
        square.x -= SENSOR_SENSITIVITY*float(sensor.get_value('accelerometer')['x'])
        square.y -= SENSOR_SENSITIVITY*float(sensor.get_value('accelerometer')['y'])
        check_border()
        get_pixel_value(global_string, square.x, square.y)
    square.draw()




pyglet.app.run()