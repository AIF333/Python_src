'''
此版本通过用字典定制报头，然后将字典的长度 格式化 传入即可万事大吉
'''
import subprocess
import struct
import json
import socketserver

# 多线程服务端，需继承类 socketserver.BaseRequestHandler，实现handle方法
class MySocketServer(socketserver.BaseRequestHandler):
    def handle(self): # 此为通信循环
        while True:
            try:
                conn=self.request
                print("===>", conn)
                print("======>", self.client_address)
                cmd=conn.recv(1024)
                if not cmd:break
                data=subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
                stdout=data.stdout.read()
                stderr=data.stderr.read()
                dic_size=len(stdout)+len(stderr)
                print("===进入方法前dic_size=",dic_size)
                MySocketServer.del_dict(conn,dic_size)
                # 不推荐用 conn.sendall(stdout+stderr)，因为+操作占内存，已定制报头可多次发送
                conn.sendall(stdout)
                conn.sendall(stderr)


            #处理异常，当客户端异常关闭时，服务端不受影响
            except ConnectionResetError as e:
                print('=====>%s',e)
                break
        conn.close()

    # 定制报头字典,两个参数 数据大小  文件名
    @staticmethod
    def del_dict(conn,size=0,filename=None):
        conn=conn
        data_dict = {}
        data_dict['size'] = size
        data_dict['filename'] = filename

        # 将字典序列化
        js_dict = json.dumps(data_dict).encode('utf-8')
        # 获取字典长度，固定成4字节
        dict_size = len(js_dict)
        dict_bytes = struct.pack('i', dict_size)
        # send 字典长度 和 序列化后字典
        # print('---->js_dict=',js_dict,'----dict_size=',dict_size)
        conn.send(dict_bytes)
        conn.send(js_dict)


if __name__ == '__main__':

    HOST,PORT=('127.0.0.1',8080)
    # 实现多线程链接循环
    s=socketserver.ThreadingTCPServer((HOST,PORT),MySocketServer)
    s.serve_forever()






