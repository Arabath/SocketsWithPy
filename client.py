import socket

IP_SERVER = "localhost"
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

clientSocket = socket.socket()

clientSocket.connect(ADDRESS)

print("CLIENT connected...")

msg = clientSocket.recv(1024).decode()

print(msg)

while True:
    try:
        userInput = int(input("Choose a question (1/2): "))
        clientSocket.send(str(userInput).encode())
        break
    except:
        print("Invalid Input, choose between Input 1 or 2")

print(f"Server RESPONSE -> {clientSocket.recv(1024).decode()}")