import os, time


class Model:
    def __init__(self, r):
        self.r = r

    def get_file(self, file_path):
        file_name = self.r.recv(1024)
        file = file_name.decode().split("\\")
        fl = os.listdir(file_path)
        if file[-1] not in fl:
            self.r.send(b"ok")
            file_path += file[-1]
            with open(file_path, "ab") as f:
                while True:
                    data = self.r.recv(1024)
                    if data == b"##":
                        break
                    f.write(data)
                    f.flush()
                self.r.send("上传成功！".encode())
        else:
            self.r.send("该文件已存在！".encode())

    def put_file(self, file_path):
        file_name = self.r.recv(1024)
        fl = os.listdir(file_path)
        if file_name.decode() in fl:
            self.r.send(b"ok")
            if self.r.recv(1024) == b"ok":
                with open(file_path + file_name.decode(), "rb") as f:
                    while True:
                        data = f.read(1024)
                        self.r.send(data)
                        if not data:
                            time.sleep(0.1)
                            self.r.send(b"##")
                            break

        else:
            self.r.send("没有你要的文件！".encode())