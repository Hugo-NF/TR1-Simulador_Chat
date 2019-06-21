import sys
from socket import *
from threading import Thread


def receive(sockobj):
    while True:
        incoming = sockobj.recv(1024).decode("utf8")
        print(incoming)

serverHost = 'localhost'
serverPort = 8080

sockobj = socket(AF_INET, SOCK_STREAM) #IP,  TCP

try:
    sockobj.connect((serverHost, serverPort))
    print("Connected")
except OSError:
    print("Failed to connect")
    print(sys.exc_info())
    sys.exit()

listening_thread = Thread(target=receive, args=(sockobj, ))
listening_thread.start()

while True:
    sending = input()
    if sending == "quit":
        break
    sockobj.send(bytes(sending, "utf8"))  # Send a message to the server

listening_thread.join(1)
sockobj.close()
