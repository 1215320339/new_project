import socket
# from multiprocessing import Process


ADDR = "192.168.0.178", 9988
USERS = {}

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDR)
    while True:
        data, addr = server.recvfrom(1024)
        msg = data.decode().split(" ")
        if msg[0] == "N":
            if msg[1] not in USERS:
                USERS[msg[1]] = addr
                for addr in USERS.values():
                    server.sendto(("%s上线！" %msg[1]).encode(), addr)
            else:
                server.sendto(b"NO", addr)
        elif msg[0] == "I":
            if msg[1] == "exit":
                server.sendto("q".encode(), addr)
            do_recv(server, msg, addr)


def do_recv(server, msg, addr):
    msg = msg[1:]
    m = " ".join(msg)
    for key, value in USERS.items():
        if value == addr:
            for v in USERS.values():
                server.sendto((key + ":" + m).encode(), v)

if __name__ == '__main__':
    main()