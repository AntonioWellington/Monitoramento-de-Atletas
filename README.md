# Monitoramento de Atletas

Sistema simples em Python para coletar, armazenar e analisar dados de atletas que retornaram de Tóquio, com persistência em JSON e banco de dados SQL.

---

## 📋 Funcionalidades

- Coleta os seguintes dados para cada atleta:
  - Idade e sexo
  - Se teve febre
  - Se teve febre, a temperatura corporal mais alta desde o retorno
  - Se não teve febre, se apresentou outro sintoma (sim/não)
  - Se tomou o “kit COVID” ao retornar ao Brasil
  - Quantidade e tipo de medalhas (ouro, prata, bronze)

- Gera relatório com as seguintes informações:
  1. Quantidade total de atletas monitorados
  2. Quantidade e porcentagem de atletas com sintomas
  3. Idade média dos atletas, dos sintomáticos e dos assintomáticos
  4. Temperatura corporal mais alta relatada
  5. Idade do atleta mais novo e mais velho entre os sintomáticos
  6. Recorte por gênero dos atletas que tomaram o kit COVID, indicando quantos tiveram ou não sintomas
  7. Recorte por gênero e sintomas dos atletas que ganharam medalhas, com a quantidade de cada tipo de medalha

---

## 📂 Organização do Projeto

- `/sql/ddl/`  
  Arquivos de definição do banco (CREATE TABLE, constraints)

- `/sql/dml/`  
  Arquivos de manipulação de dados (INSERT, UPDATE, DELETE)

- `/sql/queries/`  
  Arquivos com consultas SQL para gerar relatórios e análises

- `/data/`  
  Pasta principal com a estrutura MVC para o sistema:  
  - `/model/` — definição das classes e estruturas de dados (ex: Atleta, Covid, Medalhas)  
  - `/controller/` — tratamento das entradas, lógica de negócio e manipulação dos dados (entrada de dados via código ou leitura de arquivos)  
  - `/view/` — responsável pela exibição dos resultados e relatórios via prints no terminal (saída)

- `main.py`  
  Script principal em Python para execução do sistema

- `README.md`  
  Documentação do projeto

---

## 🚀 Como executar

1. Certifique-se de ter Python 3.x instalado  
2. Configure seu banco de dados e execute os scripts SQL na ordem:  
   - `/sql/ddl/*.sql` (criação das tabelas)  
   - `/sql/dml/*.sql` (inserção inicial de dados, se houver)  
3. Execute o programa:  
   ```bash
   python main.py

---

## 🛠️ Tecnologias utilizadas

- Python 3.x  
- Biblioteca padrão do Python para manipulação de JSON (`json`)  
- Banco de dados relacional (SQLite, MySQL ou PostgreSQL) para armazenamento e consulta dos dados  
- SQL para criação, manipulação e consulta das tabelas via scripts `.sql`  
- Consulta e manipulação dos dados via Python, usando:  
  - ORM (ex: SQLAlchemy) **ou**  
  - Execução direta de queries SQL usando bibliotecas como `sqlite3`, `mysql-connector-python` ou `psycopg2`  
- Estrutura MVC para organização do código com:  
  - Model (classes e dados)  
  - Controller (lógica de negócio e manipulação)  
  - View (exibição no terminal via prints)  
- JSON para backup, exportação e manipulação local dos dados  
