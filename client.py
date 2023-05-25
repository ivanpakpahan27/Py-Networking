import socket
s = socket.socket()
host = socket.gethostname()  # Mendapatkan nama mesin lokal
# Contoh menggunakan IP, host= "134.0.0.32"
port = 1234
print("host :", host)
s.connect((host, port))
print(s.recv(1024))
s.close


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
