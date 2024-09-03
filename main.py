import socket
import threading
from time import sleep

from app import app
from HttpRequest import HttpRequest
from register import paths


def handle_client(con, addr):
    
    print('Got connection from', addr)
    try:
        
        # получаем строчку из браузера - request
        msg = con.recv(1024)

        if msg:
            # преобразуем строчку в объект HttpRequest, который имеет словарь request
            obj = HttpRequest(msg.decode('utf-8'))
            # print(obj.request)

            response = app(obj.request)
            sleep(3)
            con.send(response)
    finally:
        con.close()
        print('Connection with', addr, 'closed') 


def main():
    print('Start')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    print('Host:', host)

    PORT = 8081

    sock.bind((host, PORT))

    print('Bound to port', PORT)

    sock.listen(5)
    # добавляем обработчики роутов
    paths()


    while True:
        con, addr = sock.accept()
        # Создание нового потока для каждого соединения
        client_thread = threading.Thread(target=handle_client, args=(con, addr))
        client_thread.start()

        print('End')

if __name__ == "__main__":
    main()
