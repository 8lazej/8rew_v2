from library_8rew.Chmiel import Chmiel
from library_8rew.Slod import Slod
from library_8rew.utils import CSV_PROPERTY_SEPARATOR, CSV_ELEMENT_SEPARATOR

def konwertuj_tekst_na_obiekty(tekst, type):
    listaElementowListyJakoLancuchyZnakow = tekst.split(CSV_ELEMENT_SEPARATOR)
    listaListWlasciwosciJakoLancuchyZnakow = map(
        lambda element: element.split(CSV_PROPERTY_SEPARATOR),
        listaElementowListyJakoLancuchyZnakow
    )
    listaListWlasciwosciJakoFloaty = list(map(
        lambda listaStringow: list(map(
            lambda string: float(string),
            listaStringow
        )),
        listaListWlasciwosciJakoLancuchyZnakow
    ))
    if (type == Chmiel):
        return zmien_na_chmiele(listaListWlasciwosciJakoFloaty)
    elif (type == Slod):
        return zmien_na_slody(listaListWlasciwosciJakoFloaty)
    return []

def zmien_na_chmiele(listaListWlasciwosciJakoFloaty):
    return list(map(
            lambda listaWlasciwosci: Chmiel(
                listaWlasciwosci[0],
                listaWlasciwosci[1], 
                listaWlasciwosci[2],
                listaWlasciwosci[3]
                ),
            listaListWlasciwosciJakoFloaty
        ))

def zmien_na_slody(listaListWlasciwosciJakoFloaty):
    return list(map(
            lambda listaWlasciwosci: Slod(
                listaWlasciwosci[0],
                listaWlasciwosci[1]
            ),
            listaListWlasciwosciJakoFloaty
        ))

def konwertuj_liste_obiektow_do_tekstu(obiekt):
    if isinstance(obiekt, list):
        if len(obiekt) == 0:
            return None
        if isinstance(obiekt[0], Chmiel):
            return konwertuj_chmiel_do_tekstu(obiekt)
        elif isinstance(obiekt[0], Slod):
            return konwertuj_slod_do_tekstu(obiekt)
        else: 
            return None
    return obiekt

def konwertuj_chmiel_do_tekstu(lista_chmielow):

    listaListWlasciwosciChmielow = map(
        lambda chmiel: [chmiel.masa_chmielu, chmiel.alfakwasy, chmiel.wykorzystanie, chmiel.czas], 
        lista_chmielow
        )
    # [ masa$alfakwasy$wykorzystanie$czas, ...]
    return zmien_liste_list_wlasciwosci_na_tekst(listaListWlasciwosciChmielow)
    
def konwertuj_slod_do_tekstu(listaSlodow):

    listaListWlasciwosciSlodow = map(
        lambda slod: [slod.procent_ekstraktywnosci, slod.procent_w_zasypie], 
        listaSlodow
        )
    return zmien_liste_list_wlasciwosci_na_tekst(listaListWlasciwosciSlodow)

def zmien_liste_list_wlasciwosci_na_tekst(listaListWlasciwosciObiektow):
    listaListWlasciwosciJakoLancuchyZnakow = map(
        lambda listaWlasciwosci: map(lambda wlasciwosc: str(wlasciwosc), listaWlasciwosci),
        listaListWlasciwosciObiektow
        )
    listaWlasciwosciObiektowJakoTekst = map(
        lambda listaWlasciwosci: CSV_PROPERTY_SEPARATOR.join(listaWlasciwosci), 
        listaListWlasciwosciJakoLancuchyZnakow
        )
    return CSV_ELEMENT_SEPARATOR.join(listaWlasciwosciObiektowJakoTekst)
