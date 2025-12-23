from data.model.ConectarSql import ConectarSql

class Criar_tabela_covid:
    def criar_tabela(self):
        conexao = ConectarSql().conexao()
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS covid(
                id VARCHAR(14) NOT NULL,
                teve_febre VARCHAR(3) NOT NULL,
                temperatura_corporal FLOAT,
                teve_outro_sintoma VARCHAR(3),
                tomou_kit_covid VARCHAR(3) NOT NULL,

                CONSTRAINT idCovid PRIMARY KEY(id),
                
                CONSTRAINT idAtletaCovid FOREIGN KEY (id) REFERENCES atletas(id)
            );
            ''')
    
        conexao.commit()
        conexao.close()