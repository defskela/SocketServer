from register import views


def router(url):
    if url:
        if url in views.keys():
            return views[url]
    return None
