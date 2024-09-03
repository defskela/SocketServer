import json
import sqlite3


def start(request):
    html = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Start</h1>
        </body>
        </html>'''
    response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                f"Content-Length: {len(html.encode('utf-8'))}\r\n"
                "\r\n" + html
            )
    return response.encode('utf-8')  # Преобразуем весь ответ в байты


def meth(request):
    html = f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Method: {request['method']}</h1>
        </body>
        </html>'''
    response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                f"Content-Length: {len(html.encode('utf-8'))}\r\n"
                "\r\n" + html
            )
    return response.encode('utf-8')  # Преобразуем весь ответ в байты

def body(request):
    response_body = b"Response to POST request"
    response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: " + str(len(response_body)).encode('utf-8') + b"\r\n\r\n" + response_body
    return response


def create_dog(request):
    json_request = json.loads(request['body'])

    name, age = json_request['name'], json_request['age']
    conn = sqlite3.connect('dogs.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dogs (name, age) VALUES (?, ?)', (name, age))

    conn.commit()
    cursor.execute('SELECT * FROM dogs ORDER BY id DESC LIMIT 1')
    last_record = cursor.fetchone()

    conn.close()

    response_body = json.dumps({
        'id': last_record[0],
        'name': last_record[1],
        'age': last_record[2]
    }).encode('utf-8')

    return b"HTTP/1.1 201 CREATED\r\nContent-Type: application/json\r\nContent-Length: " + str(len(response_body)).encode('utf-8') + b"\r\n\r\n" + response_body


def edit_dog(request):
    if request['method'] == 'PUT':
        pass