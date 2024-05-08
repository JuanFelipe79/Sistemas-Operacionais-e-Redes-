import socket

HOST = 'localhost'
PORT = 65432

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Ouvindo em,',PORT)
servidor.bind((HOST,PORT))
servidor.listen()
conn, addr = servidor.accept()
with conn:
    print('recebi uma conexão:', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('recebi: ',data)
        conn.sendall(data)
