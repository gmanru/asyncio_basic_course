"""Simple socker server"""

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # address type (host + port), protocol TCP
# todo check default params
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse port after stopping program
server_socket.bind(("127.0.0.1", 8020))
print("Start listening...")
server_socket.listen()  # start listening incoming connections - BLOCK PROGRAM!
print("Listening...")
client_socket, client_address = server_socket.accept()  # client socket and address data
print("Something happened!")
print(f"New connection from: {client_address}")
