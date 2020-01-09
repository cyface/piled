#!/home/pi/piled/.venv/bin/python
activate_this = '/home/pi/piled/.venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

import adafruit_matrixkeypad
import board
from digitalio import DigitalInOut
import time
from pygame import mixer
from time import sleep
from gpiozero import Button

# Big Red Button
button = Button(7)

# 3x4 matrix keypad
cols = [DigitalInOut(x) for x in (board.D10, board.D9, board.D11)]
rows = [DigitalInOut(x) for x in (board.D17, board.D2, board.D4, board.D3)]
keys = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ('*', 0, '#')
]
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

sound_dir = "/home/pi/piled/sounds/"
selected_sound = 1
sounds = {
    0: "Groovy.mp3",
    1: "Groovy.mp3",
    2: "Boomstick.mp3",
    3: "GetOut.mp3",
    4: "GoodGuys.mp3",
    5: "HailToTheKing.mp3",
    6: "ImWithIt.mp3",
    7: "OneMillionDollars.mp3",
    8: "ShopSmart.mp3",
    9: "laser.wav",
    '*': "Groovy.mp3",
    '#': "Groovy.mp3",
}

mixer.init()
mixer.music.load(sound_dir + sounds[selected_sound])
mixer.music.play(0)

try:
    while True:
        keys = keypad.pressed_keys
        if keys:
            selected_sound = keys[0]
            print("Key Pressed: ", keys)
        if button.is_pressed:
            print("Red Button Pressed")
            mixer.music.load(sound_dir + sounds[selected_sound])
            mixer.music.play(0)
            sleep(.25)  # wait and let the sound play

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Bye!")
