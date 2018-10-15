import time

def get_response_value():

    responses = {
        "100": "Continue",
        "101": "Switching Protocols",
        "200": "OK",
        "201": "Created",
        "202": "Accepted",
        "400": "Bad Request",
        "401": "Unauthorized",
        "402": "This could be 'wrong password' or 'no account with that name'",
        "403": "Forbidden",
        "404": "Not Found",
        "409": "Someone is already connected with the given user name",
        "410": "Gone",
        "500": "Internal Server Error"
    }

    return responses

def get_server_response(code):

    responses = get_response_value()

    data = {
        "response": code,
        "time": int(time.time()),
        "alert": responses[code],
        "encoding": "utf-8"
    }

    return data
