import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPV4 ADD UDP

IP = "xxx"
PORT = 4433

try:
    while True:
        msg = input("Message: ") + "\n"
        client.sendto(msg.encode(), (IP, PORT))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ":" + data.decode())
        if data.decode() == "quit\n" or msg == "quit\n":
            break
    client.close()
except Exception as e:
    print("um erro aconteceu... {}".format(e))
    client.close()