#
# Connect to alien server ('localhost', 10000)
#
# Then send and receive the response, for each of these values:
# USER
# aliensignal
# PASS
# unlockserver
# SEND
# moonbase
# END
#
# Note: You must receive data back from the server after you send each value
#



import socket
host = 'localhost'
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
def sen(line):
    s.sendall(bytes(line, 'utf-8')) 
    print(s.recv(1024).decode())
sen('USER')
sen('aliensignal')
sen('PASS')
sen('unlockserver')
sen('SEND')
sen('moonbase')
sen('END')

s.close()    
