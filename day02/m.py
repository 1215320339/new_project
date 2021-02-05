import os, time


class File:
    def get_file(self, conn, file_path):
        file_name = conn.recv(1024)
        file = file_name.decode().split("\\")
        fl = os.listdir(file_path)
        if file[-1] not in fl:
            conn.send(b"ok")
            file_path += file[-1]
            with open(file_path, "ab") as f:
                while True:
                    data = conn.recv(1024)
                    if data == b"##":
                        break
                    f.write(data)
                    f.flush()
                conn.send("上传成功！".encode())
        else:
            conn.send("该文件已存在！".encode())

    def put_file(self, conn, file_path):
        file_name = conn.recv(1024)
        fl = os.listdir(file_path)
        if file_name.decode() in fl:
            conn.send(b"ok")
            if conn.recv(1024) == b"ok":
                with open(file_path + file_name.decode(), "rb") as f:
                    while True:
                        data = f.read(1024)
                        conn.send(data)
                        if not data:
                            time.sleep(0.1)
                            conn.send(b"##")
                            break

        else:
            conn.send("没有你要的文件！".encode())