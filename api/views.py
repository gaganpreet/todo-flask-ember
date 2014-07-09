from flask.ext import restful
from flask.ext.restful import reqparse
from flask import Blueprint
from api.models import Todo
from database import db

api_app = Blueprint('api_app', __name__, url_prefix='/api')
api = restful.Api(api_app)


class TodoListAPI(restful.Resource):
    def get(self):
        '''Get list of all todos'''
        todos = Todo.query.order_by(Todo.last_update.desc()).all()
        todos = [todo.as_json() for todo in todos]
        return {'todos': todos}

    def post(self):
        '''Create a new todo'''
        parser = reqparse.RequestParser()
        parser.add_argument('todo', type=dict, required=True)
        args = parser.parse_args()

        if args['todo']['description']:
            todo = Todo(args['todo']['description'])
            db.session.add(todo)
            db.session.commit()
            return {'todo': todo.as_json()}
        restful.abort(400, message='Missing description')


class TodoAPI(restful.Resource):
    def get(self, id):
        '''Get a specific todo'''
        todo = Todo.query.get(id)

        if not todo:
            restful.abort(404, message='Invalid todo')

        return {'todo': todo.as_json()}

    def put(self, id):
        '''Update a specific todo'''
        todo = Todo.query.get(id)

        if not todo:
            restful.abort(404, message='Invalid todo')

        parser = reqparse.RequestParser()
        parser.add_argument('todo', type=dict, required=True)
        args = parser.parse_args()

        try:
            todo.description = args['todo']['description']
            todo.is_completed = args['todo']['isCompleted']
        except:
            restful.session.abort(400)

        db.session.add(todo)
        db.session.commit()
        return {'todo': todo.as_json()}

    def delete(self, id):
        '''Delete a todo'''
        todo = Todo.query.get(id)
        if not todo:
            restful.abort(404, message='Invalid todo')

        db.session.delete(todo)
        db.session.commit()


api.add_resource(TodoAPI, '/todos/<int:id>')
api.add_resource(TodoListAPI, '/todos')
