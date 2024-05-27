"""
Client module for sending traffic to a server.

Usage:
    python client.py <ip_server> <ip_client> <port> <packet_size>

Arguments:
    ip_server: IP address of the server, can be localhost
    ip_client: IP address of the client
    port: Port number to connect to
    packet_size: Size of each packet to send

Functions:
    start_client(ip_server, ip_client, port, packet_size): Starts the client to send messages to the server.
"""

import socket
import sys


def start_client(ip_server, ip_client, port, packet_size):
    """
    Client side. Sends a message.

    :param ip_server: IP address of the server, can be localhost
    :param ip_client: IP address of the client
    :param port: Port number to connect to
    :param packet_size: Size of each packet to send
    :return: None
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip_client, 0))
    server_address = (ip_server, port)
    print(f'connecting to port {server_address}')
    sock.connect(server_address)

    try:
        message = "this is the message. It will be repeated."
        for i in range(0, len(message), packet_size):
            print(f'sending {message[i: i + packet_size]}')
            sock.sendall(message[i: i + packet_size].encode())

    finally:
        print('closing socket')
        sock.close()


if __name__ == '__main__':
    ip_server = sys.argv[1]
    ip_client = sys.argv[2]
    port = int(sys.argv[3])
    packet_size = int(sys.argv[4])
    start_client(ip_server, ip_client, port, packet_size)
