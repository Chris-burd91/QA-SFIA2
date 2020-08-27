#from application import db

class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    answer = db.Column(db.String(50))

    def__repr__(self):
        return " ".join(['Number:', self.number, 'Answer:', self.answer]