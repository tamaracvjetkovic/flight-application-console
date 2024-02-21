
from datetime import datetime, date, timedelta

import copy
import os
import random
import unittest
from random import randint

from test.test_utils import rand_str, rand_valid_user, rand_time_str, rand_seat_positions, rand_datetime


import csv


def pregled_nerealizovanih_letova(konkretni_letovi: dict):
    now = datetime.now()
    today = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    lista = []
    for let in konkretni_letovi:
        if konkretni_letovi[let]["datum_i_vreme_polaska"] > today:
            lista.append(konkretni_letovi[let])
            
    return lista


def pregled_svih_letova(svi_letovi: dict):
    lista = [["LET", "ŠPA", "ŠOA", "POLEĆE", "SLEĆE", "DPO", "DKO", "PREVOZNIK", "MODEL", "CENA"]] 
    for let in svi_letovi:
        x1 = svi_letovi[let]["broj_leta"]
        x2 = svi_letovi[let]["sifra_polazisnog_aerodroma"]
        x3 = svi_letovi[let]["sifra_odredisnog_aerodorma"]
        x4 = svi_letovi[let]["vreme_poletanja"] + "h"
        x5 = svi_letovi[let]["vreme_sletanja"] + "h"
        x6 = svi_letovi[let]["datum_pocetka_operativnosti"]
        x7 = svi_letovi[let]["datum_kraja_operativnosti"]
        x8 = svi_letovi[let]["prevoznik"]
        x10 = svi_letovi[let]["model"]["naziv"]
        x111 = svi_letovi[let]["cena"]
        x11 = float("{:.2f}".format(x111))
        lista.append([x1, x2, x3, x4, x5, x6, x7, x8, x10, x11])
        
    return lista


"""
Funkcija koja omogucuje korisniku da pregleda informacije o letovima
Ova funkcija sluzi samo za prikaz
"""
def pregled_nerealizoivanih_letova(svi_letovi: dict):
    now = datetime.now()
    today = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    lista = []
    for let in svi_letovi:
        if svi_letovi[let]["datum_pocetka_operativnosti"] > today:
            lista.append(svi_letovi[let])
    return lista


