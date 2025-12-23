from ConectarSql import ConectarSql

class Consultas:
    def inserir(self):
        conexao = ConectarSql("monitoramento_atletas.db")
        co = conexao.conexao()           # 'co' é a conexão
        cursor = co.cursor()             # cria cursor a partir da conexão
        
        # Use '?' para parâmetros no SQLite
        cursor.execute("INSERT INTO atletas(cpf, idade, sexo) VALUES (?, ?, ?)", 
                       (123, 2, 'f'))
        cursor.execute("INSERT INTO covid(id, teve_febre, tomou_kit_covid) VALUES (?, ?, ?)", 
                       (123, 'Não', 'Sim'))
        cursor.execute("INSERT INTO medalhas(id, ouro, prata, bronze) VALUES (?, ?, ?, ?)", 
                       (123, 0, 0, 0))
        
        co.commit()                     # confirma as mudanças no banco
        cursor.close()
        co.close()
