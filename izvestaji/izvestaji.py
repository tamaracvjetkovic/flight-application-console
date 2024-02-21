
from datetime import datetime, date

from karte import karte



"""
Funkcija kao rezultat vraća listu karata prodatih na zadati dan.
"""
def izvestaj_prodatih_karata_za_dan_prodaje(sve_karte: dict, dan: date) -> list:
    listaKarata = []
    num = 1
    for karta in sve_karte:
        if sve_karte[karta]["datum_prodaje"] == dan:
            okKarta = {"broj_karte": sve_karte[karta]["broj_karte"],
                       "datum_prodaje": sve_karte[karta]["datum_prodaje"]}
            listaKarata.append(okKarta)
    
    return listaKarata


"""
Funkcija kao rezultat vraća listu svih karata čiji je dan polaska leta na zadati dan.
"""
def izvestaj_prodatih_karata_za_dan_polaska(sve_karte: dict, svi_konkretni_letovi: dict, dan: date) -> list:
    listaKarata = []
    for karta in sve_karte:
        sifra = sve_karte[karta]["sifra_konkretnog_leta"]
        datum = svi_konkretni_letovi[sifra]["datum_i_vreme_polaska"]
        if datum.year == dan.year and datum.month == dan.month and datum.day == dan.day:
                okKarta = {"broj_karte": sve_karte[karta]["broj_karte"],
                           "datum_prodaje": sve_karte[karta]["datum_prodaje"],
                           "sifra_konkretnog_leta": sve_karte[karta]["sifra_konkretnog_leta"]}
                listaKarata.append(okKarta)

    return listaKarata

# path = 'C:\\Users\\Username\\Path\\To\\File'
"""  
Funkcija kao rezultat vraća listu karata koje je na zadati dan prodao zadati prodavac.
"""
def izvestaj_prodatih_karata_za_dan_prodaje_i_prodavca(sve_karte: dict, dan: date, prodavac: str) -> list:
    listaKarata = []
    for karta in sve_karte:
        datum = sve_karte[karta]["datum_prodaje"]
        if datum.year == dan.year and datum.month == dan.month and datum.day == dan.day:
            prodavac1 = sve_karte[karta]["prodavac"]
            if prodavac1 == prodavac:
                sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
                if sve_karte == sveKarte:
                    okKarta = {"broj_karte": sve_karte[karta]["broj_karte"],
                               "sifra_konkretnog_leta": sve_karte[karta]["sifra_konkretnog_leta"],
                               "sifra": sve_karte[karta]["sifra_konkretnog_leta"],
                               "kupac": sve_karte[karta]["kupac"],
                               "prodavac": sve_karte[karta]["prodavac"],
                               "sediste": sve_karte[karta]["sediste"],
                               "datum_prodaje": sve_karte[karta]["datum_prodaje"],
                               "obrisana": sve_karte[karta]["obrisana"]}
                else:
                    okKarta = {"broj_karte": sve_karte[karta]["broj_karte"],
                               "sifra_konkretnog_leta": sve_karte[karta]["sifra_konkretnog_leta"],
                               "sifra": sve_karte[karta]["sifra_konkretnog_leta"],
                               "kupac": sve_karte[karta]["kupac"],
                               "prodavac": sve_karte[karta]["prodavac"],
                               "sifra_sedista": sve_karte[karta]["sifra_sedista"],
                               "datum_prodaje": sve_karte[karta]["datum_prodaje"],
                               "obrisana": sve_karte[karta]["obrisana"]}
                listaKarata.append(okKarta)
                
    return listaKarata


"""
Funkcija kao rezultat vraća dve vrednosti: broj karata prodatih na zadati dan i njihovu ukupnu cenu.
Rezultat se vraća kao torka. Npr. return broj, suma
"""
def izvestaj_ubc_prodatih_karata_za_dan_prodaje(sve_karte: dict, svi_konkretni_letovi: dict,
                                                svi_letovi, dan: date) -> tuple:
    num = 0
    cena = 0
    #return num, cena
    for karta in sve_karte:
        if sve_karte[karta]["datum_prodaje"] == dan:
            sifraLeta = sve_karte[karta]["sifra_konkretnog_leta"]
            brojLeta = svi_konkretni_letovi[sifraLeta]["broj_leta"]
            num += 1
            cena += float(svi_letovi[brojLeta]["cena"])
    
    return (num, cena)


