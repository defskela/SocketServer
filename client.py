import socket


def main():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local machine name
    host = '127.0.0.1'

    # Reserve a port for your service
    PORT = 8081

    # Connection to hostname on the port
    sock.connect((host, PORT))
    sock1.connect((host, PORT))

    # Send a message to the server
    sock.send('GET /start HTTP1.1\r\n\r\n'.encode())
    sock1.send('GET /start HTTP1.1\r\n\r\n'.encode())

    # Close the connection
    sock.close()
    sock1.close()

if __name__ == "__main__":
    main()