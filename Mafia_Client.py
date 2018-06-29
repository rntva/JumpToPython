import socket

HOST = '218.51.230.202'     # The remote host
PORT = 5000                 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
message = 's'
while message != 'q' :
    message = input(" -> ")
    s.send(message.encode())
    data = s.recv(1024).decode()
    print("Received from server : " + data)
s.close()