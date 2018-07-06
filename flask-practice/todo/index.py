# coding=utf-8

from flask import Flask, render_template, make_response
import config

app = Flask(__name__)

app.config.from_object(config)


@app.route('/nihao/<int:id>')
def hello_world(id=None):
    resp = make_response(render_template('main.html', name='Hello, World'))
    resp.set_cookie('UserName', 'CookieTest')

    return resp


if __name__ == '__main__':
    app.run(port=9000)
