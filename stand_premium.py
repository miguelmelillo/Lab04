from stand import Stand

class StandPremium(Stand):
    def __init__(self, metriQuadri, padiglione, prezzo, tipoPremium):
        super().__init__(metriQuadri, padiglione, prezzo)
        self._prezzo = float(prezzo) * 1.30
        self.__tipoPremium = tipoPremium

    def __str__(self):
        return [self.__metriQuadri, self.__padiglione, self.__prezzo, self.__tipoPremium]