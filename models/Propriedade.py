from marshmallow import Schema, fields, validate

from helpers.database import db
from sqlalchemy.orm import Mapped, mapped_column

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

propriedade_fields = {
    'nome': fields.String,
    'cidade': fields.String,
}


class Propriedade(db.Model):

    __tablename__ = "propriedade"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    posicao_id: Mapped[int] = mapped_column(ForeignKey("posicao.id"))
    endereco_id: Mapped[int] = mapped_column(ForeignKey("endereco.id"))
    proprietario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))

    def __init__(self, nome, cidade) -> None:
        self.nome = nome
        self.cidade = cidade

    def __repr__(self) -> str:
        return f"<Propriedade: {self.nome}, {self.cidade}>"

    def getNome(self):
        return self.nome

    def toJson(self):
        return {'nome': self.nome, 'cidade': self.cidade}


class PropriedadeSchema(Schema):
    nome = fields.String(validate=validate.Length(min=2, max=50),
                         required=True, error_messages={"required": "Nome é obrigatório."})
    cidade = fields.String(required=True)


class Posicao(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    latitude = db.Column(db.Float(8), nullable=False)
    longitude = db.Column(db.Float(8), nullable=False)

    def __init__(self):
        pass
