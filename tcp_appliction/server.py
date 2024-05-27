"""
Server module for receiving traffic from a client.

Usage:
    python server.py <ip_server> <port>

Arguments:
    ip_server: IP address of the server, can be localhost
    port: Port number to listen on

Functions:
    start_server(ip_server, port): Starts the server to accept connections from clients and receive messages.
"""

import socket
import sys


def start_server(ip_server, port):
    """
    Starts the server to accept connections from clients and receive messages.

    :param ip_server: IP address of the server, can be localhost
    :param port: Port number to listen on
    :return: None
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip_server, port)
    print('starting up on %s port %s' % server_address, file=sys.stderr)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print('waiting for connection')
        connection, client_adress = sock.accept()

        try:
            print(f'connection from {client_adress}')

            while True:
                data = connection.recv(1024)
                if data:
                    print(f'received {data}')
                else:
                    print(f'no more data from {client_adress}')
                    break

        finally:
            connection.close()


if __name__ == '__main__':
    ip_server = sys.argv[1]
    port = int(sys.argv[2])
    start_server(ip_server, port)
