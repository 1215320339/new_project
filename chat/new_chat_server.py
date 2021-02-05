import socket
from multiprocessing import Process

ADDR = "192.168.0.178", 9988
USER = {}


def do_login(server, name, addr):
    if name in USER:
        server.sendto("该用户已存在！".encode(), addr)
        return
    USER[name] = addr
    server.sendto(b"OK", addr)
    msg = "欢迎%s进入聊天室" %name
    for item in USER:
        server.sendto(msg.encode(), USER[item])

def do_chat(server, name, text):
    msg = "%s : %s" %(name, text)
    for item in USER:
        if item != name:
            server.sendto(msg.encode(), USER[item])

def do_quit(server, name):
    msg = "%s退出了聊天室！" %(name)
    for i in USER:
        if i != name:
            server.sendto(msg.encode(), USER[i])
        else:
            server.sendto(b"EXIT", USER[i])
    del USER[name]

def do_request(server):
    while True:
        data, addr = server.recvfrom(1024)
        msg = data.decode().split(" ")
        if msg[0] == "L":
            do_login(server, msg[1], addr)
        elif msg[0] == "C":
            text = " ".join(msg[2:])
            do_chat(server, msg[1], text)
        elif msg[0] == "Q":
            do_quit(server, msg[1])

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDR)
    p1 = Process(target=do_request, args=(server, ))
    p1.start()


    p1.join()

if __name__ == '__main__':
    main()