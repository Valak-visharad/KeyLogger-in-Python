import os
from Mail_hotmail import mail
from datetime import date
import socket
host = socket.gethostname()
date = date.today()
dd = str(date)
date_stamp = str(dd[-5] + dd[-4] + dd[-2] + dd[-1])
os.system('del \"C:\\Program_Files\\Intel\\Media Resource\\list.txt\"')
os.system('ls \"C:\\Program_Files\\Intel\\Intel(R) Serial IO\" >> \"C:\\Program_Files\\Intel\\Media Resource\\list.txt\"')
file = open("C:\\Program_Files\\Intel\\Media Resource\\list.txt", 'r')
file.seek(0)
a = 1
try:
    for i in file.readlines():
        val = int(i[0] + i[1] + i[2] + i[3])
        if (val < int(date_stamp)):
            i = i.split('\n')[0]
            textfile = open("C:\\Program_Files\\Intel\\Intel(R) Serial IO\\" + i, 'r')
            msg = 'File no.'+ str(a) + 'from ' + str(host) + '\nFile Name : ' + str(i) + '\n\n'
            for j in textfile.readlines():
                msg += '\n' + j
            mail(msg)
        os.system("del \"C:\\Program_Files\\Intel\\Intel(R) Serial IO\\" + i + ".txt\"")
        a += 1
        os.system('del \C:\\Program_Files\\Intel\\Media Resource\list.txt\"')
        mail('success report from ' + str(host))
except:
    print('An Error Occured')
