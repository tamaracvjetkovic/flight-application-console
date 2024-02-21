
#from common import konstante
#from functools import reduce
from datetime import datetime


import csv


"""
Brojačka promenljiva koja se automatski povećava pri kreiranju nove karte.
"""
sledeci_broj_karte = 1


"""
Kupovina karte proverava da li prosleđeni konkretni let postoji i da li ima slobodnih mesta.
U tom slučaju se karta dodaje u kolekciju svih karata.
Slobodna mesta se prosleđuju posebno iako su deo konkretnog leta, zbog lakšeg testiranja.
Baca grešku ako podaci nisu validni.
kwargs moze da prihvati prodavca kao recnik, i datum_prodaje kao datetime
recnik prodavac moze imati id i ulogu
CHECKPOINT 2: kupuje se samo za ulogovanog korisnika i bez povezanih letova.
ODBRANA: moguće je dodati saputnike i odabrati povezane letove. 
"""
def kupovina_karte(sve_karte: dict, svi_konkretni_letovi: dict, sifra_konkretnog_leta: int, 
                   putnici: list, slobodna_mesta: list, kupac: dict, **kwargs) -> tuple[dict, dict]:
        # SIFRA KONKRETNOG LETA
    if sifra_konkretnog_leta is None:
        raise Exception("GRESKA: 'šifra konkretnog leta' je prazno. Unesite ponovo.")
    if sifra_konkretnog_leta not in svi_konkretni_letovi:
        raise Exception("GRESKA: 'šifra konkretnog leta' ne postoji. Unesite ponovo.")
    
        # SLOBODNA MJESTA
    brojSlobodnih = 0
    brojRedova = len(slobodna_mesta)
    for i in range(0, brojRedova):
        for j in slobodna_mesta[i]:
            if j == False:
                brojSlobodnih += 1
    brojOsoba = 1
    if brojSlobodnih < brojOsoba:
        raise Exception("GRESKA: nema dovoljno slobodnih mesta!")
        
        # PUTNICI
    if putnici is None:
        raise Exception("GRESKA: 'putnici' ne sme biti prazno. Unesite ponovo.")
    if len(putnici) == 0:
        raise Exception("GRESKA: 'putnici' ne sme biti prazno. Unesite ponovo.")
    
        # KUPAC
    if len(kupac) == 0 or kupac == None:
        raise Exception("GRESKA: 'kupac' ne sme biti prazno. Unesite ponovo.")
    if kupac["uloga"] != "korisnik":
        raise Exception("GRESKA: 'uloga kupca' nije dobro definisano. Unesite ponovo.")  
                       
    global sledeci_broj_karte
    podesi_sledeci_broj_karte(sve_karte)
    
    karta = {"broj_karte": sledeci_broj_karte,
             "sifra_konkretnog_leta": sifra_konkretnog_leta,
             "kupac": kupac,
             "prodavac": kwargs["prodavac"],
             "datum_prodaje": kwargs["datum_prodaje"],
             "status": "nerealizovana_karta",
             "obrisana": False,
             "putnici": putnici}   
    newDict = {sledeci_broj_karte: karta}
    sve_karte.update(newDict) 
    sledeci_broj_karte += 1
   
    return (karta, sve_karte)


def podesi_sledeci_broj_karte(sve_karte: dict):
    global sledeci_broj_karte
    sledeci_broj_karte = len(sve_karte) + 1
    return


def pregled_nerealizovanaih_karata(korisnik: dict, sve_karte: iter):
    karte = []
    if korisnik == None or len(korisnik) == 0:
        raise Exception("GRESKA: 'korisnik' ne sme biti prazno. Unesite ponovo.")   
    sveKarte = ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    if sveKarte == sve_karte:
        num = 1
        for karta in sve_karte:
            for putnik in sve_karte[karta]["putnici"]:
                for key in putnik:
                    break
                #print(putnik[key])
                #print(korisnik, "\n\n")
                if putnik[key] == korisnik:
                    if sve_karte[karta]["status"] == "nerealizovana_karta":
                        x1 = sve_karte[karta]["broj_karte"]
                        x2 = sve_karte[karta]["sifra_konkretnog_leta"]
                        x33 = sve_karte[karta]["datum_prodaje"]
                        x3 = str(x33.year) + "/" + str(x33.month) + "/" + str(x33.day)
                        x4 = "NEREALIZOVANA"
                        karte.append([num, x1, x2, x3, x4])
                        num += 1
        return karte 
    else:
        for karta in sve_karte:
            for putnik in karta["putnici"]:
                if putnik == korisnik:
                    if karta["status"] == "nerealizovana_karta":
                        karte.append(karta)             
        return karte


