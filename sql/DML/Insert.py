from data.model.ConectarSql import ConectarSql
from data.model.Atleta import Atleta
from data.model.Covid import Covid
from data.model.Medalhas import Medalhas

class Inserir:
    def inserir_tabelas(self, atleta: Atleta) -> None:

        with ConectarSql().conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO atletas(id, idade, sexo)
                VALUES (?, ?, ?);''',(
                    atleta.cpf,
                    atleta.idade,
                    atleta.sexo
                )
            )
            