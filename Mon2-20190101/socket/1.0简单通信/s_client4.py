import socket
HOST,PORT=('127.0.0.1',8080)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    data=input("Msg to send::").strip()
    if not data:continue

    s.sendall(data.encode('utf-8'))
    res_data=s.recv(1024).decode('utf-8')
    print("Recevied data is %s" %res_data)
s.close()