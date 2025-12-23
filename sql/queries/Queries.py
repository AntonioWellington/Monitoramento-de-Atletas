from data.model.ConectarSql import ConectarSql

class Queries:
    
    def quantidade_total_de_atletas_monitorados(self):
        with ConectarSql().conexao() as conexao:
            cursor = conexao.cursor() 
            cursor.execute('''
                SELECT COUNT(id) 
                FROM Atletas;
            ''')

            return cursor.fetchone()[0]

    def quantidade_e_porcentagem_de_atletas_com_sintomas(self):
        with ConectarSql().conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                SELECT 
                    SUM(teve_febre AND teve_outro_sintoma) AS quantidade_com_sintomas,
                    SUM(teve_febre AND teve_outro_sintoma) * 100.0 / (
                        SELECT COUNT(Atletas.id) FROM Atletas
                    ) AS porcentagem
                FROM Covid;
            ''')

            return cursor.fetchone()

    def idade_media_dos_atletas_dos_sintomaticos_e_assintomaticos(self):
        with ConectarSql().conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                SELECT 
                    AVG(Atletas.idade) AS idade_media_dos_atletas,
                    AVG(CASE 
                            WHEN Covid.teve_febre AND Covid.teve_outro_sintoma 
                            THEN Atletas.idade
                    END) AS media_com_sintomas,
                    AVG(CASE 
                            WHEN Covid.teve_febre = FALSE AND Covid.teve_outro_sintoma = FALSE
                            THEN Atletas.idade
                    END) AS media_sem_sintomas
                FROM Atletas
                JOIN Covid ON Atletas.id = Covid.id;
            ''')

            return cursor.fetchone()

    def temperatura_corporal_mais_alta_relatada(self):
        with ConectarSql().conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                SELECT MAX(temperatura_corporal)
                FROM Covid;
            ''')

            return cursor.fetchone()[0]

    def idade_do_atleta_mais_novo_e_mais_velho_entre_os_sintomaticos(self):
        with ConectarSql().conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                SELECT 
                    MAX(Atletas.idade), 
                    MIN(Atletas.idade)
                FROM Atletas
                JOIN Covid ON Atletas.id = Covid.id
                WHERE Covid.teve_febre = TRUE AND Covid.teve_outro_sintoma = TRUE;
            ''')
            
            return cursor.fetchone()

    def recorte_por_genero_kit_covid_sintomas(self):
        with ConectarSql().conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                SELECT Atletas.sexo,
                    SUM(CASE 
                        WHEN Atletas.sexo = 'F' 
                            AND Covid.teve_febre = FALSE 
                            AND Covid.teve_outro_sintoma = FALSE 
                            AND Covid.tomou_kit_covid
                        THEN 1 ELSE 0
                    END) AS mulheres_que_n_tiveram_sintomas_e_tomaram_kit_covid,
                    
                    SUM(CASE 
                        WHEN Atletas.sexo = 'F' 
                            AND Covid.teve_febre 
                            AND Covid.teve_outro_sintoma 
                            AND Covid.tomou_kit_covid
                        THEN 1 ELSE 0
                    END) AS mulheres_que_tiveram_sintomas_e_tomaram_kit_covid,
                    
                    SUM(CASE 
                        WHEN Atletas.sexo = 'M' 
                            AND Covid.teve_febre = FALSE 
                            AND Covid.teve_outro_sintoma = FALSE 
                            AND Covid.tomou_kit_covid
                        THEN 1 ELSE 0
                    END) AS homens_que_n_tiveram_sintomas_e_tomaram_kit_covid,
                    
                    SUM(CASE 
                        WHEN Atletas.sexo = 'M' 
                            AND Covid.teve_febre
                            AND Covid.teve_outro_sintoma 
                            AND Covid.tomou_kit_covid
                        THEN 1 ELSE 0
                    END) AS homens_que_tiveram_sintomas_e_tomaram_kit_covid
                FROM Atletas
                JOIN Covid ON Atletas.id = Covid.id
                GROUP BY Atletas.sexo;
            ''')

            return cursor.fetchall()


#Recorte por gênero e sintomas dos atletas que ganharam medalhas, com a quantidade de cada tipo de medalha

