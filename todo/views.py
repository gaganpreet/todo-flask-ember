from flask import Flask, Blueprint, send_file

root_app = Blueprint('root_app', __name__,
                    static_url_path='/todo',
                    static_folder='static',
                    template_folder='templates')

@root_app.route('/')
def home():
    return send_file('todo/templates/index.html')
