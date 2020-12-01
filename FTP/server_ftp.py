import socket
s = socket.socket()

PORT = 9898

print("Server up and ready at :", PORT, "\n")
s.bind(('127.0.0.1', PORT))
s.listen(10)
file = open("recieved.txt", "ab+")

while True:
 conn, addr = s.accept()

 msg = "---|\n Hi Client[IP address: " + addr[0] + "],|------|\n \n\n"
 conn.send(msg.encode())
 
 RecvData = conn.recv(1024)
 while RecvData:
     file.write(b"\n")
     file.write(RecvData)
     RecvData = conn.recv(1024)

 file.close()
 print("File has been copied successfully.\n")

 conn.close()
 print("Server closed the connection!\n")

 print("The content of the file is:-\n")
 f = open("recieved.txt", "r")
 print(f.read())
 break
