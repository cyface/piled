activate_this = '/home/pi/piled/.venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

import adafruit_matrixkeypad
import board
from digitalio import DigitalInOut
import time

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

while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
    time.sleep(0.1)
