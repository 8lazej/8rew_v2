#!/usr/bin/env python3

'''
informacje i licecencja warunki uzytkowania
Program 8rew jest dziełem projektowym stworzonym na potrzeby pracy licencjackiej
na kierunku Bioinformatyka (upwr), autorstwa Błazeja Kloca, pod opieką dr Jana Jelowickiego o tytule 
"Program wspomagający zarządzanie procesami biochemicznymi 
w procesie produkcji piwa domowego". 


'''
from library_8rew import ParametryWarzenia
from library_8rew import menu
from library_8rew import utils
import os
import sys

if not os.path.exists(utils.FILE_NAME):
    open(utils.FILE_NAME, 'w').close()
    
print('Witaj w 8rew!\n \
    Jest to program wspomagający zarządzanie procesami biochemicznymi w procesie produkcji piwa domowego\n \
    Aby poruszać się po programie, w konsoli terminala wpisz znak znajdujący się w nawiasie kwadratowym [] \n \
    po czym wciśnij enter\n \
    Na przykład jeśli chcesz utworzyć nową warkę, wybierz 1 i zatwierdź' )
def utworz_nowa_warke():
    print('Podaj ID nowej warki')
    idNowejWarki = input()
    parametryWarzenia = ParametryWarzenia.ParametryWarzenia(idNowejWarki)
    menu.obsluzParametryWarzenia(parametryWarzenia)

def edytuj_obecna_warke():
    print('Podaj ID warki')
    idWarki = input()
    with open(utils.FILE_NAME, 'r') as file:
        rows = [row for row in file if utils.ID_COLUMN_NAME not in row] # ['1;15;15', '2;15;89', '3;90;78']
        filtered_rows = list(filter(lambda row: row.split(utils.FILE_SEPARATOR)[0] == idWarki, rows))
        if len(filtered_rows) == 1:
            parametryWarzenia = ParametryWarzenia.ParametryWarzenia.fromRow(filtered_rows[0])
            menu.obsluzParametryWarzenia(parametryWarzenia)
        else:
            raise Exception("nie istnieje taka warka lub wystąpił blad w pliku")

while True:
    print("Wybierz")
    print("[1] - utwórz nową warkę")
    print("[2] - edytuj obecną warke")
    print("[k] - zakończ program")

    wybor = input()
    if (wybor == '1'):
        utworz_nowa_warke()
    elif (wybor == '2'):
        edytuj_obecna_warke()
    elif (wybor == 'k'):
            print('Dziękuję  za skorzystanie z programu 8rew. Do zobaczenia!')
            sys.exit()
    else:
        raise Exception('Błędnie wpisana wartość')

    
