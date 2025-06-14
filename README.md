# Monitoramento de Atletas

Sistema simples em Python para coletar e analisar dados de atletas que retornaram de Tóquio, com armazenamento em JSON e banco de dados SQL.

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
  Arquivos JSON usados para persistência dos dados dos atletas

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
- SQLite / MySQL / PostgreSQL (escolha sua base e ajuste scripts)  
- SQL para criação e manipulação das tabelas  
- JSON para backup e exportação de dados
