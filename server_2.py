# Imports
import socket
from _thread import *

# Declarations
host = socket.gethostname()
port = 1233


def client_handler(connection):
    message = "You are now connected to the replay server... Type BYE to stop"
    connection.send(message.encode('utf-8'))
    while True:
        data = connection.recv(2048)
        message = data.decode('utf-8')
        print("Client : ", message)
        if message == 'BYE':
            break
        reply = input("Server : ")
        connection.sendall(str.encode(reply))
    connection.close()


def accept_connections(ServerSocket):
    global ThreadCount
    Client, address = ServerSocket.accept()
    ThreadCount = ThreadCount + 1
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))
    print("Jumlah perangkat terhubung ", ThreadCount)


def start_server(host, port):
    global ThreadCount
    ThreadCount = 0
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)


start_server(host, port)
