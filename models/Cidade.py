from flask_restful import fields
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from helpers.database import db


cidade_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'latitude': fields.Float,
    'longitude': fields.Float
}


class Cidade(db.Model):
    __tablename__ = "cidade"

    id = mapped_column(Integer, primary_key=True, nullable=False)
    nome = mapped_column(String(100), nullable=False)
    latitude = mapped_column(Float(8), nullable=True)
    longitude = mapped_column(Float(8), nullable=True)

    uf_id: Mapped[int] = mapped_column(ForeignKey("uf.id"))
    uf = relationship("Uf", uselist=False)

    def __init__(self, nome, uf_id):
        self.nome = nome
        self.uf_id = uf_id

    def __repr__(self):
        return f'<Cidade>'
