import socket

HOST,PORT=('127.0.0.1',8080)

u_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data=input('=>:').strip() #此处不需要处理空的判断，因为会自动封账加ip，端口，不存在真正的空消息
    u_client.sendto(data.encode('utf-8'),(HOST,PORT))
    rec_data,addr=u_client.recvfrom(1024)
    print(rec_data.decode('utf-8'))