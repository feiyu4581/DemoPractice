from utils.route import route
from utils.service import required_service
from sanic.response import json


@route('/car_brand/<id:int>')
@required_service('modelService')
class CarBrand:
    async def get(self, request, id):
        
        user = await self.modelService.get('user').get(id)
        return json({
            'dsf': user.nickname
        })

    async def post(self, request, id):
        user = await self.modelService.get('user').get(id)

        await user.update(**request.json).apply()
        return json({
            'msg': 'ok'
        })
