from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    statement = select(Livro).where(Livro.titulo.like(f"%{titulo}%"))
    livro = session.scalars(statement).first()

    if not livro:
            return print("Livro não encontrado")
    print(f"""
        TITULO : {livro.titulo} \n
        ANO : {livro.ano} \n
        AUTOR : {livro.autor.nome} \n
    """)

    if not livro.disponivel:
        return print("Livro não disponível")

    livro.disponivel = False
    session.commit()
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver indisponível, exiba uma mensagem.
    # TODO: se estiver disponível, altere disponivel para False e faça commit.

def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    statement = select(Livro).where(Livro.titulo.like(f"%{titulo}%"))
    livro = session.scalars(statement).first()

    if not livro:
        return print("Livro não encontrado")
    
    print(f"""
        TITULO : {livro.titulo} \n
        ANO : {livro.ano} \n
        AUTOR : {livro.autor.nome} \n
    """)

    if livro.disponivel:
        return print("Este livro já está disponível")

    livro.disponivel = True
    session.commit()
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver disponível, exiba uma mensagem.
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.
    pass
