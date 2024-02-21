
import csv


"""
Funkcija kreira rečnik za novi aerodrom i dodaje ga u rečnik svih aerodroma.
Kao rezultat vraća rečnik svih aerodroma sa novim aerodromom.
"""
def kreiranje_aerodroma(svi_aerodromi: dict, skracenica: str = "", pun_naziv: str = "", 
                        grad: str = "", drzava: str = "") -> dict:
        # SKRACENICA
    if skracenica is None or skracenica == "":
        raise Exception("GRESKA: 'skracenica' nije definisano. Unesite ponovo.")
    for i in skracenica:
        if ord(i.lower()) < 97 or ord(i.lower()) > 122 or len(skracenica) != 3: 
            raise Exception("GRESKA: 'skracenica' nije definisano. Unesite ponovo.")

        # PUN NAZIV
    if pun_naziv is None or pun_naziv == "":
        raise Exception("GRESKA: 'pun_naziv' nije dobro definisano. Unesite ponovo.")
    for i in pun_naziv:
        if ord(i.lower()) < 97 or ord(i.lower()) > 122: 
            raise Exception("GRESKA: 'pun_naziv' nije dobro definisano. Unesite ponovo.")
    
        # GRAD
    if grad is None or grad == "":
        raise Exception("GRESKA: 'grad' nije dobro definisano. Unesite ponovo.")
    for i in grad:
        if ord(i.lower()) < 97 or ord(i.lower()) > 122: 
            raise Exception("GRESKA: 'grad' nije dobro definisano. Unesite ponovo.")
    
        # DRZAVA 
    if drzava is None or drzava == "":
        raise Exception("GRESKA: 'drzava' nije dobro definisano. Unesite ponovo.")
    for i in drzava:
        if ord(i.lower()) < 97 or ord(i.lower()) > 122: 
            raise Exception("GRESKA: 'drzava' nije dobro definisano. Unesite ponovo.")
    
    aerodrom = {"skracenica": skracenica,
                "pun_naziv": pun_naziv,
                "grad": grad,
                "drzava": drzava}
    newDict = {"skracenica": aerodrom}
    svi_aerodromi.update(newDict)
    
    return svi_aerodromi


"""
Funkcija koja čuva aerodrome u fajl.
"""
def sacuvaj_aerodrome(putanja: str, separator: str, svi_aerodromi: dict):
    fields = ["skracenica", "pun_naziv", "grad", "drzava"]
    with open(putanja, 'w', newline = "") as f:
        w = csv.DictWriter(f, fieldnames = fields, delimiter = separator)
        #w.writeheader()
        for i in svi_aerodromi:
            w.writerow(svi_aerodromi[i])
            

"""
Funkcija koja učitava aerodrome iz fajla.
"""
def ucitaj_aerodrom(putanja: str, separator: str) -> dict:
    myDict = {}
    with open(putanja, 'r') as f:
        r = csv.reader(f, delimiter = separator)
        for i in r:
            newDict = {"skracenica": i[0],
                       "pun_naziv":i[1],
                       "grad": i[2],
                       "drzava": i[3]}
            newDict2 = {i[0]: newDict}
            myDict.update(newDict2)
      
    return myDict
