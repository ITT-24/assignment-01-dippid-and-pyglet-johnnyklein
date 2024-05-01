import random
import socket
import numpy as np
import time

IP = '192.168.178.104'
PORT = 5700

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#tried around for a while with accelormeter but somehow didnt get it running
def change_button_state(button_pressed):
    if button_pressed == 0:
        return 1
    else:
        return 0


while True:
    button_pressed = 0
    if (random.randrange(0, 10) < 3):
        button_pressed = change_button_state(button_pressed)
    message = '{"button_1" : ' + str(button_pressed) + '}'
    print(message)
    sock.sendto(message.encode(), (IP, PORT))
    time.sleep(1)
