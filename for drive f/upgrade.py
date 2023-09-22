import time
from pynput.keyboard import(Controller,Key)
keyboard=Controller()
time.sleep(600)
keyboard.press(Key.f10)
keyboard.release(Key.f10)

