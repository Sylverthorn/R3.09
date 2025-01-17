
import socket


host = '127.0.0.1'
port = 4200

try:
    client_socket = socket.socket()
    client_socket.connect((host, port))
except ConnectionRefusedError:
    print("Connection refused. Server is not running.")
    exit()

while True:
    
    message = input("Enter message: ")
    client_socket.send(message.encode())
    reply = client_socket.recv(1024).decode()
    print("Server reply:", reply)


    
    if message.lower() == "bye":
        print("Deconnexion du client...")
        client_socket.close()
        break
    elif message.lower() == "arret":
        print("Client and server are shutting down...")
        client_socket.close()
        break

