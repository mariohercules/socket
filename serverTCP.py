import socket

port = 12001
 
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.bind(('',port))
socketServer.listen(1)
 
print 'Server listening on port '+str(port)
 
while 1:
    connection, clientAddress = socketServer.accept()
    message = conexao.recv(2048)
    modifiedMessage = message.upper()
    print message + " ==> from " + str(clientAddress)
    connection.send(modifiedMessage)
connection.close()
