
from datetime import datetime, timedelta

import csv
    

sledeci_broj_sifre_leta = 1


"""
Funkcija koja za zadati konkretni let kreira sve konkretne letove u opsegu operativnosti.
Kao rezultat vraća rečnik svih konkretnih letova koji sadrži nove konkretne letove.
"""
def kreiranje_konkretnog_leta(svi_konkretni_letovi: dict, let: dict) -> dict:
        # BROJ LETA
    broj_leta = let["broj_leta"]
    if broj_leta is None or broj_leta == "":
        raise Exception("GRESKA: 'broj_leta' je prazno. Unesite ponovo.")
    if len(broj_leta) != 4:
        raise Exception("GRESKA: 'broj_leta' nije dobro definisano. Unesite ponovo.")
    if ord(broj_leta[0].lower()) < 97 or ord(broj_leta[0].lower()) > 122:
        raise Exception("GRESKA: 'broj_leta' nije dobro definisano. Unesite ponovo.")
    if ord(broj_leta[1].lower()) < 97 or ord(broj_leta[1].lower()) > 122:
        raise Exception("GRESKA: 'broj_leta' nije dobro definisano. Unesite ponovo.")
    if ord(broj_leta[2]) < 48 or ord(broj_leta[2]) > 57:
        raise Exception("GRESKA: 'broj_leta' nije dobro definisano. Unesite ponovo.")
    if ord(broj_leta[3]) < 48 or ord(broj_leta[3]) > 57:
        raise Exception("GRESKA: 'broj_leta' nije dobro definisano. Unesite ponovo.") 
    
    datum_kraja_operativnosti = let["datum_kraja_operativnosti"]
    datum_pocetka_operativnosti = let["datum_pocetka_operativnosti"]
    
    if datum_kraja_operativnosti < datum_pocetka_operativnosti:
        raise Exception("GRESKA: 'datum_operativnosti' nije dobro definisano. Unesite ponovo.") 
    
    sati1 = int(let["vreme_poletanja"].split(":")[0])
    minuti1 = int(let["vreme_poletanja"].split(":")[1])
    godina1 = datum_pocetka_operativnosti.year
    mjesec1 = datum_pocetka_operativnosti.month
    dan1 = datum_pocetka_operativnosti.day
    datumPocetkaOperativnosti = datetime(godina1, mjesec1, dan1, sati1, minuti1)
    sati2 = int(let["vreme_sletanja"].split(":")[0])
    minuti2 = int(let["vreme_sletanja"].split(":")[1])
    godina2 = datum_kraja_operativnosti.year
    mjesec2 = datum_kraja_operativnosti.month
    dan2 = datum_kraja_operativnosti.day
    datumKrajaOperativnosti = datetime(godina2, mjesec2, dan2, sati2, minuti2)
    
    global sledeci_broj_sifre_leta
    
    daniLista = let["dani"]
    datum = datumPocetkaOperativnosti
    
    while True:
        if datum < datum_pocetka_operativnosti:
            datum = datum + timedelta(days = 1)
            continue
        if datum > datum_kraja_operativnosti:
            break
        week = datum.weekday()
        if week in daniLista:
            datumPolaska = datum
            if let["sletanje_sutra"] is True:
                datumm = datumPolaska + timedelta(days = 1)
                datumDolaska = datetime(datumm.year, datumm.month, datumm.day, sati2, minuti2)
            else:
                datumDolaska = datetime(datumPolaska.year, datumPolaska.month, datumPolaska.day, sati2, minuti2)
            if datumDolaska > datumKrajaOperativnosti or datumPolaska < datum_pocetka_operativnosti:
                datum = datum + timedelta(days = 1)
                continue
            
            konkretniLet = {"sifra": sledeci_broj_sifre_leta, 
                           "broj_leta": broj_leta,
                           "datum_i_vreme_polaska": datumPolaska, 
                           "datum_i_vreme_dolaska": datumDolaska}
            newDict = {sledeci_broj_sifre_leta: konkretniLet}
            sledeci_broj_sifre_leta += 1
            svi_konkretni_letovi.update(newDict)   
        datum = datum + timedelta(days = 1)
    
    return svi_konkretni_letovi


"""
Funkcija čuva konkretne letove u fajl na zadatoj putanji sa zadatim separatorom. 
"""
def sacuvaj_kokretan_let(putanja: str, separator: str, svi_konkretni_letovi: dict):
    fields = ["sifra", "broj_leta", "datum_i_vreme_polaska", "datum_i_vreme_dolaska", "zauzetost"]
    with open(putanja, 'a', newline = "") as f:
        w = csv.DictWriter(f, fieldnames = fields, delimiter = separator)
        #w.writeheader()
        for i in svi_konkretni_letovi:
            w.writerow(svi_konkretni_letovi[i])
    
    return


