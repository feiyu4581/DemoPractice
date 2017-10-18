# coding=utf-8
# from __future__ import absolute_import

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import eventlet
import time
import simplejson

eventlet.monkey_patch()

app = Flask(__name__)
app.config['secret'] = 'Secret!'
app.config['debug'] = True

socketio = SocketIO(app, async_mode='eventlet')

@app.route('/<namespace>')
def main(namespace):
    # return 'Task Complete'

    print namespace
    return render_template('index.html', namespace=namespace)

@socketio.on('message1', namespace='/1')
def message(message):
    print '----------------------{}---------------'.format(message)

    emit('message2', 'Received: ' + message, namespace='/1', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    # app.run(debug=True)

