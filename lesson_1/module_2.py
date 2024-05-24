"""Simple socket client"""

# import socket
#
# i = 0
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('localhost', 8020))
# while True:
#     s.sendall("ping".encode("utf-8"))
#     i += 1
#     if i == 2:
#         raise Exception
# s.close()


import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8020))
s.sendall("ping".encode("utf-8"))
s.close()