"""
Funkcija učitava konkretne letove iz fajla na zadatoj putanji sa zadatim separatorom.
"""
def ucitaj_konkretan_let(putanja: str, separator: str) -> dict:
    myDict = {}
    with open(putanja, 'r') as f:
        r = csv.reader(f, delimiter = separator)
        for i in r:
            datumPolaska = datetime.strptime(i[2], "%Y-%m-%d %H:%M:%S")
            datumDolaska = datetime.strptime(i[3], "%Y-%m-%d %H:%M:%S")
            let = {"sifra": int(i[0]), 
                   "broj_leta": i[1],
                   "datum_i_vreme_polaska": datumPolaska,
                   "datum_i_vreme_dolaska": datumDolaska,
                   "zauzetost": eval(i[4])}
            myDict.update({int(i[0]): let})  
      
   
    return myDict


def podesi_sledeci_broj_sifre(svi_konkretni_letovi: dict):
    global sledeci_broj_sifre_leta
    sledeci_broj_sifre_leta = len(svi_konkretni_letovi) + 1
    return
    
    
def pregled_svih_konkretnih_letova(svi_letovi, konkretni_letovi):
    lista = [["ŠIFRA", "LET", "ŠPA", "ŠOA", "POLETANJE", "SLETANJE", "PREVOZNIK", "MODEL", " CENA "]]
# ["BROJ", "LET", "ŠPA", "ŠOA", "POLETANJE", "SLETANJE", "PREVOZNIK", "MODEL", " CENA "]   
    for i in konkretni_letovi:
        brojLeta = konkretni_letovi[i]["broj_leta"]
        let = svi_letovi[brojLeta]
        datumPolaska1 = konkretni_letovi[i]['datum_i_vreme_polaska']
        datumPolaska = datetime(datumPolaska1.year, datumPolaska1.month, datumPolaska1.day)  
        datumDolaska1 = konkretni_letovi[i]['datum_i_vreme_dolaska']
        datumDolaska = datetime(datumDolaska1.year, datumDolaska1.month, datumDolaska1.day) 
        num = konkretni_letovi[i]["sifra"]            
        x1 = brojLeta
        x2 = let["sifra_polazisnog_aerodroma"]
        x3 = let["sifra_odredisnog_aerodorma"]
        x4 = let["vreme_poletanja"] + "h"
        x5 = let["vreme_sletanja"] + "h"
        x66 = datumPolaska
        x6 = str(str(x66.year) + "/" + str(x66.month) + "/" + str(x66.day))
        x77 = datumDolaska
        x7 = str(str(x77.year) + "/" + str(x77.month) + "/" + str(x77.day)) 
        x6 = x6 + " | " + x4
        x7 = x7 + " | " + x5
        x8 = let["prevoznik"]
        x10 = let["model"]["naziv"] 
        x111 = let["cena"]
        x11 = float("{:.2f}".format(x111))                         
        lista.append([num, x1, x2, x3, x6, x7, x8, x10, x11])
        num += 1           
    
    return lista
    
    
"""
sacuvaj_kokretan_let("fajl.txt", "|", {23: {"sifra": 23,
                                            "broj_leta": "ss11",
                                            "datum_i_vreme_polaska": datetime(2000, 1, 10, 13, 30, 3),
                                            "datum_i_vreme_dolaska": datetime(2000, 1, 12, 13, 30, 3),
                                            "zauazetost": [[False, False], [False, False]]}})

sacuvaj_kokretan_let("fajl.txt", "|", {24: {"sifra": 24,
                                            "broj_leta": "ss11",
                                            "datum_i_vreme_polaska": datetime(2000, 1, 10, 13, 30, 3),
                                            "datum_i_vreme_dolaska": datetime(2000, 1, 12, 13, 30, 3),
                                            "zauazetost": [[False, False], [False, False]]}})

sacuvaj_kokretan_let("fajl.txt", "|", {23: {"sifra": 23,
                                            "broj_leta": "ss11",
                                            "datum_i_vreme_polaska": datetime(2000, 1, 10, 13, 30, 3),
                                            "datum_i_vreme_dolaska": datetime(2000, 1, 12, 13, 30, 3),
                                            "zauazetost": [[False, False], [False, False]]}})


dicty = ucitaj_konkretan_let("fajl.txt", "|")

for d in dicty:
    print(dicty[d]) 
    print("\n")
    
#print(dicty)
"""
