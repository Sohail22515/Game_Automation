from pynput.keyboard import Controller
import time

keyboard = Controller()

right_pressed = 'd'
left_pressed = 'a'

def PressKey(key):
    keyboard.press(key)

def ReleaseKey(key):
    keyboard.release(key)

if __name__ == '__main__':
    while True:
        PressKey('w')     
        time.sleep(1)
        ReleaseKey('w') 
        time.sleep(1)
