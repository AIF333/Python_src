import socket
import subprocess
HOST,PORT=('127.0.0.1',8080)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    cmd=input("Msg to send::").strip()
    if not cmd:continue
    s.sendall(cmd.encode('utf-8'))

    #cmd_res为获取命令的执行结果,windows下的命令返回编码均是 gbk，所以需要使用gbk编码格式
    cmd_res=s.recv(1024).decode('gbk')
    print("Recevied data is %s" %cmd_res)
s.close()