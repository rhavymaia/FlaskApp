import psycopg2
from flask import g
from helpers.application import app

DATABASE = 'agricolaif.db'


def getConnection():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = psycopg2.connect(database="agriculaif",
                                            user="postgres",
                                            password="123456",
                                            host="localhost",
                                            port="5434")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
