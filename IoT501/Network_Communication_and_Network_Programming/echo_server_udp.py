#!/usr/bin/python3


import socket


# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.56.102', 999)
sock.bind(server_address)

try:
    # Receive the data in small chunks and retransmit it
    while True:
        data, address = sock.recvfrom(4096)
        if data:
            print(data)
            sent = sock.sendto(data, address)
        else:
            break
finally:
    # Clean up the connection
    sock.close()
