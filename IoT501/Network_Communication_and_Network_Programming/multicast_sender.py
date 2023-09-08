#!/usr/bin/python3


import socket
import struct


message = b'data'
multicast_group = ('224.10.10.10', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket doesn't block indefinitely
# when trying to receive data
sock.settimeout(.2)

# Set the time-to-live for messages to 1
# so they don't go past the local network segment
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    # Send data to the multicast group
    sent = sock.sendto(message, multicast_group)

    # Look for response from all recipients
    while True:
        try:
            data, server = sock.recvfrom(4096)
        except socket.timeout:
            break
        else:
            print(f"received {data!r} from {server}")
finally:
    # Clean up the connection
    sock.close()
