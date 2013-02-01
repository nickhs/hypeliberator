from app import db
from models import *

db.drop_all()
print "All tables dropped"
db.create_all()
print "All tables created"
