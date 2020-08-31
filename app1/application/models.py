from application import db

class _8Ball(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.String(50))
    answer = db.Column(db.String(50))

    def __repr__(self):
        return ' '.join(['Order:', self.order, 'Answer:', self.answer])