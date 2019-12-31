activate_this = '/home/pi/piled/.venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 8, brightness=.02)
# for i in range(8):
#     pixels[i] = (255, 0, 0)
#     time.sleep(.25)
#
# for i in range(7, -1, -1):
#     pixels[i] = (0, 0, 0)
#     time.sleep(.25)
#
# pixels[0] = (255, 0, 0)
# time.sleep(.25)
# pixels[1] = (255, 165, 0)
# time.sleep(.25)
# pixels[2] = (255, 255, 0)
# time.sleep(.25)
# pixels[3] = (0, 255, 0)
# time.sleep(.25)
# pixels[4] = (0, 0, 255)
# time.sleep(.25)
# pixels[5] = (38, 0, 66)
# time.sleep(.25)
# pixels[6] = (255, 0, 255)
# time.sleep(.25)
# pixels[7] = (255, 255, 255)
# time.sleep(1)
#
# for i in range(7, -1, -1):
#     pixels[i] = (0, 0, 0)
#     time.sleep(.25)

# for r, g, b in zip(range(256), range(255, -1, -1), range(256)):
#     for pixel in range(8):
#         pixels[pixel] = (r, g, b)
#         time.sleep(.01)

rainbow = [
    (255, 0, 0),
    (255, 165, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 0, 255),
    (38, 0, 66),
    (255, 0, 255),
]

for color in rainbow:
    for pixel in range(8):
        pixels[pixel] = color
    time.sleep(.125)

time.sleep(1)

pixels.fill((0, 0, 0))
