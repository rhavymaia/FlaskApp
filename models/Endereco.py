from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from helpers.database import db
from models.Usuario import Usuario
from models.Cidade import Cidade


class Endereco(db.Model):
    __tablename__ = "endereco"

    id: Mapped[int] = mapped_column(primary_key=True)
    logradouro: Mapped[str] = mapped_column(String)
    cep: Mapped[str] = mapped_column(String(8))
    numero: Mapped[int] = mapped_column(Integer)
    bairro: Mapped[str] = mapped_column(String)

    cidade_id: Mapped[int] = mapped_column(ForeignKey("cidade.id"))
    cidade: Mapped["Cidade"] = relationship("Cidade", uselist=False)

    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    usuario: Mapped["Usuario"] = relationship(back_populates="endereco")

    def __init__(self, logradouro, numero, bairro, cidade_id, usuario_id):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade_id = cidade_id
        self.usuario_id = usuario_id

    def __repr__(self) -> str:
        return f"Address(logradouro={self.logradouro})"
