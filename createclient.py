import socket
import sys
import time

server=socket.socket()
port = 2727
print("Establishing Connection at-",port)
server.connect(('127.0.0.1',port))
print("Connection Established! at port-->",port)

print("___________User Info__________")

name=input("Joining As(Enter-UserName)")#Clients Name
print("______________________________")

encoded_name = name.encode()
server.send(encoded_name)

while True:
    outgoing_message = input(str("Client>>"))
    outgoing_message_ecoded = outgoing_message.encode()
    server.send(outgoing_message_ecoded)
    print("You>>", outgoing_message)

    incoming_message = server.recv(1024).decode()
    print("Server>>",incoming_message)
















