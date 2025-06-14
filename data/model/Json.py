import json, re, Atleta
from pathlib import Path

class Json:
    def __init__(self, arquivo: str) -> None:
        self._arquivo = arquivo

    @property
    def dados(self) -> dict:
        return self._dados
    
    def atualizar(self, atributo: str, novo_dado: str) -> None:
        self.dados[cpf][atributo] = novo_dado
    
    def abrir(self) -> None:
        self._arquivo = Path(self._arquivo)
        if self._arquivo.exists():
            with open(self._arquivo, 'r', encoding='utf-8') as dados:
                dados = json.load(dados)
            return dados
        else:
            return {}

    def gravar_dados(self) -> None:
        
        salvar = self.abrir()

        salvar[Atleta.Atleta.cpf] = {
            "idade": Atleta.Atleta.idade,
            "sexo": Atleta.Atleta.sexo,
            "cpf": Atleta.Atleta.cpf,
            "teve_febre": Atleta.Atleta.teve_febre,
            "temperatura_corporal": Atleta.Atleta.temperatura_corporal,
            "outro_sintoma": Atleta.Atleta.outro_sintoma,
            "kit_covid": Atleta.Atleta.kit_covid,
            "ouro": Atleta.Atleta.ouro,
            "bronze": Atleta.Atleta.bronze,
            "prata": Atleta.Atleta.prata
        }
        with open(self._arquivo, 'w', encoding='utf-8') as dados:
            json.dump(salvar, dados, indent=4)