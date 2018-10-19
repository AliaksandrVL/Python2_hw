import sqlite3

def get_users():

    connection = sqlite3.connect('messenger.db')
    cur = connection.cursor()
    cur.execute('SELECT ')
    users = {
        "Admin": 123456
    }

    return users