#!/usr/bin/python3
import socket

if __name__ == '__main__':
    from models.model import Base, Client
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Create a UDP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('192.168.56.102', 999)
    sock.bind(server_address)

    engine = create_engine('mysql+mysqldb://root@localhost/mysql')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Receive the data in small chunks
        while True:
            data, address = sock.recvfrom(4096)
            if data:
                if data.decode() == 'SELECT':
                    data = [obj.name for obj in session.query(Client).all()]
                    data = data.__repr__()
                    sock.sendto(data.encode(), address)
                elif data.decode()[:6] == 'INSERT':
                    row = Client(name=data.decode()[7:])
                    session.add(row)
                    session.commit()
            else:
                break
    finally:
        # Clean up the connection
        sock.close()
