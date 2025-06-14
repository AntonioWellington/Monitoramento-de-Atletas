class Medalhas:
    def __init__(self, ouro: int, bronze: int, prata: int) -> None:
        self._ouro = ouro
        self._prata = prata
        self._bronze = bronze
    
    @property
    def ouro(self) -> int:
        return self._ouro
    
    @ouro.setter
    def ouro(self, ouro: int) -> None:
        self._ouro = ouro
    
    @property
    def prata(self) -> int:
        return self._prata
    
    @ouro.setter
    def prata(self, prata: int) -> None:
        self._prata = prata

    @property
    def bronze(self) -> int:
        return self._bronze
    
    @ouro.setter
    def bronze(self, bronze: int) -> None:
        self._bronze = bronze

    def total_de_medalhas(self) -> int:
        total = (self._ouro + self._prata + self._bronze)
        return total