"""
Funkcija menja sve vrednosti karte novim vrednostima. Kao rezultat vraća rečnik sa svim kartama, 
koji sada sadrži izmenu.
"""
def izmena_karte(sve_karte: iter, svi_konkretni_letovi: iter, broj_karte: int,
                 nova_sifra_konkretnog_leta: int = None, nov_datum_polaska: datetime = None,
                 sediste = None) -> dict:
    if broj_karte not in sve_karte or broj_karte is None:
        raise Exception("GRESKA: 'broj_karte' nije dobro definisano. Unesite ponovo.")
    
    sve_karte[broj_karte]["sifra_leta"] = nova_sifra_konkretnog_leta
    sve_karte[broj_karte]["sifra_konkretnog_leta"] = nova_sifra_konkretnog_leta
    sve_karte[broj_karte]["sediste"] = sediste
    sve_karte[broj_karte]["datum_prodaje"] = nov_datum_polaska
    sve_karte[broj_karte]["obrisana"] = False
    
    return sve_karte


"""
 Funkcija brisanja karte se ponaša drugačije u zavisnosti od korisnika:
- Prodavac: karta se označava za brisanje
- Admin/menadžer: karta se trajno briše
Kao rezultat se vraća nova kolekcija svih karata.
"""
def brisanje_karte(korisnik: dict, sve_karte: dict, broj_karte: int) -> dict:
    if korisnik == None:
        raise Exception("GRESKA: 'korisnik' nije dobro definisano. Unesite ponovo.")
    if broj_karte not in sve_karte:
        raise Exception("GRESKA: 'broj_karte' nije dobro definisano. Unesite ponovo.")  
    if broj_karte == None: 
        raise Exception("GRESKA: 'broj_karte' nije dobro definisano. Unesite ponovo.")  
    if korisnik["uloga"] == "prodavac" or korisnik["uloga"] == "admin":
        if korisnik["uloga"] == "prodavac":
            sve_karte[broj_karte]["obrisana"] = True
        else:
            sve_karte.pop(broj_karte, None) 
    else:
        raise Exception("GRESKA: 'korisnik' nije dobro definisano. Unesite ponovo.")    
    
               
    return sve_karte


"""
Funkcija vraća sve karte koje se poklapaju sa svim zadatim kriterijumima. 
Kriterijum se ne primenjuje ako nije prosleđen.
"""
def pretraga_prodatih_karata(sve_karte: dict, svi_letovi: dict, svi_konkretni_letovi: dict,
                             polaziste: str = "", odrediste: str = "", datum_polaska: datetime = "",
                             datum_dolaska: str = "", korisnicko_ime_putnika: str = "") -> list:
    dobreKarte = {}
    for let in svi_letovi:
        brojLeta = svi_letovi[i]["broj_leta"]
        if svi_letovi[i]["sifra_polazisnog_aerodroma"] == polaziste:
            dobreKarte[brojLeta] = 1
        if svi_letovi[i]["sifra_dolazisnog_aerodroma"] == odrediste:
            dobreKarte[brojLeta] = 1
        if svi_letovi[i]["datum_pocetka_operativnosti"] == datum_polaska:
            dobreKarte[brojLeta] = 1
        if svi_letovi[i]["datum_kraja_operativnosti"] == datum_dolaska:
            dobreKarte[brojLeta] = 1
    for karta in sve_karte:
        for i in sve_karte[karta]["putnici"]:
            if i["korisnicko_ime"] == korisnicko_ime_putnika:
                brojLeta2 = svi_konkretni_letovi[sve_karte[karta]["sifra_konkretnog_leta"]]["broj_leta"]     
                dobreKarte[brojLeta2] = 1
    listaSifri = {}
    for let in svi_konkretni_letovi:
        if dobreKarte[svi_konkretni_letovi[let]["broj_leta"]] == 1:
            listaSifri[svi_konkretni_letovi[let]["sifra"]] = 1               
    newList = []
    for karta in sve_karte:
        if listaSifri[sve_karte[karta]["sifra_konkretnog_leta"]] == 1:
            newList.append(sve_karte[karta])
    
    return newList


"""
Funkcija čuva sve karte u fajl na zadatoj putanji sa zadatim separatorom.
"""
def sacuvaj_karte(sve_karte: dict, putanja: str, separator: str):
    if putanja == "sve_karte.txt":
        fields = ["broj_karte", "sifra_konkretnog_leta", "kupac", "prodavac",
                  "datum_prodaje", "status", "obrisana", "putnici", "sediste"]
    else:
        fields = ["broj_karte", "sifra_konkretnog_leta", "kupac", "prodavac",
                  "datum_prodaje", "obrisana", "putnici", "sediste"]
    with open(putanja, 'a', newline = "") as f:
        w = csv.DictWriter(f, fieldnames = fields, delimiter = separator)
        #w.writeheader()
        for i in sve_karte:
            w.writerow(sve_karte[i])
