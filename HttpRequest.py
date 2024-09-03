class HttpRequest:

    @staticmethod
    def parse_request(request):
        data = {}

        # Разделяем запрос на строки

        body = request.split('\r\n\r\n')[1]
        data['body'] = body
        lines = request.split('\r\n')

        # Первая строка - это стартовая строка с методом, URL и HTTP-версией
        data['method'], data['url'], data['http_version'] = lines[0].split()

        # Заголовки идут после стартовой строки, до пустой строки (которая разделяет заголовки и тело)
        headers = {}
        for line in lines[1:]:
            if line == '':
                break
            header, value = line.split(': ', 1)
            headers[header] = value

        data['headers'] = headers

        return data

    def __init__(self, request):
        self.request = HttpRequest.parse_request(request)
