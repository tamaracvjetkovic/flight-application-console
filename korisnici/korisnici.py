
import common.konstante
from common import konstante
from termcolor import colored

import csv

id_neregistrovanog = 1

"""
Funkcija koja kreira novi rečnik koji predstavlja korisnika sa prosleđenim vrednostima. Kao rezultat vraća kolekciju
svih korisnika proširenu novim korisnikom. Može se ponašati kao dodavanje ili ažuriranje, u zavisnosti od vrednosti
parametra azuriraj:
- azuriraj == False: kreira se novi korisnik. staro_korisnicko_ime ne mora biti prosleđeno.
Vraća grešku ako korisničko ime već postoji.
- azuriraj == True: ažurira se postojeći korisnik. Staro korisnicko ime mora biti prosleđeno. 
Vraća grešku ako korisničko ime ne postoji.

Ova funkcija proverava i validnost podataka o korisniku, koji su tipa string.

CHECKPOINT 1: Vraća string sa greškom ako podaci nisu validni.
    Hint: Postoji string funkcija koja proverava da li je string broj bez bacanja grešaka. Probajte da je pronađete.
ODBRANA: Baca grešku sa porukom ako podaci nisu validni.
"""
def kreiraj_korisnika(svi_korisnici: dict, azuriraj: bool, uloga: str, staro_korisnicko_ime: str, 
                      korisnicko_ime: str, lozinka: str, ime: str, prezime: str, email: str = "",
                      pasos: str = "", drzavljanstvo: str = "",
                      telefon: str = "", pol: str = "") -> dict:
     # -------- (AZURIRAJ = FALSE) --------     
    if not azuriraj or azuriraj is False or azuriraj == 0:
        
            # KORISNICKO IME
        if korisnicko_ime is None or korisnicko_ime == "":
            raise Exception("GRESKA: 'korisnicko ime' ne sme biti prazno. Unesite ponovo.")  
        if korisnicko_ime in svi_korisnici:
            raise Exception("GRESKA: 'korisnicko ime' je vec u upotrebi. Unesite ponovo.") 
        
            # ULOGE
        sveUloge = [konstante.ULOGA_KORISNIK, konstante.ULOGA_PRODAVAC, konstante.ULOGA_ADMIN]  
        if uloga is None:
            raise Exception("GRESKA: 'uloga' ne sme biti prazno. Unesite ponovo.")
        if uloga not in sveUloge:
            raise Exception("GRESKA: 'uloga' ne postoji. Unesite ponovo.")
        
            # LOZINKA
        if lozinka is None or lozinka == "":
            raise Exception("GRESKA: 'lozinka' ne sme biti prazno. Unesite ponovo.")
        
            # IME
        if ime is None or ime == "":
            raise Exception("GRESKA: 'ime' ne sme biti prazno. Unesite ponovo.")
        for i in range(0, len(ime)):
            s = ime[i].lower()
            if ord(s) < 97 or ord(s) > 122:
                raise Exception("GRESKA: 'ime' nije dobro definisano. Unesite ponovo.")
            
            # PREZIME
        if prezime is None or prezime == "":
            raise Exception("GRESKA: 'prezime' ne sme biti prazno. Unesite ponovo.")
        for i in range(0, len(prezime)):
            s = prezime[i].lower()
            if ord(s) < 97 or ord(s) > 122:
                raise Exception("GRESKA: 'prezime' nije dobro definisano. Unesite ponovo.")
            
            # EMAIL
        if email is None or email == "":
            raise Exception("GRESKA: 'email' ne sme biti prazno. Unesite ponovo.")
        monkey1 = 0
        checkBeforeMonkey = ""
        checkEmail = ""
        for i in email:   # tamara.cvjetkovic@gmail.com
            if monkey1:
                checkEmail += i
            if i == '@':
                if checkBeforeMonkey == '':
                    raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.")
                monkey1 += 1 
            checkBeforeMonkey += i    
        if monkey1 == 0 or monkey1 > 1:
            raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.") 
        numOfDots = 0
        dot1 = 0
        checkAfterDot = ""
        checkAfterMonkey = ""
        for i in checkEmail:
            if dot1:
                checkAfterDot += i
            if i == ".":
                if checkAfterMonkey == '':
                    raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.")
                dot1 = 1
                numOfDots += 1
            checkAfterMonkey += i
        if numOfDots != 1:
            raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.")
        if checkAfterDot == '':
            raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.")     
    
        if pasos is not None and pasos != "" and len(str(pasos)) != 0:
            lenPasos = 0  
            for i in pasos:
                cur = ord(i)
                if cur >= 48 and cur <= 57:
                    lenPasos += 1
                else:
                    raise Exception("GRESKA: 'pasos' nije dobro definisano. Unesite ponovo.") 
            if lenPasos != 9:
                raise Exception("GRESKA: 'pasos' nije dobro definisano. Unesite ponovo.")  
        
            # TELEFON   
        if telefon is None or telefon == "":
            raise Exception("GRESKA: 'telefon' ne sme biti prazno. Unesite ponovo.")               
        for i in telefon:
            cur = ord(i)
            if cur >= 48 and cur <= 57:
                continue
            else:
                raise Exception("GRESKA: 'telefon' nije dobro definisano. Unesite ponovo.") 
            
        for korisnik in svi_korisnici:
            if svi_korisnici[korisnik]["email"] == email and email != "" and email != None:
                raise Exception("GRESKA: 'email' je vec u upotrebi. Unesite ponovo.")
            if svi_korisnici[korisnik]["pasos"] == pasos and pasos != "" and pasos != None:
                raise Exception("GRESKA: 'pasos' je vec u upotrebi. Unesite ponovo.")
            if svi_korisnici[korisnik]["telefon"] == telefon and telefon != "" and telefon != None:
                raise Exception("GRESKA: 'telefon' je vec u upotrebi. Unesite ponovo.")    
             
        newDict = {korisnicko_ime: {"uloga": uloga, "korisnicko_ime": korisnicko_ime, "lozinka": lozinka, "ime": ime,
                   "prezime": prezime, "email": email, "pasos": pasos, "drzavljanstvo": drzavljanstvo,
                   "telefon": telefon, "pol": pol}}
        svi_korisnici.update(newDict);   
        
         # -------- (AZURIRAJ = TRUE) --------  
    else:
        
        for korisnik in svi_korisnici:
            if svi_korisnici[korisnik]["email"] == email and email != svi_korisnici[staro_korisnicko_ime]["email"] and email != "" and email != None:
                raise Exception("GRESKA: 'email' je vec u upotrebi. Unesite ponovo.")
            if svi_korisnici[korisnik]["pasos"] == pasos and pasos != svi_korisnici[staro_korisnicko_ime]["pasos"] and pasos != "" and pasos != None:
                raise Exception("GRESKA: 'pasos' je vec u upotrebi. Unesite ponovo.")
            if svi_korisnici[korisnik]["telefon"] == telefon and telefon != svi_korisnici[staro_korisnicko_ime]["telefon"] and telefon != "" and telefon != None:
                raise Exception("GRESKA: 'telefon' je vec u upotrebi. Unesite ponovo.") 
            # KORISNICKO IME
        if staro_korisnicko_ime is None or staro_korisnicko_ime == "":
            raise Exception("GRESKA: 'staro korisnicko ime' ne sme biti prazno. Unesite ponovo.")
        if staro_korisnicko_ime not in svi_korisnici:
            raise Exception("GRESKA: 'staro korisnicko ime' ne postoji. Unesite ponovo.") 
        
            # ULOGE
        sveUloge = ["korisnik", "prodavac", "admin"] 
        if uloga is None:
            raise Exception("GRESKA: 'uloga' ne sme biti prazno. Unesite ponovo.")
        if uloga not in sveUloge:
            raise Exception("GRESKA: 'uloga' nije dobro definisano. Unesite ponovo.")
        
            # STARO KORISNICKO IME
        if korisnicko_ime is None or korisnicko_ime == "":
            raise Exception("GRESKA: 'korisnicko ime' nije dobro definisano. Unesite ponovo.")
        if korisnicko_ime in svi_korisnici and korisnicko_ime != staro_korisnicko_ime:
            raise Exception("Greska") 
            
            # LOZINKA
        if lozinka is None or lozinka == "":
            raise Exception("GRESKA: 'lozinka' ne sme biti prazno. Unesite ponovo.")
        
            # IME
        if ime is None or ime == "":
            raise Exception("GRESKA: 'ime' ne sme biti prazno. Unesite ponovo.")
        for i in range(0, len(ime)):
            s = ime[i].lower()
            if ord(s) < 97 or ord(s) > 122:
                raise Exception("GRESKA: 'ime' nije dobro definisano. Unesite ponovo.")
            
            # PREZIME
        if prezime is None or prezime == "":
            raise Exception("GRESKA: 'prezime' ne sme biti prazno. Unesite ponovo.")
        for i in range(0, len(prezime)):
            s = prezime[i].lower()
            if ord(s) < 97 or ord(s) > 122:
                raise Exception("GRESKA: 'prezime' nije dobro definisano. Unesite ponovo.")
            
            # EMAIL
        if email is None or email == "":
            raise Exception("GRESKA: 'email' ne sme biti prazno. Unesite ponovo.")
        monkey1 = 0
        checkBeforeMonkey = ""
        checkEmail = ""
        for i in email:   # tamara.cvjetkovic@gmail.com
            if monkey1:
                checkEmail += i
            if i == '@':
                if checkBeforeMonkey == '':
                    raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.")
                monkey1 += 1 
            checkBeforeMonkey += i    
        if monkey1 != 1:
           raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.") 
        numOfDots = 0
        dot1 = 0
        checkAfterDot = ""
        checkAfterMonkey = ""
        for i in checkEmail:
            if dot1:
                checkAfterDot += i
            if i == ".":
                if checkAfterMonkey == '':
                    raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.")
                dot1 = 1
                numOfDots += 1
            checkAfterMonkey += i
        if numOfDots != 1:
            raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.") 
        if checkAfterDot == '':
            raise Exception("GRESKA: 'email' nije dobro definisano. Unesite ponovo.") 
              
        if pasos is not None and pasos != "":
            lenPasos = 0  
            for i in pasos:
                cur = ord(i)
                if cur >= 48 and cur <= 57:
                    lenPasos += 1
                else:
                    raise Exception("GRESKA: 'pasos' nije dobro definisano. Unesite ponovo.") 
            if lenPasos != 9:
                raise Exception("GRESKA: 'pasos' nije dobro definisano. Unesite ponovo.")  
        
            # TELEFON   
        if telefon is None or telefon == "":
            raise Exception("GRESKA: 'telefon' ne sme biti prazno. Unesite ponovo.")               
        for i in telefon:
            cur = ord(i)
            if cur >= 48 and cur <= 57:
                continue
            else:
                raise Exception("GRESKA: 'telefon' nije dobro definisano. Unesite ponovo.") 
              
        myList = {"uloga": uloga, "korisnicko_ime": korisnicko_ime, "lozinka": lozinka, "ime": ime,
                   "prezime": prezime, "email": email, "pasos": pasos, "drzavljanstvo": drzavljanstvo,
                   "telefon": telefon, "pol": pol}
        if korisnicko_ime == staro_korisnicko_ime:
            svi_korisnici[korisnicko_ime] = myList
        else:
            newDict = {korisnicko_ime: myList}
            svi_korisnici.update(newDict);
            del svi_korisnici[staro_korisnicko_ime]
            
        # -------- VRATI (dict) --------       
    return svi_korisnici


