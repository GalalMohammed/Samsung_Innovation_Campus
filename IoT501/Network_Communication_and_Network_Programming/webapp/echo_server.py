#!/usr/bin/python3
import socket

if __name__ == '__main__':
    from models.model import Client
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('192.168.56.102', 999)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    engine = create_engine('mysql+mysqldb://root@localhost/mysql')
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        # Wait for a connection
        connection, client_address = sock.accept()
        try:
            # Receive the data in small chunks
            while True:
                data = connection.recv(16)
                if data:
                    if data.decode() == 'SELECT':
                        data = session.query(Client).all()
                        connection.sendall(data.__repr__())
                    elif data.decode()[:6] == 'INSERT':
                        row = Client(name=data.decode()[6:])
                        session.add(row)
                        session.commit()
                else:
                    break
        finally:
            # Clean up the connection
            sock.close()
