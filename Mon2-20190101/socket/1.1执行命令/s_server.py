import socket
import subprocess

HOST,PORT=('127.0.0.1',8080)

hostname=socket.gethostname()
print('My HOSTNAME is : %s , My IP is %s' %(hostname,socket.gethostbyname(hostname)) )

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #解决ip，端口异常退出占用问题
s.bind((HOST,PORT))
s.listen(2) #监听最大数量，即客户端能等待的最大数量

while True:
    conn,addr=s.accept()
    print('Connected by %s' %str(addr))

    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd:break
            #调用subprocess模块执行window命令;linux环境下是commands模块
            #第一个参数要求是字符串
            data=subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            stdout=data.stdout.read()
            stderr=data.stderr.read()

            conn.sendall(stdout+stderr)
        except ConnectionResetError as e:
            print('=====>%s',e)
            break
    conn.close()

s.close()
print('Closed!!!!')

