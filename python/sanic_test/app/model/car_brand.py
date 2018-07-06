from app import db
from utils.model import Resource, register_model


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger(), primary_key=True)
    nickname = db.Column(db.Unicode())

    def __repr__(self):
        return '{}<{}>'.format(self.nickname, self.id)


@register_model('user')
class UserModel(Resource):
    _model = User

    async def get_list(self):
        user = await self._model.get(1)

        return user
