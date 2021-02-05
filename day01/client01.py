import socket, os
from threading import Thread


def test_send(skt):
    while True:
            msg = "I " + input(">>")
            addr = ('192.168.0.178',9988)
            skt.sendto(msg.encode(),addr)

def test_recv(skt):
    while True:
            rst, addr = skt.recvfrom(1024)
            if rst.decode() == "q":
                print("您已退出！")
                os._exit(0)
            print(rst.decode())

def main():
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        addr = ('192.168.0.178',9988)
        name = input("请输入你的姓名：")
        msg = "N " + name
        skt.sendto(msg.encode(), addr)
        data, addr = skt.recvfrom(1024)
        if data == b"NO":
            print("该姓名已存在！")
        else:
            print(data.decode())
            break

    t1 = Thread(target=test_send, args=(skt, ))
    t2 = Thread(target=test_recv, args=(skt, ))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()