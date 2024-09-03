from views import *

views = {}


def register(url, vie):
    # создаем словарь, где ключ - url, значение - указатель на функцию
    views[url] = vie


def paths():
    register('/start', start)
    register('/method', meth)
    register('/body', body)