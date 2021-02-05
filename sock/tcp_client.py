import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.connect(("192.168.0.178", 9999))

while True:
    msg = input("发送：")
    if not msg:
        break
    sockfd.send(msg.encode())

    data = sockfd.recv(1024)
    print(data.decode())

sockfd.close()