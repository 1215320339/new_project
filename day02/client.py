import socket, time


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.85", 9988))

def show_dir():
    print("""
=====================================
       file             image        
=====================================
""")

def show_command():
    print("""
=====================================
============    查询    ==============
============    上传    ==============
============    下载    ==============
============    返回    ==============
=====================================
""")

def file_put():
    file_name = input("请输入要上传的文件：")
    client.send(file_name.encode())
    data = client.recv(1024)
    if data == b"ok":
        with open(file_name, "rb") as f:
            while True:
                data = f.read(1024)
                client.send(data)
                if not data:
                    time.sleep(0.1)
                    client.send(b'##')
                    break
            print(client.recv(1024).decode())
    else:
        print(data.decode())

def file_get():
    file_name = input("请输入你要下载的文件：")
    client.send(file_name.encode())
    data = client.recv(1024)
    if data == b"ok":
        client.send(b"ok")
        with open(file_name, "ab") as f:
            while True:
                data = client.recv(1024)
                if data == b"##":
                    break
                f.write(data)
                f.flush()
            print("下载成功！")
    else:
        print(data.decode())

def select_command():
    while True:
        show_command()
        msg = input("请输入选项：")
        if msg == "查询":
            client.send(b"list")
            data = client.recv(1024)
            print(data.decode())
        elif msg == "返回":
            client.send(b"back")
            break
        elif msg == "上传":
            client.send(b"put")
            if client.recv(1024) == b"ok":
                file_put()
        elif msg == "下载":
            client.send(b"get")
            if client.recv(1024) == b"ok":
                file_get()
        else:
            print("输入有误！")
def main():
    while True:
        show_dir()
        msg = input("请输入文件类型：")
        client.send(msg.encode())
        data = client.recv(1024)
        if data.decode() == "ok":
            select_command()
        else:
            print(data.decode())

if __name__ == '__main__':
    main()