from helpers.application import app
from helpers.api import api
from helpers.cors import cors
from helpers.database import db


cors.init_app(app)
api.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# requests
# sqlalchemy
