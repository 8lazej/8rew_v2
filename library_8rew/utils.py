import os
import sys
WYJSCIE = 'x'
NADWYZKA_WODY = 1.1
INTRUKCJA_WYJSCIE = '[x] - wyjdz'
FILE_NAME = '8rew_data.csv'
FILE_SEPARATOR = ';'
ID_COLUMN_NAME = 'ID'
NULL_DATA = 'NULL'
CSV_ELEMENT_SEPARATOR = '@'
CSV_PROPERTY_SEPARATOR = '$'
SEP = '/'
FILE_NAME = os.path.split(os.path.abspath(sys.argv[0]))[0] + SEP + FILE_NAME


def get_float_input(type=float):
    while True:
        try:
            x = type(input())
            return x
        except:
            print("Podaj poprawna wartosc (moze . zamiast , ?)")
            continue

