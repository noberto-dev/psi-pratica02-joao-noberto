from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from models import Autor, Livro

def listar_livros(session):
    statement = select(Livro).options(joinedload(Livro.autor))
    livros = session.scalars(statement).all()

    for l in livros:
        print(f"""
            TITULO : {l.titulo} \n
            ANO : {l.ano} \n
            AUTOR : {l.autor.nome} \n
            DISPONÍVEL {"Sim" if l.disponivel else "Não"}
        """)
    
def listar_livros_por_autor(session, nome_autor):
    statement = select(Autor).where(Autor.nome.like(f"%{nome_autor}%")).options(selectinload(Autor.livros))
    autor = session.scalars(statement).first()
    
    for l in autor.livros:
        print(f"""
            TITULO : {l.titulo} \n
            ANO : {l.ano} \n
            AUTOR : {l.autor.nome} \n
        """)


def listar_livros_disponiveis(session):
    statement = select(Livro).where(Livro.disponivel == True).options(joinedload(Livro.autor))
    livros = session.scalars(statement).all()

    for l in livros:
        print(f"""
            TITULO : {l.titulo} \n
            ANO : {l.ano} \n
            AUTOR : {l.autor.nome} \n
        """)


def buscar_livros_por_titulo(session, trecho):
    statement = select(Livro).where(Livro.titulo.like(f"%{trecho}%"))
    livros = session.scalars(statement).all()
    
    for l in livros:
        print(f"""
            TITULO : {l.titulo} \n
            ANO : {l.ano} \n
            AUTOR : {l.autor.nome} \n
        """)
