class Covid:
    def __init__(self, teve_febre: bool, temperatura_corporal: float, outro_sintoma: bool, kit_covid: bool) -> None:
        self._teve_febre = teve_febre
        self._temperatura_corporal = temperatura_corporal
        self._outro_sintoma = outro_sintoma
        self._kit_covid = kit_covid
    
    @property
    def teve_febre(self) -> bool:
        return self._teve_febre
    
    @teve_febre.setter
    def teve_febre(self, teve_febre: bool) -> None:
        self._teve_febre = teve_febre
    
    @property
    def temperatura_corporal(self) -> bool:
        return self._temperatura_corporal
    
    @temperatura_corporal.setter
    def tempratura_corporal(self, temperatura_corporal: float) -> None:
        self._temperatura_corporal = temperatura_corporal

    @property
    def outro_sintoma(self) -> bool:
        return self._outro_sintoma
    
    @outro_sintoma.setter
    def outro_sintoma(self, outro_sintoma: bool) -> None:
        self._outro_sintoma = outro_sintoma
    
    @property
    def kit_covid(self) -> bool:
        return self._kit_covid
    
    @kit_covid.setter
    def kit_covid(self, kit_covid: bool) -> None:
        self._kit_covid = kit_covid