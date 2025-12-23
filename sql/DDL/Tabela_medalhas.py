from data.model.ConectarSql import ConectarSql

class Criar_tabela_medalhas:
    def criar_tabela(self):
        conexao = ConectarSql().conexao()
        cursor = conexao.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medalhas(
                id VARCHAR(14) NOT NULL,
                ouro INT,
                prata INT,
                bronze INT,

                CONSTRAINT idMedalhas PRIMARY KEY(id),
                
                CONSTRAINT idAtletaMedalhas FOREIGN KEY (id) REFERENCES atletas(id)
            );
            ''')
                
        conexao.commit()
        conexao.close()