# FALI STATUS U TESTOVIMA

"""
Funkcija učitava sve karte iz fajla sa zadate putanje sa zadatim separatorom.
"""
def ucitaj_karte_iz_fajla(putanja: str, separator: str) -> dict:
    myDict = {}
    with open(putanja, 'r') as f:
        r = csv.reader(f, delimiter = separator) 
        for i in r:
            brojKarte = int(i[0])
            deleted = True
            if putanja == "sve_karte.txt":
                datum = datetime.strptime(i[4], "%Y-%m-%d %H:%M:%S")
                if i[6] == 'False':
                    deleted = False
                if i[3] == "" or i[3] is None:
                    newDict = {"broj_karte": brojKarte,
                               "sifra_konkretnog_leta": int(i[1]),
                               "kupac": eval(i[2]),
                               "prodavac": i[3],
                               "datum_prodaje": datum,
                               "status": i[5],
                               "obrisana": deleted,
                               "putnici": eval(i[7]),
                               "sediste": i[8]}
                else:    
                    newDict = {"broj_karte": brojKarte,
                               "sifra_konkretnog_leta": int(i[1]),
                               "kupac": eval(i[2]),
                               "prodavac": eval(i[3]),
                               "datum_prodaje": datum,
                               "status": i[5],
                               "obrisana": deleted,
                               "putnici": eval(i[7]),
                               "sediste": i[8]}
            else:
                if i[5] == 'False':
                    deleted = False       
                newDict = {"broj_karte": brojKarte,
                           "sifra_konkretnog_leta": int(i[1]),
                           "kupac": eval(i[2]),
                           "prodavac": eval(i[3]),
                           "datum_prodaje": i[4],
                           "obrisana": deleted,
                           "putnici": eval(i[6]),
                           "sediste": i[7]}
            newDict2 = {brojKarte: newDict}
            myDict.update(newDict2)
    
    return myDict


