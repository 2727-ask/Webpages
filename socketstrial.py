import socket
server = socket.socket()#here by default TCP
print("Socket Created!")

server.bind(('192.168.1.104',5638))
print("Server Bounded Successfully!")

server.listen(10)#count of valid connections

print("Server is waiting for connections.....")
print("------------------------------------------------")

#accepts  Clients and address
client,address=server.accept()
print(address,"Connected!")
print("-*-*-*-*-*-*-*- CHAT ROOM -*-*-*-*-*-*-*-*-*-")

encoded_name = client.recv(1024).decode()
print(encoded_name,"joined")

while 10:
    Server_message = input(str("Server-->"))
    print("You -->", Server_message)
    Server_message_encoded = Server_message.encode()
    client.send(Server_message_encoded)


    incoming_message = client.recv(1024).decode()
    print(encoded_name,"said -->",incoming_message)
    
    
print("______________Process Ended __________________")    

print("Reload Server To Chat")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")








