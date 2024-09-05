import socket

def handleClient(client_socket):
    while True:
        try:
            message = client_socket.recv(1024). decode('utf-8')
            if not message:
                break
            print(f"Recived {message}")
            response= f'Message Recived :{message}'
            client_socket.send(response.encode('utf-8'))
        except ConnectionResetError:
            break

host = '0.0.0.0'
port = 8080
def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"SERVER LISTENING TO PORT : {port}")

    while True:
        client_socket, addr = server.accept()
        print(f"CONNECTION ESTABLISHED WITH {addr}")

        handleClient(client_socket) 

if __name__ == "__main__":
    start_server(host, port)