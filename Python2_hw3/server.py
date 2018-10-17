import json
from responses import get_server_response
from users import get_users
from config import get_server_socket

s = get_server_socket()
print("Server started")

client, addr = s.accept()
print(f"Client connected: {client} {addr}")

while True:
    print("Waiting for data")

    client_msg = json.loads(client.recv(10240).decode("utf-8"))
    print("Data received")

    if client_msg["action"] == "authenticate":
        data_users = get_users()

        username = client_msg["user"]["username"]
        password = client_msg["user"]["password"]

        if username not in data_users or password != data_users[username]:
            server_response = get_server_response("402")
        else:
            server_response = get_server_response("200")

        client.send(json.dumps(server_response).encode(server_response["encoding"]))
    elif client_msg["action"] == "quit":
        client.send(json.dumps(server_response).encode(server_response["encoding"]))

        client.close()
        s.close()
        server_response = get_server_response("200")

