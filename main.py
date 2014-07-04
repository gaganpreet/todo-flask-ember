#!/usr/bin/python
'''Skeleton Flask app'''

from flask import Flask
from todo.views import root_app
from api.views import api_app

app = Flask(__name__)
app.config.from_object('config.Development')
app.register_blueprint(root_app)
app.register_blueprint(api_app)

if __name__ == '__main__':
    app.run()
