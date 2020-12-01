from socket import *

serv_port = 5000
serv_socket = socket(AF_INET, SOCK_STREAM)
serv_socket.bind(('localhost',serv_port))
serv_socket.listen(1)

print("Server Ready, Shoot!")

conn_socket, addr = serv_socket.accept()

while True:
    sent = conn_socket.recv(2048).decode()
    print("Message received from Client>> ", sent)

    msg = input(">> ")
    conn_socket.send(msg.encode())

    if (msg == 'Bye!'):
        serv_socket.close()
