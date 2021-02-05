from gevent import monkey
monkey.patch_all()
import gevent
import socket


def response(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print(data.decode())
        conn.send(b"ok")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("192.168.1.113", 9999))
server.listen(5)
while True:
    conn, addr = server.accept()
    print("{}已连接！".format(addr))
    gevent.spawn(response, conn)

server.close()