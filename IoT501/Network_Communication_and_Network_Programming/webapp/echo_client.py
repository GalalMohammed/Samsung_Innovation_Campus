import socket

if __name__ == '__main__':
    from flask import Flask, request, redirect, render_template

    app = Flask(__name__)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.56.102', 999)
    sock.connect(server_address)

    @app.route('/')
    def select():
        message = b'SELECT'
        sock.sendto(message,server_address)
        data, server = sock.recvfrom(4096)
        return render_template('index.html', clients=eval(data.decode()))

    @app.route('/insert', methods=['GET', 'POST'])
    def insert():
        if request.method == 'POST':
            name = request.form['name']
            message = 'INSERT ' + name
            sock.sendto(message.encode(), server_address)
            return redirect('/')
        return render_template('insert.html')

    try:
        app.run(debug=True, port=80, host='0.0.0.0')
    finally:
        sock.close()
