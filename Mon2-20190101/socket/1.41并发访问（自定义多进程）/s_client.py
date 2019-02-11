import socket

HOST,PORT=('127.0.0.1',8080)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    s_data=input('==>:').strip()

    if not s_data:continue

    s.send(s_data.encode('utf-8'))
    rec_data=s.recv(1024)
    print(rec_data.decode('utf-8'))