def pretraga_prodatih_karata(sve_karte: dict, svi_konkretni_letovi: dict, svi_letovi: dict,
                             polaziste: str = "", odrediste: str = "",
                             datum_polaska: str = "", datum_dolaska: str = "",
                             ime_putnika: str = "", prezime_putnika: str = "") -> tuple[list, list]:
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
    
    if ime_putnika is not None and ime_putnika != "":
        s = "imenu putnika: '" + str(ime_putnika) + "'"
        listaParametara.append(s)
        for i in ime_putnika:
            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                raise Exception("GREŠKA: 'ime putnika' nije dobro definisano. Unesite ponovo.")    
        
    if prezime_putnika is not None and prezime_putnika != "":
        s = "prezimenu putnika: '" + str(prezime_putnika) + "'"
        listaParametara.append(s)    
        for i in prezime_putnika:
            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                raise Exception("GREŠKA: 'ime putnika' nije dobro definisano. Unesite ponovo.")


    polazisteOk = 1
    if polaziste is not None and polaziste != "":    
        polazisteOk = 0
        
    odredisteOk = 1     
    if odrediste is not None and odrediste != "":    
        odredisteOk = 0
       
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
            
    imePutnikaOk = 1     
    if ime_putnika is not None and ime_putnika != "":    
        imePutnikaOk = 0
        
    prezimePutnikaOk = 1     
    if prezime_putnika is not None and prezime_putnika != "":    
        prezimePutnikaOk = 0    
                
    for karta in sve_karte:
        sifraKonkretnog = sve_karte[karta]["sifra_konkretnog_leta"]
        brojLeta = svi_konkretni_letovi[sifraKonkretnog]["broj_leta"]
        if polazisteOk == 0 and polaziste == svi_letovi[brojLeta]["sifra_polazisnog_aerodroma"]:
            polazisteOk = 1
        if odredisteOk == 0 and odrediste == svi_letovi[brojLeta]["sifra_odredisnog_aerodorma"]:
            odredisteOk = 1   
        datumPolaska1 = svi_konkretni_letovi[sifraKonkretnog]['datum_i_vreme_polaska']
        datumPolaska = datetime(datumPolaska1.year, datumPolaska1.month, datumPolaska1.day)  
        datumDolaska1 = svi_konkretni_letovi[sifraKonkretnog]['datum_i_vreme_dolaska']
        datumDolaska = datetime(datumDolaska1.year, datumDolaska1.month, datumDolaska1.day)
        if datumPolaskaOk == 0 and datum_polaska1 == datumPolaska:
            datumPolaskaOk = 1
        if datumDolaskaOk == 0 and datum_dolaska1 == datumDolaska:
            datumDolaskaOk = 1       
        for i in sve_karte[karta]["putnici"]:
            if len(i) == 1:
                for key in i:
                    korisnickoIme = key
                    break
                if imePutnikaOk == 0 and ime_putnika == i[korisnickoIme]["ime"]:
                    imePutnikaOk = 1
                if prezimePutnikaOk == 0 and prezime_putnika == i[korisnickoIme]["prezime"]:
                    prezimePutnikaOk = 1
            else:
                if imePutnikaOk == 0 and ime_putnika == i["ime"]:
                    imePutnikaOk = 1
                if prezimePutnikaOk == 0 and prezime_putnika == i["prezime"]:
                    prezimePutnikaOk = 1    

    if polazisteOk == 0:
        raise Exception("GREŠKA: 'šifra polazišnog aerodroma' ne postoji u svim kartama. Unesite ponovo.") 
    if odredisteOk == 0:
        raise Exception("GREŠKA: uneseno 'šifra odredišnog aerodroma' ne postoji u svim kartama. Unesite ponovo.") 
    if datumPolaskaOk == 0:
        raise Exception("GREŠKA: unesen 'datum polaska' ne postoji u svim kartama. Unesite ponovo.")
    if datumDolaskaOk == 0:
        raise Exception("GREŠKA: unesen 'datum polaska' ne postoji u svim kartama. Unesite ponovo.")
    if imePutnikaOk == 0:
        raise Exception("GREŠKA: unesen 'ime putnika' ne postoji u svim kartama. Unesite ponovo.")
    if prezimePutnikaOk == 0:
        raise Exception("GREŠKA: unesen 'prezime putnika' ne postoji u svim kartama. Unesite ponovo.")

    brojOkKarata = {-1}
    listaKarata = []      
    for karta in sve_karte:
        ok = 0
        sifraKonkretnog = sve_karte[karta]['sifra_konkretnog_leta']
        brojLeta = svi_konkretni_letovi[sifraKonkretnog]["broj_leta"]
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
            datumPolaska1 = svi_konkretni_letovi[sifraKonkretnog]['datum_i_vreme_polaska']
            datumPolaska = datetime(datumPolaska1.year, datumPolaska1.month, datumPolaska1.day) 
            if datum_polaska1 != 0 and datumPolaska == datum_polaska1:
                ok = 1 
            else:
                continue
        if datum_dolaska != "" and datum_dolaska is not None:        
            datumDolaska1 = svi_konkretni_letovi[sifraKonkretnog]['datum_i_vreme_dolaska']
            datumDolaska = datetime(datumDolaska1.year, datumDolaska1.month, datumDolaska1.day) 
            if datum_dolaska1 != 0 and datumDolaska == datum_dolaska1:
                ok = 1
            else:
                continue
        if ime_putnika != "" and ime_putnika is not None:   
            for i in sve_karte[karta]["putnici"]:
                if len(i) == 1:
                    for key in i:
                        korisnickoIme = key
                        break       
                    if i[korisnickoIme]["ime"] == ime_putnika:
                        ok = 1
                    else:
                        continue
                else:
                    if i["ime"] == ime_putnika:
                        ok = 1 
                    else:
                        continue     
        if prezime_putnika != "" and prezime_putnika is not None:   
            for i in sve_karte[karta]["putnici"]:
                if len(i) == 1:
                    for key in i:
                        korisnickoIme = key
                        break       
                    if i[korisnickoIme]["prezime"] == prezime_putnika:
                        ok = 1
                    else:
                        continue
                else:
                    if i["prezime"] == prezime_putnika:
                        ok = 1 
                    else:
                        continue                     
        if ok == 1:
            brojOkKarata.add(karta)   
    brojOkKarata.remove(-1)  
    brojOkKarata = sorted(brojOkKarata)   
    num = 1     
    for i in brojOkKarata:
        datum = sve_karte[i]['datum_prodaje']
        date1 = str(datum.year) + "/" + str(datum.month) + "/" + str(datum.day)
        if sve_karte[i]['status'] == "nerealizovana_karta":
            status = "NEREALIZOVANA"
        else:
            status = "REALIZOVANA"
        kupac = sve_karte[i]["kupac"]["ime"] + " " + sve_karte[i]["kupac"]["prezime"]
        novaLista = [num, sve_karte[i]['broj_karte'], sve_karte[i]['sifra_konkretnog_leta'],
                     date1, status, kupac]
        listaKarata.append(novaLista)   
        num += 1
    
    return (listaKarata, listaParametara)
    
    