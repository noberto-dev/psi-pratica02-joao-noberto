from typing import List

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    pais: Mapped[str] = mapped_column(nullable=False)
    livros: Mapped[list["Livro"]] = relationship(back_populates="autor")
    # TODO: relacione Autor com Livro usando relationship e back_populates.


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    autor : Mapped["Autor"] = relationship(back_populates="livros")
    disponivel: Mapped[bool] = mapped_column(default=True)
    # TODO: adicione o campo disponivel, com valor padrão True.
    # TODO: relacione Livro com Autor usando relationship e back_populates.
