
_service = {}

def register_service(name):
    def func(service):
        _service[name] = service()
        return service

    return func


def required_service(name):
    def func(model):
        setattr(model, name, _service[name])

        return model

    return func
