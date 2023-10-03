def pokaz_podsumowanie(parametryWarzenia):
    print("zadane BLG: ", parametryWarzenia.blg)
    print('Ilosc litrow piwa: ', parametryWarzenia.litryPiwa)
    print('Alkohol:', parametryWarzenia.getAlkohol())
    print('IBU:', parametryWarzenia.getIBU())
    print('Rzeczywiste BLG przed fermnetacją wyniosło: ',parametryWarzenia.getRzeczywisteBLGprzedFermentacja())
    print('Blg po fermentacji wynosilo:', parametryWarzenia.getBLGpoFermentacji())
    wydrukuj_liste(parametryWarzenia.getListaSlodow(), 'Slod')
    wydrukuj_liste(parametryWarzenia.getListaChmieli(), 'Chmiel')
    print('Woda użyta do zacierania:', parametryWarzenia.getWodaZacieranie())
    print('Woda użyta do wysladzania:', parametryWarzenia.getWodaWysladzanie())

def wydrukuj_liste(lista, nazwa):
    for (index, item) in enumerate(lista):
        print(f'{nazwa} #{index + 1}, {item}')