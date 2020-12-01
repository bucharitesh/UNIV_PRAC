from socket import *
server_name = 'localhost'
server_port = 5000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

while True:
  sentence = input(">> ")
  client_socket.send(sentence.encode())
  message = client_socket.recv(2048)
  print("Message received from Server>> ", message.decode())
  
  if(sentence == 'Bye!'):
    client_socket.close()