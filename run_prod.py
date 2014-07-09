#!/usr/bin/python
'''Flask app runner for production'''

import os
from main import create_app

app = create_app()
app.config.from_object('config.Production')

if os.environ.get('HEROKU'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

if __name__ == '__main__':
    app.run()
