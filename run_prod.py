#!/usr/bin/python
'''Flask app runner for production'''

from main import create_app

app = create_app()
app.config.from_object('config.Production')

if __name__ == '__main__':
    app.run()
