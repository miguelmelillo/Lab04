from stand import Stand

class StandPrese(Stand):
    def __init__(self, metriQuadri, padiglione, prezzo, numPrese):
        super().__init__(metriQuadri, padiglione, prezzo)
        self._prezzo = float(prezzo) * (1 + 0.07 * int(numPrese))
        self.__numPrese = int(numPrese)

    def __str__(self):
        return [self.__metriQuadri, self.__padiglione, self.__prezzo, self.__numPrese]