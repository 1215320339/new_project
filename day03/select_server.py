import socket, os, time
from select import select
from day03.view import View
from day03.model import Model


def print_file(file_path, file_name, r):
    fiel_path = file_path + file_name + "\\"
    f = os.listdir(fiel_path)
    fs = ""
    for i in f:
        fs += (i + "\n")
    r.send(fs.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 9999))
server.listen(5)

rlist = [server]
wlist = []
xlist = []
file_type = ["file", "image"]

while True:
    flag = True
    rl, wl, xl = select(rlist, wlist, xlist)
    for r in rl:
        if r is server:
            conn, addr = r.accept()
            print(addr)
            rlist.append(conn)
        else:
            view = View(r)
            model = Model(r)
            file_path = "D:\\Application\\data\\"
            while flag:
                if r.recv(1024).decode() == "ok":
                    view.show_file_type()
                file_name = r.recv(1024).decode()
                if file_name in file_type:
                    view.show_file_option()
                else:
                    r.send(b"no")
                    continue
                while flag:
                    data = r.recv(1024).decode()
                    if data == "返回":
                        r.send(b"ok")
                        break
                    elif data == "查询":
                        print_file(file_path, file_name, r)
                        time.sleep(0.1)
                        view.show_file_option()
                    elif data == "上传":
                        model.get_file(file_path + file_name + "\\")
                        time.sleep(0.1)
                        view.show_file_option()
                    elif data == "下载":
                        model.put_file(file_path + file_name + "\\")
                        time.sleep(0.1)
                        view.show_file_option()
                    elif data == "退出":
                        flag = False
                        wlist.append(r)
                        rlist.remove(r)
                        break

    for w in wl:
        w.send(b"ok")
        wlist.remove(w)
        w.close()
