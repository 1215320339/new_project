import socket
from threading import Thread
from day02.controller import Controller


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("192.168.0.85", 9988))
server.listen(5)
c = Controller()

while True:
    conn, addr = server.accept()
    t = Thread(target=c.select_file, args=(conn, ))
    t.setDaemon(True)
    t.start()