"""
Funkcija kao rezultat vraća dve vrednosti: broj karata čiji je dan polaska leta na zadati dan i njihovu ukupnu cenu.
Rezultat se vraća kao torka. Npr. return broj, suma
"""
def izvestaj_ubc_prodatih_karata_za_dan_polaska(sve_karte: dict, svi_konkretni_letovi: dict, 
                                                svi_letovi: dict, dan: date) -> tuple:
    num = 0
    cena = 0
    sveSifre = {}
  
    for let in svi_konkretni_letovi:
        datum = svi_konkretni_letovi[let]["datum_i_vreme_polaska"]
        if datum.year == dan.year and datum.month == dan.month and datum.day == dan.day:
            brojLeta = svi_konkretni_letovi[let]["broj_leta"] 
            sveSifre.update({svi_konkretni_letovi[let]["sifra"]: brojLeta})
    for karta in sve_karte:
        sifraLeta = sve_karte[karta]["sifra_konkretnog_leta"]
        if sifraLeta in sveSifre:
            num += 1
            brojLeta = sveSifre[sifraLeta]
            cena += float(svi_letovi[brojLeta]["cena"])

    return (num, cena)


"""
Funkcija kao rezultat vraća dve vrednosti: broj karata koje je zadati prodavac prodao na zadati dan i njihovu 
ukupnu cenu. Rezultat se vraća kao torka. Npr. return broj, suma
"""
def izvestaj_ubc_prodatih_karata_za_dan_prodaje_i_prodavca(sve_karte: dict, konkretni_letovi: dict, 
                                                           svi_letovi: dict, dan: date,
                                                           prodavac: str) -> tuple:
    num = 0
    cena = 0

    for karta in sve_karte:
        datum = sve_karte[karta]["datum_prodaje"]
        if datum.year == dan.year and datum.month == dan.month and datum.day == dan.day:
            prodavac1 = sve_karte[karta]["prodavac"]
            if prodavac1 == prodavac:
               sifraLeta = sve_karte[karta]["sifra_konkretnog_leta"]
               brojLeta = konkretni_letovi[sifraLeta]["broj_leta"]
               cena += float(svi_letovi[brojLeta]["cena"])
               num += 1
               
    return (num, cena)            


"""
Funkcija kao rezultat vraća rečnik koji za ključ ima dan prodaje, a za vrednost broj karata prodatih na taj dan.
Npr: {"2023-01-01": 20}

rezultat: {prodavac1: (brKarata1, ukupnaCijena1, prodavac1), prodavac2: (brKarata2, ukupnaCijena2, prodavac1)}
"""
def izvestaj_ubc_prodatih_karata_30_dana_po_prodavcima(sve_karte: dict, svi_konkretni_letovi: dict, 
                                                       svi_letovi: dict) -> dict:
    rezultat = {}
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    for karta in sve_karte:
        prodavac = sve_karte[karta]["prodavac"]
        if prodavac == "":
            continue
        pairs = (0, 0, "")
        if sve_karte == sveKarte:
            newDict = {prodavac["korisnicko_ime"]: pairs}
        else:
            newDict = {prodavac: pairs}
        rezultat.update(newDict) 
        
    for karta in sve_karte:
        prodavac = sve_karte[karta]["prodavac"]
        if prodavac == "":
            continue
        if sve_karte == sveKarte:
            datum = sve_karte[karta]["datum_prodaje"]
        else:
            datum = str(sve_karte[karta]["datum_prodaje"])
            values = []
            str1 = ""
            for i in datum:
                if i == ".":
                    values.append(int(str1))
                    str1 = ""
                    continue
                str1 += i
        today = date.today()
        d0 = date(today.year, today.month, today.day)
        if sveKarte == sve_karte:
            d1 = date(datum.year, datum.month, datum.day)
        else:
            d1 = date(values[2], values[1], values[0])
        delta = d1 - d0
        if abs(delta.days) <= 30:
            brojLeta = svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]
            if sve_karte == sveKarte:
                pairs = rezultat[prodavac["korisnicko_ime"]]
            else:
                pairs = rezultat[prodavac]
            cena = pairs[1]
            cena += float(svi_letovi[brojLeta]["cena"]) 
            num = pairs[0]
            num += 1
            prod = prodavac
            newPairs = (num, cena, prod)
            if sve_karte == sveKarte:
                rezultat[prodavac["korisnicko_ime"]] = newPairs  
            else:
                rezultat[prodavac] = newPairs    
       
    return rezultat


