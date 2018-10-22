import json
from responses import get_server_response
from users import get_users
from config import get_server_socket

def read_data_authenticate(client, client_msg):

    data_users = get_users()

    username = client_msg["user"]["username"]
    password = client_msg["user"]["password"]

    if username not in data_users or password != data_users[username]:
        server_response = get_server_response("402")
    else:
        server_response = get_server_response("200")

        add_response = {
            "username": username
        }
        server_response.update(add_response)

    client.send(json.dumps(server_response).encode(server_response["encoding"]))

def read_data_quit(s, client, client_msg):

    server_response = get_server_response("200")
    client.send(json.dumps(server_response).encode(server_response["encoding"]))

    client.close()
    s.close()

def read_data(s, client, client_msg):

    if client_msg["action"] == "authenticate":
        read_data_authenticate(client, client_msg)
    elif client_msg["action"] == "quit":
        read_data_quit(s, client, client_msg)

def get_socket_and_waiting():

    s = get_server_socket()
    print("Server started")

    client, addr = s.accept()
    print(f"Client connected: {client} {addr}")

    while True:
        print("Waiting for data")

        client_msg = json.loads(client.recv(10240).decode("utf-8"))
        print("Data received")

        read_data(s, client, client_msg)


if __name__ == "__main__":
    get_socket_and_waiting()



