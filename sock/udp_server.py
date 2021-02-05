import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sockfd.bind(("192.168.0.178", 9999))

while True:
    data, addr = sockfd.recvfrom(1024)
    print(addr)
    if not data:
        break
    print(data.decode())
    msg = input("回复：")
    sockfd.sendto(msg.encode(), addr)

sockfd.close()