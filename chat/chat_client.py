import socket
from multiprocessing import Process


ADDR = "192.168.0.178", 9988

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        name = input("请输入您的姓名：")
        msg = "N " + name
        client.sendto(msg.encode(), ADDR)
        data, addr = client.recvfrom(1024)
        if data.decode() == "NO":
            print("该名称已存在！")
            continue
        else:
            print(data.decode())
            break


if __name__ == '__main__':
    main()