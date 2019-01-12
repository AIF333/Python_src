'''
本版本通过struct模块，格式化数据长度，来解决黏包问题，但是存在缺陷：
1.因为是int格式化，最大长度有限，大概对应为2G的数据，超出将无法发送
2.可拓展性差，如果是发送文件等，需指定文件名，md5值等
此些问题将在最终版本中解决
'''

import socket
import subprocess
import struct
# 调用subprocess模块执行window命令;linux环境下是commands模块
# 调用struct来格式化输出数字长度

print(__doc__)

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
            #第一个参数要求是字符串
            data=subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            stdout=data.stdout.read()
            stderr=data.stderr.read()

            data_size=len(stdout+stderr)
            #struct.pack('i'  格式化数字，输出4个字节byte
            data_bytes=struct.pack('i',data_size)

            #先发送固定长度的数据长度  再发送实际数据，就不会黏包
            conn.send(data_bytes)
            conn.sendall(stdout+stderr)

        #处理异常，当客户端异常关闭时，服务端不受影响
        except ConnectionResetError as e:
            print('=====>%s',e)
            break
    conn.close()

s.close()
print('Closed!!!!')

