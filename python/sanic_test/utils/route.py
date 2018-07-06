
_route_maps = {}

def route(url):
    def func(obj):
        _route_maps[url] = obj()
        
        return obj

    return func


route_attributes = [
    'get',
    'post',
    'delete',
    'put'
]


def register_route(app):
    for url, model in _route_maps.items():
        for attribute in route_attributes:
            try:
                handle = getattr(model, attribute)
            except AttributeError:
                continue

            app.add_route(handle, url, methods=[attribute.upper()])
