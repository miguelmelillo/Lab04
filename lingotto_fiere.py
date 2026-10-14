from operator import itemgetter
from stand import Stand
from stand_prese import StandPrese
from stand_premium import StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self._stands = {} # dict con chiave = codStand
        self._espositori = {} #dict con chiave = codEsp.

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        f = open(file_path, "r") # Ho salvato i dati in dizionari che hanno come chiave il codice e come elemento gli oggetti stand o espositore
        for riga in f:
            riga = riga.strip()
            campo = riga.split(",")
            if campo[0][0] == "S": # significa che è uno stand
                codStand = campo[0]
                metriQuadri = campo[1]
                padiglione = campo[2]
                prezzoBase = campo[3]
                if len(campo) == 4: # stand standard
                    self._stands[codStand] = Stand(metriQuadri, padiglione, prezzoBase)
                if len(campo) == 5:
                    if campo[4].isdigit():
                        numPrese = campo[4]
                        self._stands[codStand] = StandPrese(metriQuadri, padiglione, prezzoBase, numPrese)
                    if campo[4].isalpha():
                        tipoPremium = campo[4]
                        self._stands[codStand] = StandPremium(metriQuadri, padiglione, prezzoBase, tipoPremium)
            if campo[0][0] == "E": # significa che è un espositore
                codEspositore = campo[0]
                nomeEspositore = campo[1]
                cognomeEspositore = campo[2]
                self._espositori[codEspositore] = Espositore(nomeEspositore, cognomeEspositore)
        f.close()

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if codice_stand in self._stands.keys(): # esiste lo stand
            if codice_espositore in self._espositori.keys(): #esiste lo espositore
                if self._stands[codice_stand]._assegnatoA == '': # non è assegnato a nessuno
                    if self._espositori[codice_espositore]._associatoA == '': # non è associato a nessuno
                        self._stands[codice_stand].assegna_a(codice_espositore)
                        self._espositori[codice_espositore].associa_a(codice_stand)
                    else:
                        raise Exception('Espositore associato ad altro stand')
                else:
                    raise Exception('Stand associato ad altro espositore')
            else:
                raise Exception('Espositore non trovato')
        else:
            raise Exception('Stand non trovato')


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        print('-------------------------------------')
        for esp in self._espositori:
            if self._espositori[esp]._associatoA == '': # se non ha nessuno stand associato, stampa soltanto il suo codice
                print(esp)
            else: # invece se ha, stampa il codice e anche lo stand a cui è stato associato
                print(f'{esp} - {self._espositori[esp]._associatoA}')
        print('-------------------------------------')

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        print('-------------------------------------')
        listaStandPrezzo = []
        for st in self._stands:
            listaStandPrezzo.append([st, self._stands[st]._prezzo])
        listaStandPrezzo.sort(key=itemgetter(1), reverse=False) # per ordinare gli stand in base al prezzo
        for i in range(0, len(listaStandPrezzo)):
            print(f'{listaStandPrezzo[i][0]} - {listaStandPrezzo[i][1]:.2f} €')
        print('-------------------------------------')

