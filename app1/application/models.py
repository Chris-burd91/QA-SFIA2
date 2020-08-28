from application import db

class _8Ball(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    answer = db.Column(db.String(50))

    def __repr__(self):
        return ' '.join(['Number:', self.number, 'Answer:', self.answer])