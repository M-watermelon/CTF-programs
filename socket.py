# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory

import socket
host = 'localhost'
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
s.sendall(bytes('ls /tmp', 'utf-8'))  

print (s.recv(1024).decode())

s.close()   
