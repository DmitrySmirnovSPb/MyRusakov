import socket

SERVER_ADDRESS = ('', 15253)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(1)
print('Ждём подключения клиента...')
while True:
    c, a = server.accept()
    data = c.recv(4096).decode('UTF-8')
    print('Получили от клиента:', data)
    try:
        data = str(float(data)*10)
    except ValueError:
        if data.lower() == 'exit' or data.lower() == 'stop':
            break
        data = data.upper()
    c.send(bytes(data, encoding='UTF-8'))
    c.close()