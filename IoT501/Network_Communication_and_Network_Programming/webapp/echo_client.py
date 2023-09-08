import socket

if __name__ == '__main__':
    from flask import Flask, request, redirect, render_template

    app = Flask(__name__)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.56.102', 999)
    sock.connect(server_address)

    @app.route('/')
    def select():
        message = b'SELECT'
        sock.sendall(message)
        data = sock.recv(16)
        return render_template('index.html', clients=eval(data.decode()))

    @app.route('/insert')
    def insert():
        if request.method == 'POST':
            name = request.form['name']
            message = 'INSERT ' + name
            message.encode()
            sock.sendall(message)
            return redirect('/')
        return render_template('insert.html')

    try:
        app.run(debug=True, port=80, host='0.0.0.0')
    finally:
        sock.close()
