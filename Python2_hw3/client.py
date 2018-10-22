import json
import time
from config import get_client_socket

USERNAME = ""

def send_data_authenticate(s, client_msg):

    add_msg = {
        "user": {
            "username": input("User name: "),
            "password": int(input("Password: "))
        }
    }

    client_msg.update(add_msg)
    s.send(json.dumps(client_msg).encode(client_msg["encoding"]))

def send_data_msg(s, client_msg):

    add_msg = {
        "user": {
            "to": input("To: "),
            "from": USERNAME,
            "message": input("Message: ")
        }
    }

    client_msg.update(add_msg)
    s.send(json.dumps(client_msg).encode(client_msg["encoding"]))

def send_data_quit(s, client_msg):
    s.send(json.dumps(client_msg).encode(client_msg["encoding"]))
    exit()

def send_client_msg(s, action):

    client_msg = {
        "action": f"{action}",
        "time": int(time.time()),
        "encoding": "utf-8",
    }

    if action == "authenticate":
        send_data_authenticate(s, client_msg)
    elif action == "msg":
        send_data_msg(s, client_msg)
    elif action == "quit":
        send_data_quit(s, client_msg)

def send_data(s):

    if USERNAME == "":
        send_client_msg(s, "authenticate")
    else:
        action = input("Action: ")
        send_client_msg(s, action)

def get_socket_and_waiting():

    s = get_client_socket()

    while True:
        send_data(s)

        server_response = json.loads(s.recv(10240).decode("utf-8"))

        if USERNAME == "" and server_response["response"] == "200":
            USERNAME = server_response["username"]

        print(server_response["alert"])

if __name__ == "__main__":
    get_socket_and_waiting()