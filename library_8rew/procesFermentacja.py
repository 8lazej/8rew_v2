from library_8rew.utils import INTRUKCJA_WYJSCIE, WYJSCIE, get_float_input

WYBOR_ALK = 'a'
def pokaz_polecenie(parametryWarzenia):
    while True:
        print(f'[{WYBOR_ALK}] - Oblicz teoretyczną zawartość alkoholu')
        print(INTRUKCJA_WYJSCIE)
        wybor = input()
        if wybor == WYBOR_ALK:
            zbierz_i_policz_alkohol(parametryWarzenia)
        elif wybor == WYJSCIE:
            break

def zbierz_i_policz_alkohol(parametryWarzenia):
    print('Podaj zmierzony ekstrakt po fermentacji')
    ekstraktPOfermentacja = get_float_input()
    parametryWarzenia.BLGpoFermentacji = ekstraktPOfermentacja
    ekstraktPRZEDfermentacja = parametryWarzenia.rzeczywisteBLGprzedFermentacja
    procent_alkoholu = (ekstraktPRZEDfermentacja - ekstraktPOfermentacja)/1.9
    print(f'Orientacyjny poziom alkoholu wynosi: {procent_alkoholu}%')
    parametryWarzenia.alk = procent_alkoholu
