from flask_restful import fields

from helpers.database import db

cidade_fields = {
    'codigo_ibge': fields.Integer,
    'nome': fields.String,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'capital': fields.Boolean,
    'codigo_uf': fields.Integer,
    'siafi_id': fields.String,
    'ddd': fields.Integer,
    'fuso_horario': fields.String,
}


class Cidade(db.Model):
    __tablename__ = "cidade"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float(8), nullable=True)
    longitude = db.Column(db.Float(8), nullable=True)

    endereco = db.relationship("Endereco", uselist=False, backref="cidade")

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f'<Cidade>'
