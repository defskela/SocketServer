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