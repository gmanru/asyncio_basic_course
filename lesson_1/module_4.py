"""Simple socket ping-sender client with reading response from server"""

import socket

host = '127.0.0.1'
port = 8020

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        message = "ping"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")

        response = client_socket.recv(1024)
        print(f"Received: {response.decode('utf-8')}")

    except Exception as e:
        print(f"An error occurred: {e}")
