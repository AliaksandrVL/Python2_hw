import socket

ADDRES = 'localhost'
PORT= 7777

def get_client_socket():

    s = socket.socket()
    s.connect((ADDRES, PORT))

    return s

def get_server_socket():

    s = socket.socket()
    s.bind((ADDRES, PORT))
    s.listen(10)

    return s