# TCP server client application

This TCP application consists of a server and a client that can send and receive messages. The server listens for incoming connections and the client connects to the server and sends messages.

To start the server, run for example:
```sh
python server.py 'localhost' 8080
```

To start the client, run for example:
```sh
python client.py 'localhost' 'localhost' 8080 10
```

## Parameters

- **ip_server**: IP address of the server (e.g., `'localhost'`).
- **ip_client**: IP address of the client (e.g., `'localhost'`).
- **port**: Port number to connect to (e.g., `8080`).
- **packet_size**: Size of each packet to send (e.g., `10`).
