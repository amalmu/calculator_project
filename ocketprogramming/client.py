import socket

def start_client(server_ip="192.168.0.114",server_port=8080):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((server_ip,server_port))
    
    try:
        while True:
            message=input("ENTER MESSAGE TO SEND: ")
            client.send(message.encode('utf-8'))

            response=client.recv(1024).decode('utf-8')
            print("Server response",response)

    except KeyboardInterrupt:
        print("CONNECTION HAS BEEN CLOSED")
    client.close()

if __name__=="__main__":
    start_client()


