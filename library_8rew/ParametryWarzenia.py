from library_8rew.konwerterObiektTekst import konwertuj_liste_obiektow_do_tekstu, konwertuj_tekst_na_obiekty
from library_8rew.utils import FILE_NAME, FILE_SEPARATOR, ID_COLUMN_NAME, NULL_DATA
from library_8rew.Slod import Slod
from library_8rew.Chmiel import Chmiel

def toFloatIfExists(data):
    return float(data) if data != NULL_DATA else None


LISTA_NAGLOWKOW = [
    ID_COLUMN_NAME, 
    'BLG',
    'Litry_piwa',
    'BLG_przed_Fermentacja', 
    'BLG_po_Fermentacji', 
    'IBU', 
    'ABV',
    'Kilogramy_Zasypu',
    'Woda_Wysladzanie',
    'Woda_Zacieranie',
    'Slody',
    'Chmiele'
]

class ParametryWarzenia:
    @classmethod
    def fromRow(self, row):
        # 'ID;BLG;LITRYPIWA;RBPF;LisraSlodow'
        splitRow = row.strip().split(FILE_SEPARATOR) # [ID, BLG, ...],strip -  pozbywa sie \n np. znakow, a split dzieli po separatorze
        return ParametryWarzenia(
            splitRow[0], 
            toFloatIfExists(splitRow[1]), 
            toFloatIfExists(splitRow[2]), 
            toFloatIfExists(splitRow[3]),
            toFloatIfExists(splitRow[4]),
            toFloatIfExists(splitRow[5]),
            toFloatIfExists(splitRow[6]),
            toFloatIfExists(splitRow[7]),
            toFloatIfExists(splitRow[8]),
            toFloatIfExists(splitRow[9]),
            konwertuj_tekst_na_obiekty(splitRow[10], Slod),
            konwertuj_tekst_na_obiekty(splitRow[11], Chmiel)
            )
    
    def __init__(
            self, 
            id, 
            blg=None, 
            litryPiwa=None, 
            rzeczywisteBLGprzedFermentacja=None, 
            BLGpoFermentacji=None, 
            ibu=None,
            alk=None,
            KgZasypu=None,
            wodaDoZacierania=None,
            wodaDoWysladzania=None,
            listaSlodow=None,
            listaChmieli=None
            ):
        self.blg = blg
        self.litryPiwa = litryPiwa #definiujemy jak pola beda sie nazywaly
        self.rzeczywisteBLGprzedFermentacja = rzeczywisteBLGprzedFermentacja
        self.BLGpoFermentacji = BLGpoFermentacji
        self.id = id
        self.ibu = ibu
        self.alk = alk
        self.KgZasypu = KgZasypu
        self.wodaDoZacierania = wodaDoZacierania
        self.wodaDoWysladzania = wodaDoWysladzania
        self.listaSlodow = listaSlodow
        self.listaChmieli = listaChmieli
        

    def setBlg(self, blg):
        self.blg = blg
    def setLitryPiwa(self, litryPiwa):
        self.litryPiwa = litryPiwa
    def setListaSlodow(self, listaSlodow):
        self.listaSlodow = listaSlodow
    def setSumaZasypu(self, sumaZasypu):
        self.sumaZasypu = sumaZasypu
    def setSumaIBU(self, SumaIBU):
        self.SumaIBU = SumaIBU
    def getBlg(self):
        return self.blg
    def getLitryPiwa(self):
        return self.litryPiwa
    def setidWarkiP(self, idWarkiP):
        self.idWarkiP = idWarkiP
    def getidWarkiP(self):
        return self.idWarkiP
    def getListaSlodow(self):
        return self.try_get_value(lambda: self.listaSlodow, [])
    def getListaChmieli(self):
        return self.try_get_value(lambda: self.listaChmieli, [])
    def getSumaZasypu(self):
        return self.try_get_value(lambda: self.sumaZasypu)
    def getAlkohol(self):
        return self.try_get_value(lambda: self.alk)
    def getIBU(self):
        return self.try_get_value(lambda: self.ibu)
    def getBLGpoFermentacji(self):
        return self.try_get_value(lambda: self.BLGpoFermentacji)
    def getRzeczywisteBLGprzedFermentacja(self):
        return self.try_get_value(lambda: self.rzeczywisteBLGprzedFermentacja)
    def getWodaZacieranie(self):
        return self.try_get_value(lambda: self.wodaDoZacierania)
    def getWodaWysladzanie(self):
        return self.try_get_value(lambda: self.wodaDoWysladzania)
           
    def konwertuj_parametry_warzenia_to_row(self):
        listOfProperties = [
            self.id, 
            self.blg, 
            self.litryPiwa, 
            self.rzeczywisteBLGprzedFermentacja, 
            self.BLGpoFermentacji, 
            self.ibu, 
            self.alk, 
            self.KgZasypu,
            self.wodaDoZacierania,
            self.wodaDoWysladzania,
            konwertuj_liste_obiektow_do_tekstu(self.listaSlodow),
            konwertuj_liste_obiektow_do_tekstu(self.listaChmieli)
        ]
        listOfPropsWithEmptySpaceInsteadOfNone = map(lambda prop: NULL_DATA if prop is None else prop, listOfProperties)
        return ';'.join(map(lambda prop: str(prop), listOfPropsWithEmptySpaceInsteadOfNone)) + '\n'
        
    def save_to_file(self):
        hasBeenUpdated = False
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
        with open(FILE_NAME, 'w') as file:
            if lines == []:
                file.write(FILE_SEPARATOR.join(LISTA_NAGLOWKOW) + '\n')
            for line in lines:
                if (line.split(FILE_SEPARATOR)[0] == self.id):
                    file.write(self.konwertuj_parametry_warzenia_to_row())
                    hasBeenUpdated = True
                else:
                    file.write(line)
            
            if not hasBeenUpdated:
                file.write(self.konwertuj_parametry_warzenia_to_row())

    def try_get_value(self, getValueAction, default=None):
        try:
            x = getValueAction()
            return x
        except:
            print("Te wartości nie zostały nigdy zapisane do pliku")
            return default


    
    
    