"""
Funkcija koja čuva podatke o svim korisnicima u fajl na zadatoj putanji sa zadatim separatorom.
"""
def sacuvaj_korisnike(putanja: str, separator: str, svi_korisnici: dict):
    fields = ["uloga", "korisnicko_ime", "lozinka", "ime", "prezime", "email", "pasos", "drzavljanstvo", "telefon", "pol"]
    with open(putanja, 'a', newline = "") as f:
        w = csv.DictWriter(f, fieldnames = fields, delimiter = separator)
        #w.writeheader()
        for i in svi_korisnici:
            w.writerow(svi_korisnici[i])
    
    return


"""
Funkcija koja učitava sve korisnika iz fajla na putanji sa zadatim separatorom. Kao rezultat vraća učitane korisnike.
"""
def ucitaj_korisnike_iz_fajla(putanja: str, separator: str) -> dict:
    myDict = {}
    with open(putanja, 'r') as f:
        r = csv.reader(f, delimiter = separator)
        for i in r:
            #print(i)
            newDict = {"uloga": i[0], "korisnicko_ime": i[1], "lozinka": i[2], "ime": i[3],
                       "prezime": i[4], "email": i[5], "pasos": i[6], "drzavljanstvo": i[7],
                       "telefon": i[8], "pol": i[9]}
            newDict2 = {i[1]: newDict}
            myDict.update(newDict2)
      
    return myDict


