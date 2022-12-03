import socket
import json
from crypto import Crypto

HOST = "127.0.0.1"
PORT = 65432

f = open('config.json')
config = json.load(f)
GENERATING_ALGORITHM = config['number_generating']
KEY = config['key']

crypto = Crypto(GENERATING_ALGORITHM, KEY)

def client_program():
    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        message = crypto.encrypt(message)
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        data = crypto.decrypt(str(data))

        print('Received from server: ' + data)

        message = input(" -> ")

    client_socket.close()


if __name__ == '__main__':
    client_program()