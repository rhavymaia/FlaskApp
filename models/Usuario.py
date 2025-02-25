from helpers.database import db
from models.Endereco import Endereco

from typing import List
from typing import Optional
from sqlalchemy import String
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
