from utils.service import register_service
from utils.model import get_model 


@register_service('modelService')
class ModelService:
    def get(self, name):
        return get_model(name)
