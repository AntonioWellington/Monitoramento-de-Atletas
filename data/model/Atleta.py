from . import Covid
from . import Medalhas

class Atleta:
    def __init__(self, idade: int, sexo: str, cpf: str,
                ) -> None:
        self._idade = idade
        self._sexo = sexo
        self._cpf = cpf
        
    
    @property
    def idade(self) -> int:
        return self._idade
    
    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade
    
    @property
    def sexo(self) -> str:
        return self._sexo
        
    @sexo.setter
    def sexo(self, sexo: str) -> None:
        self._sexo = sexo

    @property
    def cpf(self) -> str:
        return self._cpf   
        
    @cpf.setter
    def cpf(self, cpf: str) -> None:
        self._cpf = cpf

    '''@property
    def covid(self) -> Covid:
        return self._covid'''
    
    '''@covid.setter
    def covid(self, covid: str) -> None:
        self._covid = covid

    @property
    def medalhas(self) -> Medalhas:
        return self._medalhas
    
    @medalhas.setter
    def medalhas(self, medalhas: str) -> None:
        self._medalhas = medalhas

    def transformar_em_dicionario(self) -> dict:  

        dicionario = {
            "cpf": self._cpf,
            "sexo": self._sexo,
            "idade": self._idade,
            "teve_febre": self._covid.teve_febre,
            "temperatura": self._covid.temperatura_corporal,
            "outro_sintoma": self._covid.outro_sintoma,
            "kit_covid": self._covid.kit_covid,
            "medalhas_ouro": self._medalhas.ouro,
            "medalhas_prata": self._medalhas.prata,
            "medalhas_bronze": self._medalhas.bronze
        }

        return dicionario'''