import json
import time
from config import get_client_socket

AUTHORIZED = False

def send_data(s):

    if not AUTHORIZED:
        client_msg = {
            "action": "authenticate",
            "time": int(time.time()),
            "encoding": "utf-8",
            "user": {
                "username": input("User name: "),
                "password": int(input("Password: "))
            }
        }
    else:
        action = input("Action: ")

        if action == "quit":
            client_msg = {
                "action": f"{action}",
                "time": int(time.time()),
                "encoding": "utf-8"
            }
            s.send(json.dumps(client_msg).encode(client_msg["encoding"]))
            exit()

    s.send(json.dumps(client_msg).encode(client_msg["encoding"]))

if __name__ == "__main__":
    s = get_client_socket()

    while True:
        send_data(s)

        server_response = json.loads(s.recv(10240).decode("utf-8"))

        if not AUTHORIZED and server_response["response"] == "200":
            AUTHORIZED = True

        print(server_response["alert"])