
from library_8rew.utils import INTRUKCJA_WYJSCIE, WYJSCIE, get_float_input
import library_8rew.Chmiel
WYBOR_IBU = 'i'
def pokaz_polecenie(parametryWarzenia):

    while True:
        print(f'[{WYBOR_IBU}] - Oblicz IBU')
        print(INTRUKCJA_WYJSCIE)
        wybor = input()
        if wybor == WYBOR_IBU:
            zbierz_i_policz_chmiele(parametryWarzenia)
        elif wybor == WYJSCIE:
            break

def zbierz_i_policz_chmiele(parametryWarzenia):
    print('Podaj ilosc chmieli')
    ilosc_chmieli = int(input())

    nowa_lista_chmieli = []
    for i in range(ilosc_chmieli):
        print('Podaj mase w gramach chmielu' + str(i+1))
        masa_chmielu = get_float_input()
        
        print('Podaj procent alfa kwasów chmielu'+ str(i+1))
        alfakwasy = get_float_input()

        print('Podajsz czas w min. gotowania chmielu' + str(i+1))
        #to trzeba zamienic na wykorzystanie
        czas = get_float_input()
        wykorzystanie = oblicz_wykorzystanie(czas)

        kolejny_chmiel = library_8rew.Chmiel.Chmiel(masa_chmielu, alfakwasy, wykorzystanie, czas)
        nowa_lista_chmieli.append(kolejny_chmiel)
        
    parametryWarzenia.listaChmieli = nowa_lista_chmieli
    ibu = obliczIBU(nowa_lista_chmieli, parametryWarzenia)
    print('IBU wynosi:')
    print(ibu)
    for (index, item) in enumerate(nowa_lista_chmieli):
        print(f'Chmiel #{index + 1}, {item}')

    print('Po chmieleniu zmierz rzeczywiste BLG przed fermentacją i je podaj:')
    rzeczywiste_blg_przed_fermentacja = get_float_input()
    parametryWarzenia.rzeczywisteBLGprzedFermentacja = rzeczywiste_blg_przed_fermentacja
    parametryWarzenia.ibu = ibu


def oblicz_wykorzystanie(czas):
    MAKSYMALNE_WYKORZYSTANIE = 34
    table = [
        [9, 6],
        [19, 15],
        [29, 19],
        [44, 24],
        [59, 27],
        [74, 30],
    ]

    for [czas_gotowania, wykorzystanie] in table:
        if (czas < czas_gotowania):
            return wykorzystanie
            print(wykorzystanie)
    return MAKSYMALNE_WYKORZYSTANIE
    

    

def obliczIBU(lista_chmieli, parametryWarzenia):
    lista_IBU = []
    litryPiwa = parametryWarzenia.litryPiwa

    for chmiel in lista_chmieli:
        IBUchmielu = (chmiel.masa_chmielu * chmiel.alfakwasy * chmiel.wykorzystanie)/(litryPiwa * 10)
        lista_IBU.append(IBUchmielu)
        print(IBUchmielu)
    return sum(lista_IBU)