import socket

ip = '172.19.7.239'
porta = 12001
mensagem = ''

while mensagem.find('.') < 0:
    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketCliente.connect((ip,porta))
    mensagem = raw_input("Digite uma mensagem: ")

    socketCliente.send(mensagem)
    resposta = socketCliente.recv(2048)
    print resposta

socketCliente.close()
