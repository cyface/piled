#!/home/pi/piled/.venv/bin/python
activate_this = '/home/pi/piled/.venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

import adafruit_matrixkeypad
import board
from digitalio import DigitalInOut
from gpiozero import Button
import neopixel_spi
from pygame import mixer
import sys
import time

# NeoPixel Strip
NUM_PIXELS = 8
spi = board.SPI()
pixels = neopixel_spi.NeoPixel_SPI(spi, NUM_PIXELS, brightness=0.05)

# Big Red Button
button = Button(24)

# 3x4 matrix keypad
cols = [DigitalInOut(x) for x in (board.D4, board.D3, board.D2)]
rows = [DigitalInOut(x) for x in (board.D23, board.D22, board.D27, board.D17)]
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


def pixel_loop():
    for curr_pixel in range(0, 8):
        pixels[curr_pixel] = (255, 0, 0)
        time.sleep(.025)
    for curr_pixel in range(7, -1, -1):
        pixels[curr_pixel] = (0, 255, 0)
        time.sleep(.025)
    pixels.fill(0)


try:
    pixel_loop()
    while True:
        keys = keypad.pressed_keys
        if keys:
            selected_sound = keys[0]
            print("Key Pressed: ", keys)
        if button.is_pressed:
            print("Red Button Pressed")
            mixer.music.load(sound_dir + sounds[selected_sound])
            mixer.music.play(0)
            time.sleep(.25)  # wait and let the sound play
            pixel_loop()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Bye!")
    sys.exit()
