from flask_restful import fields

from helpers.database import db

uf_fields = {
    'id': fields.Integer,
    'sigla': fields.String,
    'nome': fields.String,
    'latitude': fields.Float,
    'longitude': fields.Float
}


class Uf(db.Model):
    __tablename__ = "uf"

    id = db.Column(db.Integer, primary_key=True)
    sigla = db.Column(db.String(2), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float(8), nullable=True)
    longitude = db.Column(db.Float(8), nullable=True)

    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla

    def __repr__(self):
        return f'<UF>'
