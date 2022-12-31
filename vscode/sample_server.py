import socket
import time
from _thread import *
import pickle

server = ''
port = 22222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((server, port))
except socket.error as e:
    str(e)
sock.listen(2)
print("Waiting for a connection, Server Started")

clients = []

while True:
    conn, _ = sock.accept()
    try:
        clients.append(conn)
        print(conn)
        if len(clients) == 2:
            print("Two clients have joined, starting game...")
            for client in clients:
                client.sendall(b"start")

            while True:
                data = clients[0].recv(1024)
                if data:
                    clients[1].sendall(data)
                else:
                    clients.remove(clients[0])
                    clients[0].close()
                    break
                data = clients[1].recv(1024)
                if data:
                    clients[0].sendall(data)
                else:
                    clients.remove(clients[1])
                    clients[0].close()
                    break

    except Exception as e:
        print(e)
        conn.close()