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
        todos = Todo.query.all()
        todos = [todo.as_dict() for todo in todos]
        return todos

    def post(self):
        '''Create a new todo'''
        parser = reqparse.RequestParser()
        parser.add_argument('description', type=str, required=True)
        args = parser.parse_args()

        todo = Todo(args['description'])
        db.session.add(todo)
        db.session.commit()
        return todo


class TodoAPI(restful.Resource):
    def get(self, id):
        '''Get a specific todo'''
        todo = Todo.query.get(id)

        if not todo:
            restful.abort(404, message='Invalid todo')

        return todo.as_dict()

    def put(self, id):
        '''Update a specific todo (mark as completed)'''
        todo = Todo.query.get(id)

        if not todo:
            restful.abort(404, message='Invalid todo')

        todo.is_completed = True
        db.session.add(todo)
        db.commit(todo)
        return todo.as_dict()


api.add_resource(TodoAPI, '/todos/<int:id>')
api.add_resource(TodoListAPI, '/todos')
