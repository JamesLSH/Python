import socket
HOST = '127.0.0.1'
PORT = 8099

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

while True:
    conn, clientAddress = server.accept()
    print('Client ip is:', str(clientAddress))
    clientMessage = str(conn.recv(1024), encoding='utf-8')
    serverMessage = 'I\'m here!'
    conn.send(serverMessage.encode())
    conn.close()

    # (clientsocket, address) = serversocket.accept()
    # print('Client message is:', clientMessage)
    # print('This is a socket program test')
    # ct = client_thread(clientsocket)
    # ct.run()
