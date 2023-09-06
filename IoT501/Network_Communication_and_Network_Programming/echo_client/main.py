import socket


# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.56.102', 999)
sock.connect(server_address)

try:
    # Send data
    message = b'It is a message'
    sent = sock.sendto(message, server_address)

    # Receive response
    data, server = sock.recvfrom(4096)
    print(data)
finally:
    sock.close()
