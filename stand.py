class Stand:
    def __init__(self, metriQuadri, padiglione, prezzo):
        #self.__codiceStand = codiceStand
        self.__metriQuadri = metriQuadri
        self.__padiglione = padiglione
        self._prezzo = float(prezzo)
        self._assegnatoA = ''

    def __str__(self):
        return [self.__prezzo, self.__padiglione, self.__prezzo]

    def assegna_a(self, codEspositore):
        self._assegnatoA = codEspositore