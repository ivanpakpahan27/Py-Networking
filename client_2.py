import socket

host = socket.gethostname()
port = 1233


ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))
while True:
    Input = input('Client : ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print("Server : ", Response.decode('utf-8'))

ClientSocket.close()
