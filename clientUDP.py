import socket
ip = '192.168.0.102'
port = 12000
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input("Enter the message: ")
socketClient.sendto(message, (ip,port))
response, serverAddress = socketClient.recvfrom(2048)
print response
socketClient.close()
