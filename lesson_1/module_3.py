"""Simple socket server with infinite listening"""

import socket
host = '127.0.0.1'
port = 8020

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        try:
            print(f"Connected by {client_address}")
            while True:
                data = client_socket.recv(1)
                if not data:
                    break
                print(f"Received data: {data.decode()}")
                client_socket.sendall(b'success')
        except ConnectionResetError:
            print(f"Connection reset by {client_address}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print(f"Closing connection to {client_address}")
            client_socket.close()
