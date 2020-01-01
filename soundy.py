from pygame import mixer
from time import sleep
from gpiozero import Button

mixer.init()

soundObj = mixer.Sound('laser.wav')
soundObj.play()

button = Button(7)
while True:
    if button.is_pressed:
        print("pressed")
        soundObj.play()
        sleep(.25)  # wait and let the sound play for X second