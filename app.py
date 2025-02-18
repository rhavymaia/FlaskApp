from models.Usuario import User
from helpers.application import app
from helpers.api import api
from helpers.cors import cors
from helpers.database import db


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123456@localhost:5434/agriculaif"


cors.init_app(app)
api.init_app(app)
db.init_app(app)

user = User()

with app.app_context():
    db.create_all()

# requests
# sqlalchemy