def kreiraj_neregistrovanog(svi_neregistrovani: dict, ime: str, prezime: str) -> dict:
    global id_neregistrovanog
    podesi_id_neregistrovanog(svi_neregistrovani)
    noviNeregistrovani = {id: {"uloga": "neregistrovan",
                               "id": id_neregistrovanog,
                               "ime": ime,
                               "prezime": prezime,
                               "email": "",
                               "pasos": "",
                               "drzavljanstvo": "",
                               "telefon": "",
                               "pol": ""}}
    return noviNeregistrovani
    
    
def podesi_id_neregistrovanog(svi_neregistrovani_korisnici: dict):
    global id_neregistrovanog
    id_neregistrovanog = len(svi_neregistrovani_korisnici) + 1
    return


def sacuvaj_neregistrovane_korisnike(putanja: str, separator: str, svi_neregistrovani: dict):
    fields = ["uloga", "id", "ime", "prezime", "email", "pasos", "drzavljanstvo", "telefon", "pol"]
    with open(putanja, 'a', newline = "") as f:
        w = csv.DictWriter(f, fieldnames = fields, delimiter = separator)
        #w.writeheader()
        for i in svi_neregistrovani:
            w.writerow(svi_neregistrovani[i])
    
    return


def ucitaj_neregistrovane_korisnike_iz_fajla(putanja: str, separator: str) -> dict:
    myDict = {}
    with open(putanja, 'r') as f:
        r = csv.reader(f, delimiter = separator)
        for i in r:
            newDict = {"uloga":  i[0],
                       "id": int(i[1]),
                       "ime": i[2],
                       "prezime": i[3],
                       "email": i[4],
                       "pasos": i[5],
                       "drzavljanstvo": i[6],
                       "telefon": i[7],
                       "pol": i[8]}
            newDict2 = {i[1]: newDict}
            myDict.update(newDict2)
      
    return myDict

            


