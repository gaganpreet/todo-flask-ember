from flask import Flask, Blueprint, render_template

api_app = Blueprint('api_app', __name__,
                    template_folder='templates')

