from sanic import Sanic
from sanic.exceptions import abort
from sanic.response import json
from gino.ext.sanic import Gino

app = Sanic()
app.config.DB_HOST = 'localhost'
app.config.DB_DATABASE = 'dl'
app.config.DB_USER = 'zhengxiang'
db = Gino()
db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger(), primary_key=True)
    nickname = db.Column(db.Unicode())

    def __repr__(self):
        return '{}<{}>'.format(self.nickname, self.id)


@app.route("/users/<user_id>")
async def get_user(request, user_id):
    if not user_id.isdigit():
        abort(400, 'invalid user id')
    user = await User.get_or_404(int(user_id))
    return json({'name': user.nickname})


if __name__ == '__main__':
    app.run(debug=True)