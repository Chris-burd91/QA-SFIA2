from application import db
from application.models import _8Ball

db.drop_all
db.create_all()