from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from time import sleep

mouse = MouseController()
keyboard =KeyboardController()
sleep(5)

while True:
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.move(200,0)
    sleep(0.5)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.move(0,200)
    sleep(0.5)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.move(-200,0)
    sleep(0.5)
    mouse.click(Button.left, 1)
    sleep(0.5)
    mouse.move(0,-200)
    sleep(0.5)
    
