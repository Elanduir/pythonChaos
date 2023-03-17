from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from time import sleep

mouse = MouseController()
keyboard =KeyboardController()
sleep(5)

while True:
    mouse.move(200,200)
    sleep(1)
    mouse.click(Button.left, 1)
    sleep(1)
    keyboard.press('1')
    sleep(0.5)
    keyboard.release('1')
    sleep(0.5)
    mouse.move(-200,200)
    sleep(1)
    keyboard.press('2')
    sleep(0.5)
    keyboard.release('2')
    sleep(0.5)
