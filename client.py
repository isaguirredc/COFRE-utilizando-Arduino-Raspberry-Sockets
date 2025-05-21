import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.1.25.177', 5000))

    while True:
        message = input("Client: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            print("Connection closed by the client.")
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()