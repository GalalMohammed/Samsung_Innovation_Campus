#!/usr/bin/python3


import socket


# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.56.102', 999)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()

    try:
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            if data:
                print(data)
                connection.sendall(data)
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
