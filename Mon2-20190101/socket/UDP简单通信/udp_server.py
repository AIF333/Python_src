'''简单的udp通信，与tcp不同，udp不需要建立链接
接受消息是 recvfrom 方法，会自动获取到信息来源的地址
发送信息是 sendto  需要制定地址
udp发送的消息会自动加头，不存在真正意义的空消息，不需要和tcp一样处理空的判断
所以空也能发送和接受：如 (b'', ('127.0.0.1', 51016))
'''

import socket

HOST,PORT=('127.0.0.1',8080)

u_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
u_server.bind((HOST,PORT))

while True:
    rec_data, addr=u_server.recvfrom(1024)  # (b'hjh', ('127.0.0.1', 51016))
    upper_data=rec_data.upper()
    u_server.sendto(upper_data,addr)
    print(upper_data,addr)
