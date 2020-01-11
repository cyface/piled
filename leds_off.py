activate_this = '/home/pi/piled/.venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

import board
import neopixel_spi

NUM_PIXELS = 8
spi = board.SPI()

pixels = neopixel_spi.NeoPixel_SPI(spi, NUM_PIXELS, brightness=0.2)
pixels.fill(0)
