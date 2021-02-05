import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.113", 9999))
while True:
    msg = input("请输入：")
    client.send(msg.encode())
    data = client.recv(1024)
    print(data.decode())