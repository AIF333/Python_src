import socket
import multiprocessing

HOST,PORT=('127.0.0.1',8080)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # 解决端口未释放问题
s.bind((HOST,PORT))
s.listen(5)

def talk(conn,addr):
    while True: #通信循环 此处可用启动子进程来替代
        data= conn.recv(1024)
        print('recv=>:%s',data)
        conn.send(data.upper())
    conn.close()

#这里就简单的接受，不做黏包处理，主要是为了实现多进程
if __name__ == '__main__':

    while True:#链接循环
        conn,addr=s.accept()
        p=multiprocessing.Process(target=talk,args=(conn,addr))
        p.start()
    s.close()
