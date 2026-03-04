import socket
import threading
import random

nickname = input("Choose your nickname before joining server: ")

# defining a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this is the ip of the server that we want to connect to
client.connect(('127.0.0.1', 55556))


def receive():
    # always tries to receive data from the server
    while True:
        try:
            # receiving from the server
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))

            else:
                print(message)

        except:
            (print("An error occurred!"))
            client.close()
            break


def sending():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


# we are running 2 threads receive thread and the write thread

# the thread for receiving
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# the thread for sending
write_thread = threading.Thread(target=sending)
write_thread.start()
