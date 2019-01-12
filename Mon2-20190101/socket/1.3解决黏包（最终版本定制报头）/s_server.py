'''
此版本通过用字典定制报头，然后将字典的长度 格式化 传入即可万事大吉
'''
import socket
import subprocess
import struct
import json

HOST,PORT=('127.0.0.1',8080)

hostname=socket.gethostname()
print('My HOSTNAME is : %s , My IP is %s' %(hostname,socket.gethostbyname(hostname)) )

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #解决ip，端口异常退出占用问题
s.bind((HOST,PORT))
s.listen(2)

# 定制报头字典,两个参数 数据大小  文件名
def del_dict(size=0,filename=None):
    data_dict = {}
    data_dict['size']=size
    data_dict['filename']=filename

    #将字典序列化
    js_dict = json.dumps(data_dict).encode('utf-8')
    #获取字典长度，固定成4字节
    dict_size = len(js_dict)
    dict_bytes = struct.pack('i', dict_size)
    #send 字典长度 和 序列化后字典
    #print('---->js_dict=',js_dict,'----dict_size=',dict_size)
    conn.send(dict_bytes)
    conn.send(js_dict)

while True:
    conn,addr=s.accept()
    print('Connected by %s' %str(addr))

    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd:break
            data=subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            stdout=data.stdout.read()
            stderr=data.stderr.read()
            dic_size=len(stdout)+len(stderr)
            print("===进入方法前dic_size=",dic_size)
            del_dict(dic_size)
            # 不推荐用 conn.sendall(stdout+stderr)，因为+操作占内存，已定制报头可多次发送
            conn.sendall(stdout)
            conn.sendall(stderr)


        #处理异常，当客户端异常关闭时，服务端不受影响
        except ConnectionResetError as e:
            print('=====>%s',e)
            break
    conn.close()

s.close()
print('Closed!!!!')

