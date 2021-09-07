import socket

ost = '127.0.0.1'
port = 8080

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
envio = (ost,port)
soquete.connect(envio)

print('Digite: S     e pressione ENTER para encerrar...')
print('DIGITE A MENSAGEM: ')
mensagem = input()
while mensagem not in ('s','S'):
    socket.send_fds(str(mensagem).encode())
    mensagem = input()

    soquete.close()