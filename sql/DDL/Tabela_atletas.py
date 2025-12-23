from data.model.ConectarSql import ConectarSql

class Criar_tabela_atletas:
    def criar_tabela(self):
        conexao = ConectarSql().conexao()
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS atletas(
                id VARCHAR(14) NOT NULL,
                sexo VARCHAR(1) NOT NULL,
                idade INT NOT NULL,
                CONSTRAINT idAtleta PRIMARY KEY(id) 
            );
            ''')
    
        conexao.commit()
        conexao.close()
