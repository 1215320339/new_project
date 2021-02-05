import socket, time, sys


def put_file(client):
    while True:
        file_name = input("请输入要上传的文件：")
        try:
            with open(file_name, "rb") as f:
                client.send(file_name.encode())
                data = client.recv(1024)
                if data == b"ok":
                    while True:
                        data = f.read(1024)
                        client.send(data)
                        if not data:
                            time.sleep(0.1)
                            client.send(b'##')
                            break
                    print(client.recv(1024).decode())
                    break
                else:
                    print(data.decode())
                    break
        except FileNotFoundError:
            print("没有找到该文件！")
            continue

def get_file(client):
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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.85", 9999))

def main():
    while True:
        client.send(b"ok")
        print(client.recv(1024).decode())
        msg = input("请输入你要选择的文件类型：")
        client.send(msg.encode())
        data = client.recv(1024).decode()
        if data != "no":
            print(data)
            while True:
                m = input("请输入你的选项：")
                if m == "返回":
                    client.send(m.encode())
                    if client.recv(1024) == b"ok":
                        break
                elif m == "查询":
                    client.send(m.encode())
                    print(client.recv(1024).decode())
                    print(client.recv(1024).decode())
                elif m == "上传":
                    client.send(m.encode())
                    put_file(client)
                    print(client.recv(1024).decode())
                elif m == "下载":
                    client.send(m.encode())
                    get_file(client)
                    print(client.recv(1024).decode())
                elif m == "退出":
                    client.send(m.encode())
                    if client.recv(1024) == b"ok":
                        sys.exit("你已退出！")
                else:
                    print("输入的选项有误！")
        else:
            print("输入的文件类型错误！")
            continue


if __name__ == '__main__':
    main()