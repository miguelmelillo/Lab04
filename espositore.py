class Espositore:
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome
        self._associatoA = ''

    def __str__(self):
        return [self.__nome, self.__cognome]

    def associa_a(self, codStand):
        self._associatoA = codStand
