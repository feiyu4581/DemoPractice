
_model_maps = {}

def register_model(name):
    def func(model):
        _model_maps[name] = model()
        return model

    return func


def get_model(name):
    return _model_maps[name]


class Resource:
    _model = None

    def __getattr__(self, name):
        if self._model:
            return getattr(self._model, name)

        raise AttributeError('model does not exists')

