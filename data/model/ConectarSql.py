import sqlite3

class ConectarSql:

    def __init__(self, nome_do_BD = "monitoramento_de_atletas.db") -> None:
        self.nome_do_BD = nome_do_BD

    def conexao(self):
       return sqlite3.connect(self.nome_do_BD)