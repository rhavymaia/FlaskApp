from helpers.database import db
from sqlalchemy.orm import Mapped, mapped_column

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Usuario(db.Model):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    sobrenome: Mapped[Optional[str]] = mapped_column(String)

    endereco: Mapped[List["Endereco"]] = relationship(
        back_populates="usuario", cascade="all, delete-orphan"
    )

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __repr__(self) -> str:
        return f"Usuario(nome={self.nome}, sobrenome={self.sobrenome})"


class Endereco(db.Model):
    __tablename__ = "endereco"

    id: Mapped[int] = mapped_column(primary_key=True)
    logradouro: Mapped[str] = mapped_column(String)
    cep: Mapped[str] = mapped_column(String(8))
    numero: Mapped[int] = mapped_column(Integer)
    bairro: Mapped[str] = mapped_column(String)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))

    usuario: Mapped["Usuario"] = relationship(back_populates="endereco")

    def __init__(self, logradouro, numero, bairro, usuario_id):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.usuario_id = usuario_id

    def __repr__(self) -> str:
        return f"Address(logradouro={self.logradouro})"
