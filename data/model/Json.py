import json
from pathlib import Path


class Json:
    def __init__(self, dados: dict) -> None:
        self._arquivo = "dados.json"
        self._dados = dados

    @property
    def dados(self) -> dict:
        return self._dados
    
    @dados.setter
    def dados(self, dados: dict) -> None:
        self._dados = dados

    def atualizar(self, cpf: str, atributo: str, novo_dado: str) -> None:
        self._dados[cpf][atributo] = novo_dado
    
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

        salvar[self._dados["cpf"]] = self._dados

        with open(self._arquivo, 'w', encoding='utf-8') as dados:
            json.dump(salvar, dados, indent=4)