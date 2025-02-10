from helpers.application import app
from helpers.api import api
from helpers.cors import cors

cors.init_app(app)
api.init_app(app)

# requests
# sqlalchemy
