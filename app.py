from router import router


def app(request):
    func = router(request['url'])
    if func is None:
        return b'HTTP/1.1 404 Not Found\n\n'
    return func(request)