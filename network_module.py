import inspect
import requests
import webbrowser
import subprocess
import ipaddress
import os
import socket

# Modul Requests
# req = requests.get('http://google.com')
# with open('sample.txt', 'w', encoding="utf-8") as f:
#     f.write(str(req.text))
# f.close()

# Modul Web Browser
# address = input("Alamat Web : ")
# webbrowser.open(address)

# Modul Subprocess
# for ping in range(72, 75):
#     address = "192.168.2." + str(ping)
#     res = subprocess.call('ping /n 2 /w 1000 %s' % address)
#     if res == 0:
#         print("Ping ke alamat "+address+" OK")
#     elif res == 1:
#         print("Tiada respon dari "+address)
#     else:
#         print("Ping ke alamat "+address+" Gagal")

# Modul IP Address
# myIpAddress = input('Enter an IP Address with a CIDR >>> ')  # 192.168.0.1/24
# myAdd = ipaddress.ip_interface(myIpAddress)
# # False lets you enter any ip address in the /24 ip address block.
# myNet = ipaddress.ip_network(myAdd, strict=False)
# for i in myNet:
#     canPing = subprocess.call('ping /n 2 /w 1000 %s' % str(i))
#     if canPing == 0:
#         print('I can ping %s.' % str(i))
#     if canPing == 1:
#         print('%s is not responding' % str(i))

# Modul os.popen
# ip = input("IP Address Target : ")
# results = os.popen("pathping " + str(ip))
# for i in results:
#     print(i)
# print(inspect.getargspec(os.popen))

# Modul Socket
# Create a new socket using the given address family
# socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Setting up the default timeout in seconds for new socket object
# socket.setdefaulttimeout(1)
# addr = "192.168.2.75"  # Ip Address target dapat diketahui dari hasil ping
# port = 80
# result = socket_obj.connect_ex((addr, port))
# if result == 0:
#     print("Connected")
# else:
#     print("Disconnect")
# socket_obj.close()

socket.setdefaulttimeout(1)
addr = "127.0.0.1"
daftar_port = [20, 21, 22, 23, 25, 53, 79,
               80, 110, 137, 138, 139, 443, 445, 3306]
for port in daftar_port:
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = socket_obj.connect_ex((addr, int(port)))
    if result == 0:
        print("Terbuka Port "+str(port))
        socket_obj.close()
    else:
        print("Tertutup Port "+str(port))
        socket_obj.close()
