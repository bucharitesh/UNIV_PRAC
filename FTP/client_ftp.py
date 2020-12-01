import socket
import sys
 
s = socket.socket()

PORT = 9898

s.connect(('127.0.0.1', PORT))

filename = str(input("Enter filename :: "))

file = open(filename, "rb")
SendData = file.read(1024)

while SendData:

 print("\nAcknowledgement from Server\n ",
     s.recv(1024).decode("utf-8"))

 s.send(SendData)
 SendData = file.read(1024)
s.close()
