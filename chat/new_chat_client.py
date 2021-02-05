import socket, sys
import os

ADDR = "192.168.0.178", 9988


def send_msg(client, name):
    while True:
        try:
            text = input("发送：")
        except KeyboardInterrupt:
            text = "quit"
        if text == "quit":
            msg = "Q " + name
            client.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室！")
        msg = "C %s %s" %(name, text)
        client.sendto(msg.encode(), ADDR)

def recv_msg(client):
    while True:
        data, addr = client.recvfrom(1024)
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        name = input("请输入姓名：")
        msg = "L " + name
        client.sendto(msg.encode(), ADDR)
        data, addr = client.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室！")
            break
        else:
            print(data.decode())

    pid = os.fork()
    if pid < 0:
        sys.exit()
    elif pid == 0:
        send_msg(client, name)
    else:
        recv_msg(client)



if __name__ == '__main__':
    main()