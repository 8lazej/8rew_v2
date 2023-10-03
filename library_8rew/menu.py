import library_8rew.procesZacieranie 
import library_8rew.procesChmielenie
import library_8rew.procesFermentacja
from library_8rew.utils import WYJSCIE, INTRUKCJA_WYJSCIE, get_float_input 
import library_8rew.podsumowanie 
import sys
def obsluzParametryWarzenia(parametryWarzenia):
    while True:
        podaj_podstawowe_parametry(parametryWarzenia)
        print('Wybierz opcję:')
        print('[z] - Zacieranie')
        print('[c] - Chmielenie')
        print('[f] - Fermentacja')
        print('[p] - Zobacz podsumowanie parametrów danej Warki')
        print('[k] - zakończ program')
        print(INTRUKCJA_WYJSCIE)
        wybor = input()
        if wybor == 'z':
            library_8rew.procesZacieranie.pokaz_polecenie(parametryWarzenia)
        elif wybor == 'c':
            library_8rew.procesChmielenie.pokaz_polecenie(parametryWarzenia)
        elif wybor == 'f':
            library_8rew.procesFermentacja.pokaz_polecenie(parametryWarzenia)
        elif wybor == 'p':
            library_8rew.podsumowanie.pokaz_podsumowanie(parametryWarzenia)
        elif wybor == WYJSCIE:
            break
        elif wybor == 'k':
            print('Dziękuję  za skorzystanie z programu 8rew. Do zobaczenia!')
            sys.exit()
        else:
            print('Bledny wpis, sprobuj jeszcze raz')
        parametryWarzenia.save_to_file()
        
def podaj_podstawowe_parametry(parametryWarzenia):
    if parametryWarzenia.blg == None or parametryWarzenia.litryPiwa == None:
        print('Na początku podaj podstawowe parametry twojej warki')
        print('Podaj żądane BLG:')
        blg = get_float_input()
        print('Podaj ile litrów piwa chcesz uwarzyć:')
        litry_piwa = get_float_input()
        parametryWarzenia.blg = blg
        parametryWarzenia.litryPiwa = litry_piwa
        parametryWarzenia.save_to_file()
    