def pretraga_letova_proveri_sve(svi_letovi: dict, konkretni_letovi: dict, polaziste: str = "",
                                odrediste: str = "", datum_polaska: str = "",
                                datum_dolaska: str = "", vreme_poletanja: str = "",
                                vreme_sletanja: str = "", prevoznik: str = "") -> tuple[list, list]:
    listaParametara = []
    # SIFRA POLAZISNOG aerodorma        
    if polaziste is not None and polaziste != "":
        s = "polazištu: '" + str(polaziste) + "'"
        listaParametara.append(s)
        if len(polaziste) != 3:
            raise Exception("GREŠKA: 'šifra polazišnog aerodroma' nije dobro definisano. Unesite ponovo.")
        for i in range(0, 3):
            if ord(polaziste[i].lower()) < 97 or ord(polaziste[i].lower()) > 122:
                raise Exception("GREŠKA: 'šifra polazišnog aerodroma' nije dobro definisano. Unesite ponovo.")    
    
        # SIFRA ODREDISNOG aerodorma
    if odrediste is not None and odrediste != "":
        s = "odredištu: '" + str(odrediste) + "'"
        listaParametara.append(s)
        if len(odrediste) != 3:
            raise Exception("GREŠKA: 'šifra odredišnog aerodroma' nije dobro definisano. Unesite ponovo.")
        for i in range(0, 3):
            if ord(odrediste[i].lower()) < 97 or ord(odrediste[i].lower()) > 122:
                raise Exception("GREŠKA: 'šifra odredišnog aerodroma' nije dobro definisano. Unesite ponovo.") 
    
    if datum_polaska is not None and datum_polaska != "":
        s = "datumu polaska: '" + str(datum_polaska) + "'"
        listaParametara.append(s)
        try:
            datumPolaska = datetime.strptime(datum_polaska, '%Y-%m-%d')
        except ValueError:
            raise Exception("GREŠKA: 'datum polaska' nije definisano u formatu 'YYYY-MM-DD'. Unesite ponovo.")     
        
    if datum_dolaska is not None and datum_dolaska != "":   
        s = "datumu dolaska: '" + str(datum_dolaska) + "'"
        listaParametara.append(s)   
        try:
            datumDolaska = datetime.strptime(datum_dolaska, '%Y-%m-%d')
        except ValueError:
            raise Exception("GREŠKA: 'datum polaska' nije definisano u formatu 'YYYY-MM-DD'. Unesite ponovo.")
        
        # VREME POLETANJA
    if vreme_poletanja is not None and vreme_poletanja != "":
        s = "vremenu poletanja: '" + str(vreme_poletanja) + "'"
        listaParametara.append(s)
        if len(vreme_poletanja) != 5:
            raise Exception("GREŠKA: 'vreme poletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.") 
        if vreme_poletanja[2] != ":":
            raise Exception("GREŠKA: 'vreme poletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.") 
        if vreme_poletanja[0] == "0":
            if ord(vreme_poletanja[1]) < 48 or ord(vreme_poletanja[1]) > 57:
                raise Exception("GREŠKA: 'vreme poletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")     
        elif vreme_poletanja[0] == "1":
            if ord(vreme_poletanja[1]) < 48 or ord(vreme_poletanja[1]) > 57:
                raise Exception("GREŠKA: 'vreme poletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
        elif vreme_poletanja[0] == "2":
            if ord(vreme_poletanja[1]) < 48 or ord(vreme_poletanja[1]) > 52:
                raise Exception("GREŠKA: 'vreme poletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
        else:
            raise Exception("GREŠKA: 'vreme poletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
        if ord(vreme_poletanja[3]) < 48 or ord(vreme_poletanja[3]) > 53:
            raise Exception("GREŠKA: 'vreme poletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
        if ord(vreme_poletanja[4]) < 48 or ord(vreme_poletanja[4]) > 57:
            raise Exception("GREŠKA: 'vreme poletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
            
            
        # VREME SLETANJA
    if vreme_sletanja is not None and vreme_sletanja != "":
        s = "vremenu sletanja: '" + str(vreme_sletanja) + "'"
        listaParametara.append(s)
        if len(vreme_sletanja) != 5:
            raise Exception("GREŠKA: 'vreme sletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.") 
        if vreme_sletanja[2] != ":":
            raise Exception("GREŠKA: 'vreme sletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.") 
        if vreme_sletanja[0] == "0":
            if ord(vreme_sletanja[1]) < 48 or ord(vreme_sletanja[1]) > 57:
                raise Exception("GREŠKA: 'vreme sletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")     
        elif vreme_sletanja[0] == "1":
            if ord(vreme_sletanja[1]) < 48 or ord(vreme_sletanja[1]) > 57:
                raise Exception("GREŠKA: 'vreme sletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
        elif vreme_sletanja[0] == "2":
            if ord(vreme_sletanja[1]) < 48 or ord(vreme_sletanja[1]) > 52:
                raise Exception("GREŠKA: 'vreme sletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
        else:
            raise Exception("GREŠKA: 'vreme sletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
        if ord(vreme_sletanja[3]) < 48 or ord(vreme_sletanja[3]) > 53:
            raise Exception("GREŠKA: 'vreme sletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
        if ord(vreme_sletanja[4]) < 48 or ord(vreme_sletanja[4]) > 57:
            raise Exception("GREŠKA: 'vreme sletanja' nije definisano u formatu 'hh:mm'. Unesite ponovo.")
    
        # PREVOZNIK
    if prevoznik is not None and prevoznik != "":  
        s = "prevozniku: '" + str(prevoznik) + "'"
        listaParametara.append(s) 
        for i in range(0, len(prevoznik)):
            if ord(prevoznik[i].lower()) < 97 or ord(prevoznik[i].lower()) > 122:
                raise Exception("GREŠKA: 'prevoznik' nije dobro definisano. Unesite ponovo.")
    
    polazisteOk = 1
    if polaziste is not None and polaziste != "":    
        polazisteOk = 0
        
    odredisteOk = 1     
    if odrediste is not None and odrediste != "":    
        odredisteOk = 0
        
    vremePoletanjaOk = 1       
    if vreme_poletanja is not None and vreme_poletanja != "":    
        vremePoletanjaOk = 0
        
    vremeSletanjaOk = 1
    if vreme_sletanja is not None and vreme_sletanja != "":    
        vremeSletanjaOk = 0
        
    prevoznikOk = 1     
    if prevoznik is not None and prevoznik != "":    
        prevoznikOk = 0
                
    for let in svi_letovi:
        if polazisteOk == 0 and polaziste == svi_letovi[let]["sifra_polazisnog_aerodroma"]:
            polazisteOk = 1
        if odredisteOk == 0 and odrediste == svi_letovi[let]["sifra_odredisnog_aerodorma"]:
            odredisteOk = 1   
        if vremePoletanjaOk == 0 and vreme_poletanja == svi_letovi[let]["vreme_poletanja"]:
            vremePoletanjaOk = 1 
        if vremeSletanjaOk == 0 and vreme_sletanja == svi_letovi[let]["vreme_sletanja"]:
            vremeSletanjaOk = 1  
        if prevoznikOk == 0 and prevoznik == svi_letovi[let]["prevoznik"]:
            prevoznikOk = 1
            
    datumPolaskaOk = 1   
    datum_polaska1 = 0
    if datum_polaska is not None and datum_polaska != "":    
        datumPolaskaOk = 0
        datum_polaska1 = datetime.strptime(datum_polaska, "%Y-%m-%d")
        
    datumDolaskaOk = 1     
    datum_dolaska1 = 0
    if datum_dolaska is not None and datum_dolaska != "":    
        datumDolaskaOk = 0       
        datum_dolaska1 = datetime.strptime(datum_dolaska, "%Y-%m-%d")
          
    for let in konkretni_letovi:
        datumPolaska1 = konkretni_letovi[let]['datum_i_vreme_polaska']
        datumPolaska = datetime(datumPolaska1.year, datumPolaska1.month, datumPolaska1.day)  
        datumDolaska1 = konkretni_letovi[let]['datum_i_vreme_dolaska']
        datumDolaska = datetime(datumDolaska1.year, datumDolaska1.month, datumDolaska1.day)
        if datumPolaskaOk == 0 and datum_polaska1 == datumPolaska:
            datumPolaskaOk = 1
        if datumDolaskaOk == 0 and datum_dolaska1 == datumDolaska:
            datumDolaskaOk = 1       
    
    if polazisteOk == 0:
        raise Exception("GREŠKA: unesena 'šifra polazišnog aerodroma' ne postoji. Unesite ponovo.") 
    if odredisteOk == 0:
        raise Exception("GREŠKA: uneseno 'šifra odredišnog aerodroma' ne postoji. Unesite ponovo.") 
    if vremePoletanjaOk == 0:
        raise Exception("GREŠKA: uneseno 'vreme poletanja' ne postoji. Unesite ponovo.")
    if vremeSletanjaOk == 0:
        raise Exception("GREŠKA: uneseno 'vreme sletanja' ne postoji. Unesite ponovo.")
    if prevoznikOk == 0:
        raise Exception("GREŠKA: unesen 'prevoznik' ne postoji. Unesite ponovo.") 
    if datumPolaskaOk == 0:
        raise Exception("GREŠKA: unesen 'datum polaska' ne postoji. Unesite ponovo.")
    if datumDolaskaOk == 0:
        raise Exception("GREŠKA: unesen 'datum polaska' ne postoji. Unesite ponovo.")
    
    sifreOkLetova = {-1}
    listaLetova = []      
    for let in konkretni_letovi:
        ok = 0
        brojLeta = konkretni_letovi[let]['broj_leta']
        if polaziste != "" and polaziste is not None:      
            if svi_letovi[brojLeta]['sifra_polazisnog_aerodroma'] == polaziste:
                ok = 1 
            else:
                continue  
        if odrediste != "" and odrediste is not None:
            if svi_letovi[brojLeta]['sifra_odredisnog_aerodorma'] == odrediste:
                ok = 1
            else:
                continue
        if datum_polaska != "" and datum_polaska is not None:          
            datumPolaska1 = konkretni_letovi[let]['datum_i_vreme_polaska']
            datumPolaska = datetime(datumPolaska1.year, datumPolaska1.month, datumPolaska1.day) 
            if datum_polaska1 != 0 and datumPolaska == datum_polaska1:
                ok = 1 
            else:
                continue
        if datum_dolaska != "" and datum_dolaska is not None:        
            datumDolaska1 = konkretni_letovi[let]['datum_i_vreme_dolaska']
            datumDolaska = datetime(datumDolaska1.year, datumDolaska1.month, datumDolaska1.day) 
            if datum_dolaska1 != 0 and datumDolaska == datum_dolaska1:
                ok = 1
            else:
                continue
        if vreme_poletanja != "" and vreme_poletanja is not None:        
            if svi_letovi[brojLeta]['vreme_poletanja'] == vreme_poletanja:
                ok = 1  
            else:
                continue
        if vreme_sletanja != "" and vreme_sletanja is not None:          
            if svi_letovi[brojLeta]['vreme_sletanja'] == vreme_sletanja:
                ok = 1      
            else:
                continue 
        if prevoznik != "" and prevoznik is not None:          
            if svi_letovi[brojLeta]['prevoznik'] == prevoznik:
                ok = 1 
            else:
                continue     
        if ok == 1:
            sifreOkLetova.add(let)   
    sifreOkLetova.remove(-1)  
    sifreOkLetova = sorted(sifreOkLetova)        
    for i in sifreOkLetova:
        brojLeta = konkretni_letovi[i]["broj_leta"]
        noviDict = {"sifra": konkretni_letovi[i]["sifra"], 
                    "broj_leta": brojLeta, 
                    "sifra_polazisnog_aerodroma": svi_letovi[brojLeta]["sifra_polazisnog_aerodroma"],
                    "sifra_odredisnog_aerodorma": svi_letovi[brojLeta]["sifra_odredisnog_aerodorma"],
                    "datum_i_vreme_polaska": konkretni_letovi[i]['datum_i_vreme_polaska'], 
                    "datum_i_vreme_dolaska": konkretni_letovi[i]['datum_i_vreme_dolaska'],
                    "prevoznik": svi_letovi[brojLeta]["prevoznik"],
                    "cena": float("{:.2f}".format(svi_letovi[brojLeta]["cena"]))}
        listaLetova.append(noviDict)   
    
    return (listaLetova, listaParametara)


"""
Funkcija koja omogucava pretragu leta po zadatim kriterijumima.
Korisnik moze da zada jedan ili vise kriterijuma.
Povratna vrednost je lista konkretnih letova.
vreme_poletanja i vreme_sletanja su u formatu hh:mm
"""
def pretraga_letova(svi_letovi: dict, konkretni_letovi: dict, polaziste: str = "", odrediste: str = "",
                    datum_polaska: datetime = None, datum_dolaska: datetime = None,
                    vreme_poletanja: str = "", vreme_sletanja: str = "", prevoznik: str = "") -> list:
    sifreOkLetova = {-1}
    listaLetova = []
    for let in konkretni_letovi:
        ok = 0
        brojLeta = konkretni_letovi[let]['broj_leta']
        if svi_letovi[brojLeta]['sifra_polazisnog_aerodroma'] == polaziste:
            ok = 1    
        if svi_letovi[brojLeta]['sifra_odredisnog_aerodorma'] == odrediste:
            ok = 1
        if konkretni_letovi[let]['datum_i_vreme_polaska'] == datum_polaska:
            ok = 1
        if konkretni_letovi[let]['datum_i_vreme_dolaska'] == datum_dolaska:
            ok = 1
        if svi_letovi[brojLeta]['vreme_poletanja'] == vreme_poletanja:
            ok = 1    
        if svi_letovi[brojLeta]['vreme_sletanja'] == vreme_sletanja:
            ok = 1       
        if svi_letovi[brojLeta]['prevoznik'] == prevoznik:
            ok = 1      
        if ok == 1:
            sifreOkLetova.add(let)   
    sifreOkLetova.remove(-1)           
    for i in sifreOkLetova:
        brojLeta = konkretni_letovi[i]["broj_leta"]
        noviDict = {"sifra": konkretni_letovi[i]["sifra"], 
                    "broj_leta": brojLeta, 
                    #"sifra_polazisnog_aerodroma": svi_letovi[brojLeta]["sifra_polazisnog_aerodroma"],
                    #"sifra_odredisnog_aerodorma": svi_letovi[brojLeta]["sifra_odredisnog_aerodorma"],
                    "datum_i_vreme_polaska": konkretni_letovi[i]['datum_i_vreme_polaska'], 
                    "datum_i_vreme_dolaska": konkretni_letovi[i]['datum_i_vreme_dolaska']}
                    #"prevoznik": svi_letovi[brojLeta]["prevoznik"],
                    #"cena": float("{:.2f}".format(svi_letovi[brojLeta]["cena"]))}
        listaLetova.append(noviDict)    
        
    return listaLetova


"""
Funkcija koja kreira novi rečnik koji predstavlja let sa prosleđenim vrednostima. Kao rezultat vraća kolekciju
svih letova proširenu novim letom. 
Ova funkcija proverava i validnost podataka o letu. Paziti da kada se kreira let, da se kreiraju i njegovi konkretni letovi.
vreme_poletanja i vreme_sletanja su u formatu hh:mm
CHECKPOINT2: Baca grešku sa porukom ako podaci nisu validni.
"""
def kreiranje_letova(svi_letovi : dict, broj_leta: str, sifra_polazisnog_aerodroma: str,
                     sifra_odredisnog_aerodorma: str,
                     vreme_poletanja: str, vreme_sletanja: str, sletanje_sutra: str, prevoznik: str,
                     dani: list, model: dict, cena: float,  datum_pocetka_operativnosti: datetime = None ,
                     datum_kraja_operativnosti: datetime = None):
        # BROJ LETA
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
    if broj_leta in svi_letovi:
        raise Exception("GRESKA: 'broj_leta' vec postoji. Unesite ponovo.")         
         
        # SIFRA POLAZISNOG aerodorma
    if sifra_polazisnog_aerodroma is None or sifra_polazisnog_aerodroma == "":
        raise Exception("GRESKA: 'šifra_polazišnog_aerodroma' je prazno. Unesite ponovo.")
    if len(sifra_polazisnog_aerodroma) != 3:
        raise Exception("GRESKA: 'šifra_polazišnog_aerodroma' nije dobro definisano. Unesite ponovo.")
    for i in range(0, 3):
        if ord(sifra_polazisnog_aerodroma[i].lower()) < 97 or ord(sifra_polazisnog_aerodroma[i].lower()) > 122:
            raise Exception("GRESKA: 'šifra_polazišnog_aerodroma' nije dobro definisano. Unesite ponovo.")    
    
        # SIFRA ODREDISNOG aerodorma
    if sifra_odredisnog_aerodorma is None or sifra_odredisnog_aerodorma == "":
        raise Exception("GRESKA: 'šifra_odredišnog_aerodroma' je prazno. Unesite ponovo.") 
    if len(sifra_odredisnog_aerodorma) != 3:
        raise Exception("GRESKA: 'šifra_odredišnog_aerodroma' nije dobro definisano. Unesite ponovo.")
    for i in range(0, 3):
        if ord(sifra_odredisnog_aerodorma[i].lower()) < 97 or ord(sifra_odredisnog_aerodorma[i].lower()) > 122:
            raise Exception("GRESKA: 'šifra_odredišnog_aerodroma' nije dobro definisano. Unesite ponovo.") 
    
        # VREME POLETANJA
    if vreme_poletanja is None or vreme_poletanja == "":
        raise Exception("GRESKA: 'vreme_poletanja' je prazno. Unesite ponovo.") 
    if len(vreme_poletanja) != 5:
        raise Exception("GRESKA: 'vreme_poletanja' nije dobro definisano. Unesite ponovo.") 
    for i in range(0, 5):
        if i == 2:
            if ord(vreme_poletanja[i]) != 58:
                raise Exception("GRESKA: 'vreme_poletanja' nije dobro definisano. Unesite ponovo.")
            continue
        if ord(vreme_poletanja[i]) < 48 or ord(vreme_poletanja[i]) > 57:
            raise Exception("GRESKA: 'vreme_poletanja' nije dobro definisano. Unesite ponovo.")
    
        # VREME SLETANJA
    if vreme_sletanja is None or vreme_sletanja == "":
        raise Exception("GRESKA: 'vreme_sletanja' je prazno. Unesite ponovo.") 
    if len(vreme_sletanja) != 5:
        raise Exception("GRESKA: 'vreme_sletanja' nije dobro definisano. Unesite ponovo.") 
    for i in range(0, 5):
        if i == 2:
            if ord(vreme_sletanja[i]) != 58:
                raise Exception("GRESKA: 'vreme_sletanja' nije dobro definisano. Unesite ponovo.")
            continue
        if ord(vreme_sletanja[i]) < 48 or ord(vreme_sletanja[i]) > 57:
            raise Exception("GRESKA: 'vreme_sletanja' nije dobro definisano. Unesite ponovo.")
    
        # SLETANJE SUTRA
    if sletanje_sutra is None:
        raise Exception("GRESKA: 'sletanje_sutra' je prazno. Unesite ponovo.")
    if type(sletanje_sutra) is str:
        if sletanje_sutra == "False":
            sletanje_sutra = False
        elif sletanje_sutra == "True":
            sletanje_sutra = True
        else: 
            raise Exception("GRESKA: 'sletanje_sutra' nije dobro definisano. Unesite ponovo.") 
    
        # PREVOZNIK
    if prevoznik is None or prevoznik == "":
        raise Exception("GRESKA: 'prevoznik' je prazno. Unesite ponovo.")
    for i in range(0, len(prevoznik)):
        if ord(prevoznik[i].lower()) < 97 or ord(prevoznik[i].lower()) > 122:
            raise Exception("GRESKA: 'prevoznik' nije dobro definisano. Unesite ponovo.")
    
        # DANI
    if dani is None or len(dani) == 0:
        raise Exception("GRESKA: 'dani' je prazno. Unesite ponovo.") 
    if len(dani) > 7:
        raise Exception("GRESKA: 'dani' nije dobro definisano. Unesite ponovo.")
    for i in dani:
        if i < 0 or i > 6:
            raise Exception("GRESKA: 'dani' nije dobro definisano. Unesite ponovo.")    
    
        # MODEL
    if model is None or len(model) == 0:
        raise Exception("GRESKA: 'model' je prazno. Unesite ponovo.") 
    
        # CENA
    if cena is None or cena == "":
        raise Exception("GRESKA: 'cena' je prazno. Unesite ponovo.")
    try:
        cena2 = float(cena)
        if cena2 <= 0:
            raise Exception("GRESKA: 'cena' nije dobro definisana. Unesite ponovo.")
    except ValueError:
        raise Exception("GRESKA: 'cena' nije dobro definisana. Unesite ponovo.")    
    
        # DATUM POCETKA OPERATIVNOSTI
    if datum_kraja_operativnosti < datum_pocetka_operativnosti:
        raise Exception("GRESKA: 'datum kraja operativnosti' nije dobro definisano. Unesite ponovo.")
    
        # VALJA SVE, KREIRAMO NOVI DICT
    newDict = {broj_leta: {"broj_leta": broj_leta,
                           "sifra_polazisnog_aerodroma": sifra_polazisnog_aerodroma,
                           "sifra_odredisnog_aerodorma": sifra_odredisnog_aerodorma,
                           "vreme_poletanja": vreme_poletanja,
                           "vreme_sletanja": vreme_sletanja,
                           "datum_pocetka_operativnosti": datum_pocetka_operativnosti,
                           "datum_kraja_operativnosti": datum_kraja_operativnosti,
                           "sletanje_sutra": sletanje_sutra,
                           "prevoznik": prevoznik,
                           "dani": dani,
                           "model": model,
                           "cena": float(cena)}}
    svi_letovi.update(newDict);
    
        # -------- VRATI (dict) -------- 
    return svi_letovi


"""
Funkcija koja menja let sa prosleđenim vrednostima. Kao rezultat vraća kolekciju
svih letova sa promenjenim letom. 
Ova funkcija proverava i validnost podataka o letu.
vreme_poletanja i vreme_sletanja su u formatu hh:mm
CHECKPOINT2: Baca grešku sa porukom ako podaci nisu validni.
"""
def izmena_letova(svi_letovi : dict, broj_leta: str, sifra_polazisnog_aerodroma: str, 
                  sifra_odredisnog_aerodorma: str, vreme_poletanja: str, vreme_sletanja: str, 
                  sletanje_sutra: bool, prevoznik: str, dani: list, model: dict, cena: float, 
                  datum_pocetka_operativnosti: datetime, datum_kraja_operativnosti: datetime) -> dict:
        # BROJ LETA
    if broj_leta not in svi_letovi:
        raise Exception("GRESKA: 'broj_leta' ne postoji. Unesite ponovo.")    
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
         
        # SIFRA POLAZISNOG aerodorma
    if sifra_polazisnog_aerodroma is None or sifra_polazisnog_aerodroma == "":
        raise Exception("GRESKA: 'sifra_polazisnog_aerodroma' je prazno. Unesite ponovo.")
    if len(sifra_polazisnog_aerodroma) != 3:
        raise Exception("GRESKA: 'sifra_polazisnog_aerodroma' nije dobro definisano. Unesite ponovo.")
    for i in range(0, 3):
        if ord(sifra_polazisnog_aerodroma[i].lower()) < 97 or ord(sifra_polazisnog_aerodroma[i].lower()) > 122:
            raise Exception("GRESKA: 'sifra_polazisnog_aerodroma' nije dobro definisano. Unesite ponovo.")    
    
        # SIFRA ODREDISNOG aerodorma
    if sifra_odredisnog_aerodorma is None or sifra_odredisnog_aerodorma == "":
        raise Exception("GRESKA: 'sifra_odredisnog_aerodorma' je prazno. Unesite ponovo.") 
    if len(sifra_odredisnog_aerodorma) != 3:
        raise Exception("GRESKA: 'sifra_odredisnog_aerodorma' nije dobro definisano. Unesite ponovo.")
    for i in range(0, 3):
        if ord(sifra_odredisnog_aerodorma[i].lower()) < 97 or ord(sifra_odredisnog_aerodorma[i].lower()) > 122:
            raise Exception("GRESKA: 'sifra_odredisnog_aerodorma' nije dobro definisano. Unesite ponovo.") 
    
        # VREME POLETANJA
    if vreme_poletanja is None or vreme_poletanja == "":
        raise Exception("GRESKA: 'vreme_poletanja' je prazno. Unesite ponovo.") 
    if len(vreme_poletanja) != 5:
        raise Exception("GRESKA: 'vreme_poletanja' nije dobro definisano. Unesite ponovo.") 
    for i in range(0, 5):
        if i == 2:
            if ord(vreme_poletanja[i]) != 58:
                raise Exception("GRESKA: 'vreme_poletanja' nije dobro definisano. Unesite ponovo.")
            continue
        if ord(vreme_poletanja[i]) < 48 or ord(vreme_poletanja[i]) > 57:
            raise Exception("GRESKA: 'vreme_poletanja' nije dobro definisano. Unesite ponovo.")
    
        # VREME SLETANJA
    if vreme_sletanja is None or vreme_sletanja == "":
        raise Exception("GRESKA: 'vreme_sletanja' je prazno. Unesite ponovo.") 
    if len(vreme_sletanja) != 5:
        raise Exception("GRESKA: 'vreme_sletanja' nije dobro definisano. Unesite ponovo.") 
    for i in range(0, 5):
        if i == 2:
            if ord(vreme_sletanja[i]) != 58:
                raise Exception("GRESKA: 'vreme_sletanja' nije dobro definisano. Unesite ponovo.")
            continue
        if ord(vreme_sletanja[i]) < 48 or ord(vreme_sletanja[i]) > 57:
            raise Exception("GRESKA: 'vreme_sletanja' nije dobro definisano. Unesite ponovo.")
    
        # SLETANJE SUTRA
    if sletanje_sutra is None:
        raise Exception("GRESKA: 'sletanje_sutra' je prazno. Unesite ponovo.") 
    if sletanje_sutra != False and sletanje_sutra != True:
        raise Exception("GRESKA: 'sletanje_sutra' je prazno. Unesite ponovo.") 
    
        # PREVOZNIK
    if prevoznik is None or prevoznik == "":
        raise Exception("GRESKA: 'prevoznik' je prazno. Unesite ponovo.")
    for i in range(0, len(prevoznik)):
        if ord(prevoznik[i].lower()) < 97 or ord(prevoznik[i].lower()) > 122:
            raise Exception("GRESKA: 'vreme_poletanja' nije dobro definisano. Unesite ponovo.")
    
        # DANI
    if dani is None:
        raise Exception("GRESKA: 'dani' je prazno. Unesite ponovo.") 
    if len(dani) > 7 or len(dani) == 0:
        raise Exception("GRESKA: 'dani' nije dobro definisano. Unesite ponovo.")
    for i in dani:
        if i < 0 or i > 6:
            raise Exception("GRESKA: 'dani' nije dobro definisano. Unesite ponovo.")    
    
        # MODEL
    if model is None or len(model) == 0:
        raise Exception("GRESKA: 'model' je prazno. Unesite ponovo.") 
    
    if cena is None or cena == "":
        raise Exception("GRESKA: 'cena' je prazno. Unesite ponovo.")
    try:
        cena2 = float(cena)
        if cena2 <= 0:
            raise Exception("GRESKA: 'cena' nije dobro definisana. Unesite ponovo.")
    except ValueError:
        raise Exception("GRESKA: 'cena' nije dobro definisana. Unesite ponovo.")    
    
    if datum_kraja_operativnosti < datum_pocetka_operativnosti:
        raise Exception("GRESKA: 'datum_operativnosti' nije dobro definisano. Unesite ponovo.")
    
        # VALJA SVE
    newDict = {broj_leta: {"broj_leta": broj_leta,
                           "sifra_polazisnog_aerodroma": sifra_polazisnog_aerodroma,
                           "sifra_odredisnog_aerodorma": sifra_odredisnog_aerodorma,
                           "vreme_poletanja": vreme_poletanja,
                           "vreme_sletanja": vreme_sletanja,
                           "datum_pocetka_operativnosti": datum_pocetka_operativnosti,
                           "datum_kraja_operativnosti": datum_kraja_operativnosti,
                           "sletanje_sutra": sletanje_sutra,
                           "prevoznik": prevoznik,
                           "dani": dani,
                           "model": model,
                           "cena": cena}}
    svi_letovi.update(newDict); 
    
        # -------- VRATI (dict) --------
    return svi_letovi


"""
Funkcija koja cuva sve letove na zadatoj putanji
"""
def sacuvaj_letove(putanja: str, separator: str, svi_letovi: dict):
    fields = ["broj_leta", "sifra_polazisnog_aerodroma", "sifra_odredisnog_aerodorma",
              "vreme_poletanja", "vreme_sletanja", "datum_pocetka_operativnosti",
              "datum_kraja_operativnosti", "sletanje_sutra", "prevoznik", "dani", "model", "cena"]
    with open(putanja, 'a', newline = "") as f:
        w = csv.DictWriter(f, fieldnames = fields, delimiter = separator)
        #w.writeheader()
        for i in svi_letovi:
            w.writerow(svi_letovi[i])
            
    return


"""
Funkcija koja učitava sve letove iz fajla i vraća ih u rečniku.
"""
def ucitaj_letove_iz_fajla(putanja: str, separator: str) -> dict:
    myDict = {}
    with open(putanja, 'r') as f:
        r = csv.reader(f, delimiter = separator)
        for i in r:
            sletanjeSutra = False
            if i[7] == True:
                sletanjeSutra = True
            cenaFloat = float(i[11])
            datumPocetkaOperativnosti = datetime.strptime(i[5], '%Y-%m-%d %H:%M:%S')
            datumKrajaOperativnosti = datetime.strptime(i[6], '%Y-%m-%d %H:%M:%S')
            newDict = {"broj_leta": i[0],
                       "sifra_polazisnog_aerodroma": i[1],
                       "sifra_odredisnog_aerodorma": i[2],
                       "vreme_poletanja": i[3],
                       "vreme_sletanja": i[4],
                       "datum_pocetka_operativnosti": datumPocetkaOperativnosti,
                       "datum_kraja_operativnosti": datumKrajaOperativnosti,
                       "sletanje_sutra": sletanjeSutra,
                       "prevoznik": i[8],
                       "dani": eval(i[9]),
                       "model": eval(i[10]),
                       "cena": cenaFloat}
            newDict2 = {i[0]: newDict}
            myDict.update(newDict2)
            
    return myDict


"""
Pomoćna funkcija koja podešava matricu zauzetosti leta tako da sva mesta budu slobodna.
Prolazi kroz sve redove i sve poziciej sedišta i postavlja ih na "nezauzeto".
"""
def podesi_matricu_zauzetosti(svi_letovi: dict, konkretni_let: dict):
    matr = []
    red = []
    brojLeta = konkretni_let["broj_leta"]
    modelAviona = svi_letovi[brojLeta]["model"]
    brojRedova = modelAviona["broj_redova"]
    pozicijeSedista = modelAviona["pozicije_sedista"]
    brojSedista = len(pozicijeSedista)
    for i in range(0, brojSedista):
        red.append(False)
    for i in range(0, brojRedova):
        matr.append(red)
    konkretni_let["zauzetost"] = matr
    
    return

"""
Funkcija koja vraća matricu zauzetosti sedišta. Svaka stavka sadrži oznaku pozicije i oznaku reda.
Primer: [[True, False], [False, True]] -> A1 i B2 su zauzeti, A2 i B1 su slobodni
"""
def matrica_zauzetosti(konkretni_let: dict) -> list:
    return konkretni_let["zauzetost"]


"""
Funkcija koja zauzima sedište na datoj poziciji u redu, najkasnije 48h pre poletanja. Redovi počinju od 1. 
Vraća grešku ako se sedište ne može zauzeti iz bilo kog razloga.
"""
def checkin(karta, svi_letovi: dict, konkretni_let: dict, red: int,
            pozicija: str) -> tuple[dict, dict]:
    brojLeta = konkretni_let["broj_leta"]
    model = svi_letovi[brojLeta]["model"]
    pos = 0
    for i in model["pozicije_sedista"]:
        if i == pozicija:
            break;
        pos += 1
        
    matrica = konkretni_let["zauzetost"]    
    if matrica[red - 1][pos] == True:
        raise Exception("GRESKA: uneseno sedište je već zauzeto! Unesite ponovo.")
    
    today = datetime.now() + timedelta(hours = 48)
    if today < konkretni_let["datum_i_vreme_polaska"]:
        raise Exception("GREŠKA: Nije moguće uraditi check-in!\nCheck-in se može obaviti najranije 48h pre poletanja.\n\n")
    
    karta["sediste"] = str(pozicija + str(red))
    matrica[red - 1][pos] = True
    konkretni_let["zauzetost"] = matrica

    return (konkretni_let, karta)


"""
Funkcija koja vraća listu konkretnih letova koji zadovoljavaju sledeće uslove:
1. Polazište im je jednako odredištu prosleđenog konkretnog leta
2. Vreme i mesto poletanja im je najviše 120 minuta nakon sletanja konkretnog leta
"""
def povezani_letovi(svi_letovi: dict, svi_konkretni_letovi: dict, konkretni_let: dict) -> list:
    if konkretni_let["broj_leta"] not in svi_letovi:
        raise Exception("GRESKA: 'konkretni_let' nije dobro definisano. Unesite ponovo.")

    lista = []
    ok = 0
    odrediste = svi_letovi[konkretni_let["broj_leta"]]["sifra_odredisnog_aerodorma"]
    sletanje = konkretni_let["datum_i_vreme_dolaska"]
    sletanje2 = sletanje + timedelta(minutes = 120)
    for let in svi_konkretni_letovi:
        if svi_letovi[svi_konkretni_letovi[let]["broj_leta"]]["sifra_polazisnog_aerodroma"] == odrediste:
            ok += 1
        poletanje = svi_konkretni_letovi[let]["datum_i_vreme_polaska"]
        if poletanje <= sletanje2 and poletanje >= sletanje:
            ok += 1 
        if ok == 2:
            lista.append(svi_konkretni_letovi[let])    
        ok = 0
     
    newLista = [["ŠIFRA", "LET", "ŠPA", "ŠOA", "POLETANJE", "SLETANJE", "PREVOZNIK", "MODEL", " CENA "]]
# ["BROJ", "LET", "ŠPA", "ŠOA", "POLETANJE", "SLETANJE", "PREVOZNIK", "MODEL", " CENA "]   
    #print(lista, "\n")
    for i in lista:
        #print(i, "\n\n")
        brojLeta = i["broj_leta"]
        let = svi_letovi[brojLeta]
        datumPolaska1 = i['datum_i_vreme_polaska']
        datumPolaska = datetime(datumPolaska1.year, datumPolaska1.month, datumPolaska1.day)  
        datumDolaska1 = i['datum_i_vreme_dolaska']
        datumDolaska = datetime(datumDolaska1.year, datumDolaska1.month, datumDolaska1.day) 
        x0 = i["sifra"]            
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
        newLista.append([x0, x1, x2, x3, x6, x7, x8, x10, x11])
                      
    return newLista       


"""
Funkcija koja vraća sve konkretne letove čije je vreme polaska u zadatom opsegu, +/- zadati broj fleksibilnih dana
"""
def fleksibilni_polasci(svi_letovi: dict, konkretni_letovi: dict, polaziste: str, odrediste: str,
                        datum_polaska: date, datum_dolaska: date, broj_fleksibilnih_dana: int) -> list:
    
    if polaziste is None or polaziste == "":
        raise Exception("GRESKA: 'šifra polazišnog aerodroma' je prazno. Unesite ponovo.")
    if len(polaziste) != 3:
        raise Exception("GRESKA: 'šifra polazišnog aerodroma' nije dobro definisano. Unesite ponovo.")
    for i in range(0, 3):
        if ord(polaziste[i].lower()) < 97 or ord(polaziste[i].lower()) > 122:
            raise Exception("GRESKA: 'šifra polazišnog aerodroma' nije dobro definisano. Unesite ponovo.")    
    
        # SIFRA ODREDISNOG aerodorma
    if odrediste is None or odrediste == "":
        raise Exception("GRESKA: 'šifra odredišnog aerodroma' je prazno. Unesite ponovo.") 
    if len(odrediste) != 3:
        raise Exception("GRESKA: 'šifra odredišnog aerodroma' nije dobro definisano. Unesite ponovo.")
    for i in range(0, 3):
        if ord(odrediste[i].lower()) < 97 or ord(odrediste[i].lower()) > 122:
            raise Exception("GRESKA: 'šifra odredišnog aerodroma' nije dobro definisano. Unesite ponovo.")
    
    if datum_polaska is None or datum_polaska == "":
        raise Exception("GRESKA: 'datum polaska' je prazno. Unesite ponovo.")
    
    try:
        datumPolaska = datetime.strptime(datum_polaska, '%Y-%m-%d')
    except ValueError:
        raise Exception("GREŠKA: 'datum polaska' nije definisano u formatu 'YYYY-MM-DD'. Unesite ponovo.")     
       
    if datum_dolaska is None or datum_dolaska == "":
        raise Exception("GRESKA: 'datum dolaska' je prazno. Unesite ponovo.")   
    try:
        datumDolaska = datetime.strptime(datum_dolaska, '%Y-%m-%d')
    except ValueError:
        raise Exception("GREŠKA: 'datum polaska' nije definisano u formatu 'YYYY-MM-DD'. Unesite ponovo.")
    
    polazisteOk = 1
    if polaziste is not None and polaziste != "":    
        polazisteOk = 0
        
    odredisteOk = 1     
    if odrediste is not None and odrediste != "":    
        odredisteOk = 0
                
    for let in svi_letovi:
        if polazisteOk == 0 and polaziste == svi_letovi[let]["sifra_polazisnog_aerodroma"]:
            polazisteOk = 1
        if odredisteOk == 0 and odrediste == svi_letovi[let]["sifra_odredisnog_aerodorma"]:
            odredisteOk = 1   
            
    if polazisteOk == 0:
        raise Exception("GREŠKA: unesena 'šifra polazišnog aerodroma' ne postoji. Unesite ponovo.") 
    if odredisteOk == 0:
        raise Exception("GREŠKA: unesena 'šifra odredišnog aerodroma' ne postoji. Unesite ponovo.") 
    
    if broj_fleksibilnih_dana is None or broj_fleksibilnih_dana == "":
        raise Exception("GREŠKA: 'broj fleksibilnih dana' je prazno. Unesite ponovo.") 
    for i in range(0, len(broj_fleksibilnih_dana)):
        if i == 0 and len(broj_fleksibilnih_dana) != 1:
            if ord(broj_fleksibilnih_dana[i]) == 48:
                raise Exception("GREŠKA: uneseni 'broj fleksibilnih dana' nije u dobrom formatu. Unesite ponovo.") 
        if ord(broj_fleksibilnih_dana[i]) < 48 or ord(broj_fleksibilnih_dana[i]) > 57:
            raise Exception("GREŠKA: 'broj fleksibilnih dana' treba da bude pozitivan celi broj. Unesite ponovo.") 
       
    datumPolaska1 = datetime(datumPolaska.year, datumPolaska.month, datumPolaska.day)  
    datumDolaska1 = datetime(datumDolaska.year, datumDolaska.month, datumDolaska.day)
   
    lista = []
    okLetovi = {}
    date1 = datumPolaska1 - timedelta(days = int(broj_fleksibilnih_dana))
    date2 = datumPolaska1 + timedelta(days = int(broj_fleksibilnih_dana))
    date3 = datumDolaska1 - timedelta(days = int(broj_fleksibilnih_dana))
    date4 = datumDolaska1 + timedelta(days = int(broj_fleksibilnih_dana))
    
    for let in svi_letovi:
        if svi_letovi[let]["sifra_polazisnog_aerodroma"] == polaziste:
            if svi_letovi[let]["sifra_odredisnog_aerodorma"] == odrediste:
                okLetovi[svi_letovi[let]["broj_leta"]] = 1
    
    lista = []
    for i in konkretni_letovi:
        if konkretni_letovi[i]["broj_leta"] in okLetovi:
            datum11 = konkretni_letovi[i]["datum_i_vreme_polaska"]
            datum1 = datetime(datum11.year, datum11.month, datum11.day)
            datum22 = konkretni_letovi[i]["datum_i_vreme_dolaska"]
            datum2 = datetime(datum22.year, datum22.month, datum22.day)
            ok = 0
            if datum1 >= date1 and datum1 <= date2:
                ok = 1
            elif datum2 >= date3 and datum2 <= date4:
                ok = 1
            if ok == 1:
                brojLeta = konkretni_letovi[i]["broj_leta"]
                let = svi_letovi[brojLeta]
                datumPolaska1 = konkretni_letovi[i]['datum_i_vreme_polaska']
                datumPolaska = datetime(datumPolaska1.year, datumPolaska1.month, datumPolaska1.day)  
                datumDolaska1 = konkretni_letovi[i]['datum_i_vreme_dolaska']
                datumDolaska = datetime(datumDolaska1.year, datumDolaska1.month, datumDolaska1.day)             
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
                x10 = let["model"]["naziv"]  # BEZ MODELA, NE MOZE STATI U TABELU SVE
                x111 = let["cena"]
                x11 = float("{:.2f}".format(x111))        
# "BR", "LET", "ŠPA", "ŠOA", "POLETANJE", "SLETANJE", "PREVOZNIK", "MODEL", " CENA "                      
                lista.append([x11, x1, x2, x3, x6, x7, x8, x10, x11])           
    
    lista.sort(reverse = True)  
    newLista = []    
    for l in range(0, len(lista)):
        novi = []
        novi.append(l + 1)
        for i in range(1, 9):
            novi.append(lista[l][i])
        newLista.append(novi)
        
    return newLista


"""
Funkcija koja trazi 10 najjeftinijih letova po opadajucem redosledu
"""
def trazenje_10_najjeftinijih_letova(svi_letovi: dict, polaziste: str = "",
                                     odrediste: str = ""):
        # SIFRA POLAZISNOG AERODROMA
    if polaziste is None or polaziste == "":
        raise Exception("GREŠKA: 'šifra polazišnog aerodroma' ne sme biti prazno. Unesite ponovo.")   
    if len(polaziste) != 3:
        raise Exception("GREŠKA: 'šifra polazišnog aerodroma' nije dobro definisano. Unesite ponovo.")
    for i in range(0, 3):
        if ord(polaziste[i].lower()) < 97 or ord(polaziste[i].lower()) > 122:
            raise Exception("GREŠKA: 'šifra polazišnog aerodroma' nije dobro definisano. Unesite ponovo.")    
    
        # SIFRA ODREDISNOG AERODROMA
    if odrediste is None or odrediste == "":
        raise Exception("GREŠKA: 'šifra odredišnog aerodroma' ne sme biti prazno. Unesite ponovo.")   
    if len(odrediste) != 3:
        raise Exception("GREŠKA: 'šifra odredišnog aerodroma' nije dobro definisano. Unesite ponovo.")
    for i in range(0, 3):
        if ord(odrediste[i].lower()) < 97 or ord(odrediste[i].lower()) > 122:
            raise Exception("GREŠKA: 'šifra odredišnog aerodroma' nije dobro definisano. Unesite ponovo.") 
    
    ok = 0
    for let in svi_letovi:
        if polaziste == svi_letovi[let]["sifra_polazisnog_aerodroma"]:
            ok = 1  
            break
    if ok == 0:
        raise Exception("GREŠKA: unesena 'šifra polazišnog aerodroma' ne postoji. Unesite ponovo.")   
    
    ok = 0
    for let in svi_letovi:
        if odrediste == svi_letovi[let]["sifra_odredisnog_aerodorma"]:
            ok = 1  
            break
    if ok == 0:
        raise Exception("GREŠKA: unesena 'šifra odredišnog aerodroma' ne postoji. Unesite ponovo.")
    
    ok = 0
    for let in svi_letovi:
        if polaziste == svi_letovi[let]["sifra_polazisnog_aerodroma"] and odrediste == svi_letovi[let]["sifra_odredisnog_aerodorma"]:
            ok = 1  
            break
    if ok == 0:
        raise Exception("GREŠKA: relacija između unesenih šifri polazišnog i odredišnog aerodroma ne postoji. \n Unesite ponovo.")   
         
    lista = []
    for let in svi_letovi:
        brojLeta = svi_letovi[let]["broj_leta"]
        cenaLeta = svi_letovi[let]["cena"]
        if svi_letovi[let]["sifra_polazisnog_aerodroma"] == polaziste and svi_letovi[let]["sifra_odredisnog_aerodorma"] == odrediste:
            pair = (cenaLeta, brojLeta)
            lista.append(pair)
    arr = sorted(lista, key = lambda x: x[0])
    newLista = []
    br = 1
    num = len(arr)
    if num > 10:
        num = 10
    for i in arr:
        let = svi_letovi[i[1]]
        x1 = let["broj_leta"]
        x2 = let["sifra_polazisnog_aerodroma"]
        x3 = let["sifra_odredisnog_aerodorma"]
        x4 = let["vreme_poletanja"] + "h"
        x5 = let["vreme_sletanja"] + "h"
        x66 = let["datum_pocetka_operativnosti"]
        x6 = str(str(x66.year) + "/" + str(x66.month) + "/" + str(x66.day))
        x77 = let["datum_kraja_operativnosti"]
        x7 = str(str(x77.year) + "/" + str(x77.month) + "/" + str(x77.day))
        x8 = let["prevoznik"]
        x99 = let["dani"]
        x9 = ""
        for j in range(0, 7):
            if j in x99:
                if j == 0:
                    x9 += "P"
                elif j == 1:
                    x9 += "U"
                elif j == 2:
                    x9 += "S"
                elif j == 3:
                    x9 += "Č"
                elif j == 4:
                    x9 += "P"
                elif j == 5:
                    x9 += "S"
                elif j == 6:
                    x9 += "N"
            else:
                x9 += "_"
 # newLista = [["BR.", "LET", "POLETANJE", "SLETANJE", "DPO", "DKO", "PREVOZNIK", "DANI", "MODEL", " CENA "]]               
        x10 = let["model"]["naziv"]  # BEZ MODELA, NE MOZE STATI U TABELU SVE
        x111 = let["cena"]
        x11 = float("{:.2f}".format(x111))
        newLista.append([num, x1, x4, x5, x6, x7, x8, x9, x10, x11])
        if br == 10:
            break
        br += 1
        num -= 1
    newLista.reverse()    
    
    return newLista    


def kreiraj_poseban_let(broj_leta: str, sifra_polazisnog_aerodroma: str,
                        sifra_odredisnog_aerodorma: str, vreme_poletanja: str, vreme_sletanja: str,
                        sletanje_sutra: bool, prevoznik: str, dani: list, model: dict, cena: float,
                        datum_pocetka_operativnosti: datetime = None,
                        datum_kraja_operativnosti: datetime = None) -> dict:
    letDict = {"broj_leta": broj_leta,
               "sifra_polazisnog_aerodroma": sifra_polazisnog_aerodroma, 
               "sifra_odredisnog_aerodorma": sifra_odredisnog_aerodorma,
               "vreme_poletanja": vreme_poletanja,
               "vreme_sletanja": vreme_sletanja,
               "datum_pocetka_operativnosti": datum_pocetka_operativnosti,
               "datum_kraja_operativnosti": datum_kraja_operativnosti,
               "sletanje_sutra": sletanje_sutra,
               "prevoznik": prevoznik,
               "dani": dani,
               "model": model,
               "cena:": cena}
    
    return letDict


def napravi_random_let() -> dict:
    dani = list({random.randint(0, 6): True for n in range(random.randint(1, 7))}.keys())
    now = datetime.now() 
    today = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    pocetak_operativnosti = today + timedelta(days = randint(0, 500))
    print("\n\n", pocetak_operativnosti)
    #pocetak_operativnosti = rand_datetime()
    kraj_operativnosti = pocetak_operativnosti + timedelta(days = randint(0, 4))
    modeli_aviona = {
            123: {
                "id": 123,
                "naziv": rand_str(10),
                "broj_redova": random.randint(2, 5),
                "pozicije_sedista": rand_seat_positions()
            },
            124: {
                "id": 124,
                "naziv": rand_str(10),
                "broj_redova": random.randint(2, 5),
                "pozicije_sedista": rand_seat_positions()
            }
        }
    let = {
            "broj_leta": rand_str(2) + str(randint(10,99)),
            "sifra_polazisnog_aerodroma": rand_str(3),
            "sifra_odredisnog_aerodorma": rand_str(3),
            "vreme_poletanja": rand_time_str(),
            "vreme_sletanja": rand_time_str(),
            "datum_pocetka_operativnosti": pocetak_operativnosti,
            "datum_kraja_operativnosti": kraj_operativnosti,
            "sletanje_sutra": False,
            "prevoznik": rand_str(10),
            "dani": dani,
            "model": modeli_aviona[123],
            "cena": 100 + random.random() * 200}
    
    return let