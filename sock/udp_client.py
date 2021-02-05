import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("192.168.0.178", 9999)

while True:
    msg = input("发送：")
    if not msg:
        break
    sockfd.sendto(msg.encode(), addr)
    data, addr = sockfd.recvfrom(1024)
    print(data.decode())

sockfd.close()