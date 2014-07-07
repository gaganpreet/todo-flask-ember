from main import create_app
from database import db
from api.models import Todo

app = create_app()
app.config.from_object('config.Config')

with app.test_request_context():
    db.create_all()
