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

def server_program():
    server_socket = socket.socket()
    server_socket.bind((HOST,PORT))

    server_socket.listen(2)

    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        message = crypto.decrypt(str(data))
        if not data:
            break
        print("from connected user: " + message)
        data = input(' -> ')
        data = crypto.encrypt(data)
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_program()