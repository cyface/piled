import board
import neopixel
pixels = neopixel.NeoPixel(board.D0, 30)
pixels[0] = (255, 0, 0)