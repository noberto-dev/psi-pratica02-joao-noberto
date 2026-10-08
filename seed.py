from models import Autor, Livro


def popular_banco(session):
    user1 = Autor(nome="P.H. Medeiros",pais = "Japão")
    user2 = Autor(nome="Jeizon Gomes da Silva Filho",pais = "Estados Unidos")
    user2 = Autor(nome="Pedroca Machado",pais = "Rússia")

    livros = [
        Livro(titulo="Vendedor de Sonhos", ano=2026, autor=user1, autor_id=user2.id, disponivel=True),
        Livro(titulo="Primeira Análise de Jesus Cristo", ano=-2000, autor=user1, autor_id=user1.id, disponivel=True),
        Livro(titulo="Tsunami: A Revanche", ano=2020, autor=user1, autor_id=user1.id, disponivel=True),
        Livro(titulo="GPT 5: Como se tornar o Mestre da IA", ano=2028, autor_id=user2.id, autor=user2, disponivel=True),
        Livro(titulo="IA: O Domínio", ano=2030, autor=user2, autor_id=user2.id,disponivel=False),
        Livro(titulo="Do lixo ao domínio: Inteligencias Artificiais", ano=2027, autor_id=user2.id, autor=user2, disponivel=False)
    ]
    for l in livros:
        session.add(l)

    session.add_all([user1, user2])
    session.commit()