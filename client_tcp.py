import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCKET IPV4 AND TCP
client.settimeout(2)
IP = "xxx"
PORT = 4433
try:
    client.connect((IP, PORT))
    client.send(b"TESTE\n")
    received_packages = client.recv(1024).decode()
    print(received_packages)
except Exception as e:
    print("um erro aconteceu... {}".format(e))