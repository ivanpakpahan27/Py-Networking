import requests
import webbrowser
import subprocess
import ipaddress

# Modul Requests
# req = requests.get('http://google.com')
# with open('sample.txt', 'w', encoding="utf-8") as f:
#     f.write(str(req.text))
# f.close()

# Modul Web Browser
# address = input("Alamat Web : ")
# webbrowser.open(address)

# Modul Subprocess
for ping in range(72, 75):
    address = "192.168.2." + str(ping)
    res = subprocess.call('ping /n 2 /w 1000 %s' % address)
    if res == 0:
        print("Ping ke alamat "+address+" OK")
    elif res == 1:
        print("Tiada respon dari "+address)
    else:
        print("Ping ke alamat "+address+" Gagal")

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
