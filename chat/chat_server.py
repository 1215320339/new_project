import socket
from multiprocessing import Process

ADDR = "192.168.0.178", 9988
USER = []


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDR)
    while True:
        data, addr = server.recvfrom(1024)
        msg = data.decode().split(" ")
        if msg[0] == "N":
            send_no_line(addr, msg, server)


def send_no_line(addr, msg, server):
    if add_user(addr, msg, server):
        for item in USER:
            if item[0] != msg[1]:
                server.sendto(("%s 上线！" % msg[1]).encode(), item[1])
            else:
                server.sendto("你已上线！".encode(), item[1])


def add_user(addr, msg, server):
    if USER:
        for item in USER:
            if item[0] == msg[1]:
                server.sendto("NO".encode(), item[1])
                slogan = False
                break
        else:
            USER.append((msg[1], addr))
            slogan = True
    else:
        USER.append((msg[1], addr))
        slogan = True
    return slogan


if __name__ == '__main__':
    main()