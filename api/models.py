from database import db


class Todo(db.Model):
    ''' Todo representation '''
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(512))

    is_completed = db.Column(db.Boolean, default=False)

    added_on = db.Column(db.DateTime,
                         default=db.func.now())

    last_update = db.Column(db.DateTime,
                            default=db.func.now(),
                            onupdate=db.func.now())

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<{0}>'.format(self.description)

    def as_dict(self):
        return {'id': self.id,
                'description': self.description,
                'is_completed': self.is_completed,
                'added_on': self.added_on.strftime('%s'),
                'last_update': self.last_update.strftime('%s')
                }
