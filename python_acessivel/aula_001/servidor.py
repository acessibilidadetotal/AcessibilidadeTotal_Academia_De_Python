import socket
from datetime import *

ost = '127.0.0.1'
port = 8080

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recebe = (ost, port)

socket.bind(recebe)
socket.listen(2)

print('\nSERVIDOR INICIADO...IP: ', ost, 'PORTA: ', port)

while True:
    conexao, enderecoIP = socket.accept()
    print('\nSERVIDOR ACESSADO PELO CLIENTE:', enderecoIP, 'EM: ', datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

    while True:
        mensagem = conexao.recv(2048)
        if not  mensagem:
            break
            print('\nIP CLIENTE:', enderecoIP)
            print('MENSAGEN RECEBIDA: ', mensagem.decode(), ' - ', datetime.now().strftime('%H:%M:%S'))

            print('CONEXÃO COM O CLIENTE FINALIZADA...', enderecoIP, ' EM: ',
                  datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
            conexao.close()

