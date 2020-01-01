activate_this = '/home/pi/piled/.venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

import adafruit_matrixkeypad
import board
from digitalio import DigitalInOut
import time

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

while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
    time.sleep(0.1)
