from socket import socket

with socket() as socket:
    socket.bind(('', 4000))
    socket.listen(1)

    while True:
        conn, addr = socket.accept()
        recv_msg = conn.recv(1024)
        print(recv_msg.decode())
        send_msg = 'OK'
        conn.sendall(send_msg.encode())
        conn.close()