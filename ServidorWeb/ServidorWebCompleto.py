import socket

HOST = 'localhost'
PORT = 80

# Definição de host e porta
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Ouvindo em ', PORT)
servidor.bind((HOST, PORT))
servidor.listen()
conn, addr = servidor.accept()
with conn:
    print('Recebi uma conexão: ', addr)
    data = conn.recv(1024)
    linhas = data.decode().split('\n')  # Decodifica os bytes recebidos e divide em linhas
    for linha in linhas:
        if 'User-Agent' in linha:  # Verifica se a linha contém o cabeçalho User-Agent
            navegador = linha.split(': ')[1].strip()  # Extrai o nome do navegador
            print('Navegador usado:', navegador)
    resposta = 'HTTP/1.1 200 OK\n'
    resposta += 'Content-Type: text/html\n\n'
    conn.sendall(str.encode(resposta))
    arq = open('hello_world.html', 'r')  # Abre o arquivo hello_world.html
    conn.sendall(str.encode(arq.read()))  # Lê o arquivo todo e envia pela conexão
    arq.close()
servidor.close()
