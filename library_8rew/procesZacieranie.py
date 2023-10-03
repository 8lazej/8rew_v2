from library_8rew.utils import WYJSCIE, INTRUKCJA_WYJSCIE, NADWYZKA_WODY, get_float_input
import library_8rew.Slod

WYBOR_EKSTRAKT = 's'
WYBOR_WODA = 'w'

def pokaz_polecenie(parametryWarzenia):

    while True:
        print(f'[{WYBOR_EKSTRAKT}] - Oblicz ilosc potrzebnych slodow')
        print(f'[{WYBOR_WODA}] - Oblicz ilosc potrzebnej wody')
        print(INTRUKCJA_WYJSCIE)
        wybor_procesu_zacierania = input()
        if wybor_procesu_zacierania == WYBOR_EKSTRAKT:
            zbierz_i_policz_ekstrakt(parametryWarzenia)
        elif wybor_procesu_zacierania == WYBOR_WODA:
            zbierz_i_policz_wode(parametryWarzenia)
        elif wybor_procesu_zacierania == WYJSCIE:
            break

def zbierz_i_policz_ekstrakt(parametryWarzenia):
    ekstrakt = policz_ekstrakt(parametryWarzenia.blg, parametryWarzenia.litryPiwa)
    print('Podaj ilosc slodow')
    ilosc_slodow = get_float_input(int)
    suma_udzialow = 0
    while not (99 < suma_udzialow <= 100):
        nowa_lista_slodow = []
        for i in range(ilosc_slodow):
            print('Podaj ekstraktywnosc slodu' + str(i+1))
            ekstraktywnosc_slodu = get_float_input()
            
            print('Podaj procentowy udział w zasypie')
            procent_w_zasypie = get_float_input()


            kolejny_slod = library_8rew.Slod.Slod(ekstraktywnosc_slodu, procent_w_zasypie)
            nowa_lista_slodow.append(kolejny_slod)
        
        lista_udzialow = list(map(lambda slod: slod.procent_w_zasypie, nowa_lista_slodow))

        suma_udzialow = sum(lista_udzialow)
        parametryWarzenia.setListaSlodow(nowa_lista_slodow)

        if not (99 < suma_udzialow <= 100):
            print("Suma udzialow powinna byc wieksza niz 99 i mniejsza badz rowna 100 %")
 
    print('Suma rzeczywostych ekstraktow slodow wynosi:')
    suma_RES = policz_sume_rzeczyswistych_ekstraktow_slodow(nowa_lista_slodow)
    print(suma_RES)

    print('Suma zasypu w kg wynosi:')
    suma_zasypu = ekstrakt/suma_RES
    parametryWarzenia.setSumaZasypu(suma_zasypu)
    print(suma_zasypu)

    lista_kazdego_slodu_w_kg = list(map(lambda udzial: udzial / 100 * suma_zasypu, lista_udzialow))
    
    for (index, item) in enumerate(lista_kazdego_slodu_w_kg):
        print(f'Slod {index + 1} dodaj w ilości {item} kg')
    parametryWarzenia.KgZasypu = suma_zasypu

def zbierz_i_policz_wode(parametryWarzenia):
    print('Podaj wspolczynnik 1 kg slodu do x l wody')
    wspolczynnik_slod_woda = get_float_input()
    print('Woda potrzebna do zacierania w litrach:')
    suma_listy_slodow = parametryWarzenia.getSumaZasypu() 
    woda_do_zacierania = suma_listy_slodow * wspolczynnik_slod_woda
    print(woda_do_zacierania)
    parametryWarzenia.wodaDoZacierania = woda_do_zacierania
    print('Woda potrzebna do wysladzania w litrach')
    woda_do_wysladzania = policz_sume_wody_do_wysladzania(parametryWarzenia.getLitryPiwa(), suma_listy_slodow, woda_do_zacierania)
    print(woda_do_wysladzania)
    parametryWarzenia.wodaDoWysladzania = woda_do_wysladzania
    print('Woda do calego prcoesu:')
    woda_calosc = woda_do_zacierania + woda_do_wysladzania
    print(woda_calosc)

def policz_ekstrakt(BLG, litry_piwa):
    brzeczka_po_warzeniu_przed_cedzeniem = litry_piwa * NADWYZKA_WODY
    gestosc_wlasciwa = 1 + (BLG / (258.6 - (BLG / 258.2) * 227.1))
    waga_brzeczki_po_warzeniu = brzeczka_po_warzeniu_przed_cedzeniem * gestosc_wlasciwa 
    return waga_brzeczki_po_warzeniu * BLG * 10 

def policz_sume_rzeczyswistych_ekstraktow_slodow(lista_slodow):
    suma_RESow = []
    for slod in lista_slodow:
        teoretyczny_ekstrakt_slodu_w_gramach_na_kilogram = slod.procent_ekstraktywnosci * 10
        rzeczywisty_ekstrakt_slodu_w_gramach_na_kilogram = teoretyczny_ekstrakt_slodu_w_gramach_na_kilogram * 0.75
        rzeczywisty_ekstrakt_slodu = rzeczywisty_ekstrakt_slodu_w_gramach_na_kilogram * slod.procent_w_zasypie /100
        suma_RESow.append(rzeczywisty_ekstrakt_slodu)
    return sum(suma_RESow)

def policz_sume_wody_do_wysladzania(litryPiwa, suma_listy_slodow, woda_do_zacierania):
    woda_pozotala_w_mlocie = suma_listy_slodow
    woda_odparowana_przy_chmieleniu = litryPiwa * 0.15
    straty_chmiel_gestwa = litryPiwa * 0.1
    woda_do_uzupelnienia = litryPiwa - woda_do_zacierania
    return woda_pozotala_w_mlocie + woda_odparowana_przy_chmieleniu + straty_chmiel_gestwa + woda_do_uzupelnienia