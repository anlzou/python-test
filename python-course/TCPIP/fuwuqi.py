import socket
import threading
import time

def tcplink(sock,addr):
    print('接收一个来自%s：%s的连接请求'%addr)
    sock.send('成功连接服务器。。。'.encode('utf-8'))
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(5)
print('等待客户端连接...')
while True:
    sock,addr = s.accept()
    t = threading.Thread(target = tcplink,args=(sock,addr))
    t.start()
