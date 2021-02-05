import os
from day02.m import File

class Controller:
    def __init__(self):
        self.file = File()

    def select_file(self, conn):
        files = ["file", "image"]
        while True:
            file_path = r'D:\Application\data' + "\\"
            file_name = conn.recv(1024)
            if file_name.decode() in files:
                file_path += (file_name.decode() + "\\")
                conn.send(b"ok")
                self.implement(conn, file_path)
            else:
                conn.send("文件输入有误！".encode())

    def implement(self, conn, file_path):
        while True:
            try:
                data = conn.recv(1024)
            except ConnectionResetError:
                pass
            else:
                if data == b"list":
                    fl = os.listdir(file_path)
                    f = ""
                    for i in fl:
                        f += (i + "\n")
                    conn.send(f.encode())
                elif data == b"back":
                    break
                elif data == b"put":
                    conn.send(b"ok")
                    self.file.get_file(conn, file_path)
                elif data == b"get":
                    conn.send(b"ok")
                    self.file.put_file(conn, file_path)


