'''简单的udp通信，与tcp不同，udp不需要建立链接
接受消息是 recvfrom 方法，会自动获取到信息来源的地址
发送信息是 sendto  需要制定地址
udp发送的消息会自动加头，不存在真正意义的空消息，不需要和tcp一样处理空的判断
所以空也能发送和接受：如 (b'', ('127.0.0.1', 51016))
'''

import socketserver

class MyUDPSever(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request) #(消息，socket对象) (b'aa', <socket.socket fd=212, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0, laddr=('127.0.0.1', 8080)>)
        self.request[1].sendto(self.request[0].upper(),self.client_address)

HOST,PORT=('127.0.0.1',8080)

if __name__ == '__main__':
    s=socketserver.ThreadingUDPServer((HOST,PORT),MyUDPSever)
    s.serve_forever()