"""
Funkcija koja vraća korisnika sa zadatim korisničkim imenom i šifrom.
CHECKPOINT 1: Vraća string sa greškom ako korisnik nije pronađen.
ODBRANA: Baca grešku sa porukom ako korisnik nije pronađen.
"""
def login(svi_korisnici, korisnicko_ime, lozinka) -> dict:
    if korisnicko_ime is None:
        raise Exception("GRESKA: 'korisnicko ime' je prazno. Unesite ponovo.")
    if korisnicko_ime not in svi_korisnici:
        raise Exception("GRESKA: 'korisnicko ime' ne postoji. Unesite ponovo.") 
    if lozinka is None:
        raise Exception("GRESKA: 'lozinka' je prazno. Unesite ponovo.")   
    if svi_korisnici[korisnicko_ime]["lozinka"] != lozinka:
        raise Exception("GRESKA: 'lozinka' nije odgovarajuce. Unesite ponovo.")
    
    return svi_korisnici[korisnicko_ime]


"""
Funkcija koja vrsi log out
*
"""
def logout(korisnicko_ime: str):
    print("\n\n")
    print(colored("ODJAVA USPESNA!\n", "green", attrs = ["bold", "underline"]))
    print(colored("Dovidjenja, '", "green"), end = "")
    print(colored(korisnicko_ime, "light_green"), end = "")
    print(colored("'!\n\n", "green"))
    print("─────────────────────────────────────────────────────────────────────────────\n\n")      
    return

