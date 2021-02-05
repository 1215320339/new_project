import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.bind(("192.168.1.113", 9999))

sockfd.listen(5)

while True:
    conn, addr = sockfd.accept()
    print(conn, addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("接收到消息：", data.decode())
        msg = input("回复：")
        conn.send(msg.encode())
    conn.close()