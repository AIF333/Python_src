import socket
import struct
import json

HOST,PORT=('127.0.0.1',8080)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    cmd=input("Msg to send::").strip()
    if not cmd:continue
    s.sendall(cmd.encode('utf-8'))

    # 获取数据长度的 固定字节，用unpack转换成int数字，注意是元祖
    rec_bytes=s.recv(4)
    dict_size=struct.unpack('i',rec_bytes)[0]
    #print('dict_size=',dict_size)
    js_dict=s.recv(dict_size).decode('utf-8')
    data_dict=json.loads(js_dict)
    #print(data_dict)

    total_size=data_dict['size']

    # 这个地方一定要注意，因为返回的是GBK字节，而我们是分着收，
    # 如果在过程中解码将很可能会报错，等全部收完再解码，
    # rec_data一定要定义成字节空，否则无法相加
    rec_data=b''
    rec_size=0

    while rec_size < total_size:
        cmd_res=s.recv(1024)
        rec_size+=1024
        rec_data+=cmd_res
        #print('===>rec_size=',rec_size,'===>len(rec_data)=',len(rec_data),'===>len(cmd_res)=',len(cmd_res))

    # cmd_res为获取命令的执行结果,windows下的命令返回编码均是 gbk，所以需要使用gbk编码格式
    print("==>%s" %rec_data.decode('gbk'))
s.close()