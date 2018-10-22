import unittest
import threading
import socket
from config import *
import client, server, responses

class TestServer(unittest.TestCase):

    def test_read_data(self):
        t = threading.Thread(target=client.get_socket_and_waiting, daemon=True)
        t.start()

        s = socket.socket()
        s.bind((ADDRES, PORT))
        s.listen(10)
        s.settimeout(3)

        client_acc, addr_acc = s.accept()

        client_msg = {
            "action": "quit"
        }

        server.read_data(s, client_acc, client_msg)

    def read_data_authenticate(self):
        pass

    def read_data_quit(self):
        pass

    # def test_read_data(self):
    #     pass

if __name__ == '__main__':
    unittest.main()