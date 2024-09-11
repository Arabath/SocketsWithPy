import socket
import time #get current time
import datetime #get current date


#IP_SERVER = socket.gethostbyname(socket.gethostname())

IP_SERVER = 'localhost'
PORT = 9999
ADDRESS = (IP_SERVER, PORT)

def recvUser():
    msg = int(connection.recv(1024).decode())

    if msg == 1:
        print(f"USER Requested Time, SUCCESSFULLY SEND TIME TO USER...")
        connection.send(f"TIME -> {time.ctime()}".encode())
    elif msg == 2:
        print(f"USER Requested current date, SUCCESSFULLEY SEND CURRENT DATE TO USER")
        connection.send(f"DATE -> {datetime.datetime.now()}".encode())
    else:
        print(f"USER REQUESTED UNKOWN SERVICE, ERROR!")
        connection.send(f"Your request is not valid, choose between 1 or 2".encode())
            

serverSocket = socket.socket()

# 1 argument -> Type of Network (IPv4)
# 2 argument -> Type of Connection (TCP)

serverSocket.bind(ADDRESS)
print(f"Server STARTED...")

serverSocket.listen(3)

listOfQuestion = ["What time it is", "What is today's date"]

while True:
    connection, address = serverSocket.accept()

    print(f"USER connected -> {address}")

    connection.send(f"Hello Client, Ask the following questions \n{listOfQuestion}".encode())

    recvUser()