import socket
import os

server = str(os.getenv('SERVER'))
port = os.getenv('PORT')
nickname = str(os.getenv('NICKNAME'))
token = str(os.getenv('TOKEN'))
channel = str(os.getenv('CHANNEL'))

print(server, port, nickname, token, channel)

sock = socket.socket()

sock.connect((server, int(port)))
sock.send("PASS {0}\n NICK {1}\n JOIN {2}\n".format(token, nickname, channel).encode('utf-8'))

while True:
    rec = sock.recv(2048).decode('utf-8')

    print(rec)
