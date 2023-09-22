from time import sleep
from pynput.keyboard import(Controller,Key)
keyboard=Controller()
sleep(600)
keyboard.press(Key.f10)
keyboard.release(Key.f10)


