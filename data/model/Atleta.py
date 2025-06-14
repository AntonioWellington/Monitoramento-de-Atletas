
import Covid
import Medalhas
import Json

class Atleta:
    def __init__(self, idade: int, sexo: str, cpf: str,
                teve_febre: bool, temperatura_corporal: float, outro_sintoma: bool, kit_covid: bool, 
                ouro: int, bronze: int, prata: int) -> None:
        self._idade = idade
        self._sexo = sexo
        self._cpf = cpf
        self._covid = Covid.Covid(teve_febre, temperatura_corporal, outro_sintoma, kit_covid)
        self._medalhas = Medalhas.Medalhas(ouro, bronze, prata)
    
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

    def transformar_em_dicionario(self):
        dicionario = {}
        
        dicionario = {
            self._cpf = self._cpf,
            self._sexo = self._sexo,
            self._idade = self._idade,
            self._covid.teve_febre() = self._covid.teve_febre(),
            self._covid.temperatura_corporal() = self._covid.temperatura_corporal(),
            self._covid.outro_sintoma() = self._covid.outro_sintoma(),
            self._covid.kit_covid() = self._covid.kit_covid(),
            self._medalhas.ouro() = self._medalhas.ouro(),
            self._medalhas.prata() = self._medalhas.prata(),
            self._medalhas.bronze() = self._medalhas.bronze()
        }