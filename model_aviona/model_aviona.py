
import csv


idModela = 0



def podesi_sledeci_id_modela(svi_modeli: dict):
    global idModela
    idModela = len(svi_modeli) + 1
    return

"""
Funkcija kreira novi rečnik za model aviona i dodaje ga u rečnik svih modela aviona.
Kao rezultat vraća rečnik svih modela aviona sa novim modelom.
"""
def kreiranje_modela_aviona(svi_modeli_aviona: dict, naziv: str ="", broj_redova: str = "", 
                            pozicije_sedista: list = []) -> dict:
        # NAZIV
    if naziv == None:
        raise Exception("GRESKA: 'naziv' je prazno. Unesite ponovo.")
    for i in range(0, 3):
        if (ord(naziv[i].lower()) < 97 or ord(naziv[i].lower()) > 122) or len(naziv) != 3:
            raise Exception("GRESKA: 'naziv' nije dobro definisano. Unesite ponovo.")  
     
        # BROJ REDOVA   
    if broj_redova is None:
        raise Exception("GRESKA: 'broj_redova' nije dobro definisano. Unesite ponovo.")  
    if type(broj_redova) is str:    
        for i in broj_redova:
            if ord(i) < 48 or ord(i) > 57:
                raise Exception("GRESKA: 'broj_redova' nije dobro definisano. Unesite ponovo.")  
         
        # POZICIJE SEDISTA
    if pozicije_sedista is None:
        raise Exception("GRESKA: 'pozicije sedista' je prazno. Unesite ponovo.") 
     
    avion = {"id": idModela,
             "naziv": naziv,
             "broj_redova": int(broj_redova),
             "pozicije_sedista": pozicije_sedista}
    newDict = {idModela: avion}
    svi_modeli_aviona.update(newDict)
    
    return svi_modeli_aviona


"""
Funkcija čuva sve modele aviona u fajl na zadatoj putanji sa zadatim operatorom.
"""
def sacuvaj_modele_aviona(putanja: str, separator: str, svi_aerodromi: dict):
    fields = ["id", "naziv", "broj_redova", "pozicije_sedista"]
    with open(putanja, 'a', newline = "") as f:
        w = csv.DictWriter(f, fieldnames = fields, delimiter = separator)
        #w.writeheader()
        for i in svi_aerodromi:
            w.writerow(svi_aerodromi[i])


"""
Funkcija učitava sve modele aviona iz fajla na zadatoj putanji sa zadatim operatorom.
"""
def ucitaj_modele_aviona(putanja: str, separator: str) -> dict:
    myDict = {}
    with open(putanja, 'r') as f:
        r = csv.reader(f, delimiter = separator)
        for i in r:
            newDict = {"id": int(i[0]),
                       "naziv": i[1],
                       "broj_redova": int(i[2]),
                       "pozicije_sedista": eval(i[3])}
            newDict2 = {int(i[0]): newDict}
            myDict.update(newDict2)
      
    return myDict
