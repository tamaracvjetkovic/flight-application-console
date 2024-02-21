
import os 
#import stdiomask


from aerodromi import aerodromi
from izvestaji import izvestaji
from karte import karte
from konkretni_letovi import konkretni_letovi
from korisnici import korisnici
from korisnici import *
from letovi import letovi
from model_aviona import model_aviona
from test import test_aerodromi, test_izvestaji, test_karte, test_konkretni_letovi, test_korisnici, test_letovi, test_model_aviona, test_utils


from datetime import date, datetime, timedelta
from termcolor import colored
from tabulate import tabulate


povezani = 0
global trenutni_ulogovan_korisnik

      
###################################################################################################


# EXIT SKROZ
def izlazak_iz_aplikacije():
    print("\n\n─────────────────────────────────────────────────────────────────────────────────────\n")
    print_time()
    print(colored("Hvala Vam što ste koristili našu aplikaciju.\n", "red"))
    print("\nAko imate bilo kakvih pitanja ili primedbi u vezi aplikacije, možete nas kontaktirati:")
    print("- službeni mail: tacaairlines@gmail.com")
    print("- broj telefona: +381 65 114 6648, +381 65 116 2248\n\n")
    print(colored("┌────────────┐", "red", attrs = ["bold", "dark"]))
    print(colored("│ ", "red", attrs = ["dark"]), end = "")
    print(colored("Doviđenja!", "red", attrs = ["bold", "dark"]), end = "")
    print(colored(" │", "red", attrs = ["dark"]))
    print(colored("└────────────┘", "red", attrs = ["bold", "dark"]))
    print("\n\n─────────────────────────────────────────────────────────────────────────────────────\n\n")
    quit()

# PRINT TIME
def print_time():
    dateNow = datetime.now()
    d1 = dateNow.strftime("%d/%m/%Y, %H:%M:%S")
    d2 = colored(str(d1), "light_green")
    print("\n", d2, "\n")
    return

# OCISTI SKROZ FILE NA ZADATOJ PUTANJI
def ocisti_file(putanja):
    f = open(putanja, "w")
    f.close()
    return


####################################################################################################

                                    # RANDOM TESTOVI


def dodaj_random_kartu():                                       
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|") # dict
    karta = karte.napravi_random_kartu()
    puna_karta = {karta["broj_karte"]: karta}
    sveKarte.update(puna_karta)
    ocisti_file("sve_karte.txt")
    karte.sacuvaj_karte("sve_karte.txt", "|", sveKarte)
    sveKarte2 = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|") # dict
    #print(sveKarte2)
    return
#dodaj_random_kartu()
         
                                    
def dodaj_random_let():                                       
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|") # dict
    let = letovi.napravi_random_let()
    pun_let = {let["broj_leta"]: let}
    sviLetovi.update(pun_let)
    ocisti_file("svi_letovi.txt")
    letovi.sacuvaj_letove("svi_letovi.txt", "|", sviLetovi)
    sviLetovi2 = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|") # dict
    #print(sviLetovi2)
    
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    konkretni_letovi.podesi_sledeci_broj_sifre(sviKonkretniLetovi)
    konkretniLetovi = konkretni_letovi.kreiranje_konkretnog_leta({}, let)
    print(konkretniLetovi)
    for konkretniLet in konkretniLetovi:
        letovi.podesi_matricu_zauzetosti(sviLetovi2, konkretniLetovi[konkretniLet])
        sviKonkretniLetovi.update({konkretniLetovi[konkretniLet]["sifra"]: konkretniLetovi[konkretniLet]})
    #print(sviKonkretniLetovi)
    ocisti_file("svi_konkretni_letovi.txt")
    konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)
    sviKonkretniLetovi2 = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|") 
    print(sviKonkretniLetovi2)
    return
#dodaj_random_let()


def pregled_letova():
    sviLetovi3 = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|") # dict
    print("\n\n", sviLetovi3)
    #quit()
   
   
###################################################################################################
 
# 20) IZVESTAVANJE  

def izabrana_opcija_izvestavanje():
    global trenutni_ulogovan_korisnik
    print("\n\n──────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("IZVESTAVANJE\n", "yellow", attrs = ["underline", "bold"]), "\n")
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    sviKorisnici = korisnici.ucitaj_korisnike_iz_fajla("svi_korisnici.txt", "|")
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    while (True):
        print(colored("\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
        print(colored("1) LISTA PRODATIH KARATA ZA IZABRANI DAN PRODAJE", "red"))
        print(colored("2) LISTA PRODATIH KARATA ZA IZABRANI DAN POLASKA", "red"))
        print(colored("3) LISTA PRODATIH KARATA ZA IZABRANI DAN PRODAJE I IZABRANOG PRODAVCA", "red"))
        print(colored("4) UKUPAN BROJ I CENA PRODATIH KARATA ZA IZABRANI DAN PRODAJE", "red"))
        print(colored("5) UKUPAN BROJ I CENA PRODATIH KARATA ZA IZABRANI DAN POLASKA", "red"))
        print(colored("6) UKUPAN BROJ I CENA PRODATIH KARATA ZA IZABRANI DAN PRODAJE I IZABRANOG PRODAVCA", "red"))
        print(colored("7) UKUPAN BROJ I CENA PRODATIH KARATA U POSLEDNJIH 30 DANA, PO PRODAVCIMA", "red"))
        print(colored("8) POVRATAK NA MENI\n\n", "red"))
        option = str(input("Unesite redni broj opcije koju želite: "))
        print("\n")
        if option == "1":
            while (True):
                datum = str(input("Unesite dan prodaje (YYYY-MM-DD): "))
                try:
                    datum2 = datetime.strptime(datum, "%Y-%m-%d")
                    datum = datetime(datum2.year, datum2.month, datum2.day)
                    break
                except ValueError:
                    print(colored("\n\nGRESKA: 'datum' nije dobro definisan. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                    continue
            listaKarata = izvestaji.izvestaj_prodatih_karata_za_dan_prodaje(sveKarte, datum)
            print(colored("\n\nPREGLED PRODATIH KARATA ZA DAN PRODAJE\n\n", "yellow", attrs = ["bold"]))
            newLista = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC", "ZA BRISANJE"]]
            num = 1
            for karta in listaKarata:
                brojKarte = karta["broj_karte"]
                datum = sveKarte[brojKarte]['datum_prodaje']
                date1 = str(datum.year) + "/" + str(datum.month) + "/" + str(datum.day)
                obrisana = "NEOZNAČENA"
                if sveKarte[brojKarte]["obrisana"] is True:
                    obrisana = "OZNAČENA"
                if sveKarte[brojKarte]['status'] == "nerealizovana_karta":
                    status = "NEREALIZOVANA"
                else:
                    status = "REALIZOVANA"
                newList = [num, sveKarte[brojKarte]["broj_karte"], 
                            sveKarte[brojKarte]['sifra_konkretnog_leta'], date1, status,
                            str(sveKarte[brojKarte]["kupac"]["ime"] + " " + sveKarte[brojKarte]["kupac"]["prezime"]), obrisana]
                newLista.append(newList)
                num += 1
            if len(newLista) == 1:
                print(colored("\n\nTrenutno ne postoji ni jedna karta koja odgovara Vašem zahtevu!\n\n", "red", attrs = ["bold"]))
                izabrana_opcija_izvestavanje()
                return  
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n") 
            print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")   
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return 
        elif option == "2":
            while (True):
                datum = str(input("Unesite dan polaska (YYYY-MM-DD): "))
                try:
                    datum2 = datetime.strptime(datum, "%Y-%m-%d")
                    datum = datetime(datum2.year, datum2.month, datum2.day)
                    break
                except ValueError:
                    print(colored("\n\nGRESKA: 'datum' nije dobro definisan. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                    continue
            listaKarata = izvestaji.izvestaj_prodatih_karata_za_dan_polaska(sveKarte, sviKonkretniLetovi, datum)
            print(colored("\n\nPREGLED PRODATIH KARATA ZA DAN POLASKA\n\n", "yellow", attrs = ["bold"]))
            newLista = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC", "ZA BRISANJE"]]
            num = 1
            for karta in listaKarata:
                brojKarte = karta["broj_karte"]
                datum = sveKarte[brojKarte]['datum_prodaje']
                date1 = str(datum.year) + "/" + str(datum.month) + "/" + str(datum.day)
                obrisana = "NEOZNAČENA"
                if sveKarte[brojKarte]["obrisana"] is True:
                    obrisana = "OZNAČENA"
                if sveKarte[brojKarte]['status'] == "nerealizovana_karta":
                    status = "NEREALIZOVANA"
                else:
                    status = "REALIZOVANA"
                newList = [num, sveKarte[brojKarte]["broj_karte"], 
                            sveKarte[brojKarte]['sifra_konkretnog_leta'], date1, status,
                            str(sveKarte[brojKarte]["kupac"]["ime"] + " " + sveKarte[brojKarte]["kupac"]["prezime"]), obrisana]
                newLista.append(newList)
                num += 1
            if len(newLista) == 1:
                print(colored("\n\nTrenutno ne postoji ni jedna karta koja odgovara Vašem zahtevu!\n\n", "red", attrs = ["bold"]))
                izabrana_opcija_izvestavanje()
                return  
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n") 
            print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")   
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return 
        elif option == "3":
            while (True):
                datum = str(input("Unesite dan prodaje (YYYY-MM-DD): "))
                try:
                    datum2 = datetime.strptime(datum, "%Y-%m-%d")
                    datum = datetime(datum2.year, datum2.month, datum2.day)
                    break
                except ValueError:
                    print(colored("\n\nGRESKA: 'datum' nije dobro definisan. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                    continue
            while (True):
                korisnicko = str(input("Unesite korisničko ime prodavca: "))   
                if korisnicko not in sviKorisnici:
                    print(colored("\n\nGRESKA: 'korisničko ime' ne postoji. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")         
                    continue
                if sviKorisnici[korisnicko]["uloga"] != "prodavac":
                    print(colored("\n\nGRESKA: ovaj korisnik nije prodavac. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")         
                    continue
                break
            listaKarata = izvestaji.izvestaj_prodatih_karata_za_dan_prodaje_i_prodavca(sveKarte, datum, sviKorisnici[korisnicko])
            print(colored("\n\nPREGLED PRODATIH KARATA ZA DAN POLASKA\n\n", "yellow", attrs = ["bold"]))
            newLista = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC", "ZA BRISANJE"]]
            num = 1
            for karta in listaKarata:
                brojKarte = karta["broj_karte"]
                datum = sveKarte[brojKarte]['datum_prodaje']
                date1 = str(datum.year) + "/" + str(datum.month) + "/" + str(datum.day)
                obrisana = "NEOZNAČENA"
                if sveKarte[brojKarte]["obrisana"] is True:
                    obrisana = "OZNAČENA"
                if sveKarte[brojKarte]['status'] == "nerealizovana_karta":
                    status = "NEREALIZOVANA"
                else:
                    status = "REALIZOVANA"
                newList = [num, sveKarte[brojKarte]["broj_karte"], 
                            sveKarte[brojKarte]['sifra_konkretnog_leta'], date1, status,
                            str(sveKarte[brojKarte]["kupac"]["ime"] + " " + sveKarte[brojKarte]["kupac"]["prezime"]), obrisana]
                newLista.append(newList)
                num += 1
            if len(newLista) == 1:
                print(colored("\n\nTrenutno ne postoji ni jedna karta koja odgovara Vašem zahtevu!\n\n", "red", attrs = ["bold"]))
                izabrana_opcija_izvestavanje()
                return  
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n") 
            print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")   
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return     
        elif option == "4":
            while (True):
                datum = str(input("Unesite dan prodaje (YYYY-MM-DD): "))
                try:
                    datum2 = datetime.strptime(datum, "%Y-%m-%d")
                    datum = datetime(datum2.year, datum2.month, datum2.day)
                    break
                except ValueError:
                    print(colored("\n\nGRESKA: 'datum' nije dobro definisan. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                    continue
            br, cena = izvestaji.izvestaj_ubc_prodatih_karata_za_dan_prodaje(sveKarte, sviKonkretniLetovi, sviLetovi, datum)
            print(colored("\n\n\nBroj prodatih karata na zadati dan: ", "green", attrs = ["bold"]), end = "")
            print(colored(br, "green", attrs = ["bold"]), "\n")
            print(colored("Ukupna cena karata: ", "green", attrs = ["bold"]), end = "")
            print(colored(cena, "green", attrs = ["bold"]), "\n")
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return 
        elif option == "5":
            while (True):
                datum = str(input("Unesite dan polaska (YYYY-MM-DD): "))
                try:
                    datum2 = datetime.strptime(datum, "%Y-%m-%d")
                    datum = datetime(datum2.year, datum2.month, datum2.day)
                    break
                except ValueError:
                    print(colored("\n\nGRESKA: 'datum' nije dobro definisan. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                    continue
            br, cena = izvestaji.izvestaj_ubc_prodatih_karata_za_dan_polaska(sveKarte, sviKonkretniLetovi, sviLetovi, datum)
            print(colored("\n\n\nBroj prodatih karata na zadati dan: ", "green", attrs = ["bold"]), end = "")
            print(colored(br, "green", attrs = ["bold"]), "\n")
            print(colored("Ukupna cena karata: ", "green", attrs = ["bold"]), end = "")
            print(colored(cena, "green", attrs = ["bold"]), "\n")
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return 
        elif option == "6":
            while (True):
                datum = str(input("Unesite dan prodaje (YYYY-MM-DD): "))
                try:
                    datum2 = datetime.strptime(datum, "%Y-%m-%d")
                    datum = datetime(datum2.year, datum2.month, datum2.day)
                    break
                except ValueError:
                    print(colored("\n\nGRESKA: 'datum' nije dobro definisan. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                    continue
            while (True):
                korisnicko = str(input("Unesite korisničko ime prodavca: "))   
                if korisnicko not in sviKorisnici:
                    print(colored("\n\nGRESKA: 'korisničko ime' ne postoji. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")         
                    continue
                if sviKorisnici[korisnicko]["uloga"] != "prodavac":
                    print(colored("\n\nGRESKA: ovaj korisnik nije prodavac. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")         
                    continue
                break    
            br, cena = izvestaji.izvestaj_ubc_prodatih_karata_za_dan_prodaje_i_prodavca(sveKarte, sviKonkretniLetovi, sviLetovi, datum, sviKorisnici[korisnicko])
            print(colored("\n\n\nBroj prodatih karata na zadati dan: ", "green", attrs = ["bold"]), end = "")
            print(colored(br, "green", attrs = ["bold"]), "\n")
            print(colored("Ukupna cena karata: ", "green", attrs = ["bold"]), end = "")
            print(colored(cena, "green", attrs = ["bold"]), "\n")
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return 
        elif option == "7":
            newDict = izvestaji.izvestaj_ubc_prodatih_karata_30_dana_po_prodavcima(sveKarte, sviKonkretniLetovi, sviLetovi)
            lista = [["REDNI BR.", "PRODAVAC", "BROJ KARATA", "UKUPNA CENA"]]
            num = 1
            for i in newDict:
                lista.append([num, i, newDict[i][0], newDict[i][1]])
                num += 1
            if len(lista) == 1:
                print(colored("\n\nLista je prazna!\n\n", "red", attrs = ["bold"]))
                izabrana_opcija_izvestavanje()
                return  
            print("\n\n────────────────────────────────────────────────────────────\n\n") 
            print(tabulate(lista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
            print("\n\n────────────────────────────────────────────────────────────\n\n")   
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return         
        elif option == "8":    
            print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
            print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return      
        else:
            print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))    
            continue         
            

###################################################################################################

# 19) IZMENA LETOVA

def izabrana_opcija_izmena_letova():
    global trenutni_ulogovan_korisnik
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    print("\n\n──────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("IZMENA LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    while (True):
        print(colored("Molimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
        print(colored("1) PREGLED SVIH LETOVA", "red"))
        print(colored("2) DIREKTNI UNOS BROJ LETA", "red"))
        print(colored("3) POVRATAK NA MENI\n\n", "red"))
        option = str(input("Unesite redni broj opcije koju želite: "))
        if option == "1":
            lista = letovi.pregled_svih_letova(sviLetovi)
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
            print(colored("\nPREGLED SVIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print(tabulate(lista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
        if option == "2" or option == "1":
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
            brojLeta = str(input("Unesite broj leta: "))
            if brojLeta is None or brojLeta == "":
                print(colored("\n\nGREŠKA: 'broj leta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                izabrana_opcija_izmena_letova()
                return
            if brojLeta not in sviLetovi:
                print(colored("\n\n\nGREŠKA: 'broj leta' ne postoji. Unesite ponovo.\n", "light_red"))
                izabrana_opcija_izmena_letova()
                return 
            oki = 0
            print("\nMolimo Vas da unesete sledeće podatke (ako ne želite da izmenite nešto, samo stisnite enter): \n")
            sifraPolazisnogAerodroma = input("Unesite šifru polazišnog aerodroma: ")
            if sifraPolazisnogAerodroma is None or sifraPolazisnogAerodroma == "":
                sifraPolazisnogAerodroma = sviLetovi[brojLeta]["sifra_polazisnog_aerodroma"]
            else:
                oki = 1
            sifraOdredisnogAerodorma = input("Unesite šifru odredišnog aerodroma: ")
            if sifraOdredisnogAerodorma is None or sifraOdredisnogAerodorma == "":
                sifraOdredisnogAerodorma = sviLetovi[brojLeta]["sifra_odredisnog_aerodorma"]
            else:
                oki = 1    
            vremePoletanja = input("Unesite vreme poletanja (hh:mm): ")
            if vremePoletanja is None or vremePoletanja == "":
                vremePoletanja = sviLetovi[brojLeta]["vreme_poletanja"]
            else:
                oki = 1    
            vremeSletanja = input("Unesite vreme sletanja (hh:mm): ")
            if vremeSletanja is None or vremeSletanja == "":
                vremeSletanja = sviLetovi[brojLeta]["vreme_sletanja"]
            else:
                oki = 1    
            sletanjeSutra = str(input("Unesite 'sletanje sutra' (False/True): "))
            if sletanjeSutra is None or sletanjeSutra == "":
                sletanjeSutra = sviLetovi[brojLeta]["sletanje_sutra"]
            else:
                oki = 1    
            prevoznik = input("Unesite prevoznika: ")
            if prevoznik is None or prevoznik == "":
                prevoznik = sviLetovi[brojLeta]["prevoznik"]
            else:
                oki = 1   
            dani = []
            while (True):
                ok = 1
                danii = str(input("Unesite dane u kojim se let obavlja (0 - 6, bez zareza, jedan broj za drugim): "))
                if danii == "" or dani is None:
                    dani = sviLetovi[brojLeta]["dani"]
                    break
                for i in range(0, len(danii)):
                    if ord(danii[i]) < 48 or ord(danii[i]) > 54:  
                        print(colored("\n\nGRESKA: 'dani' nije dobro definisano. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")
                        ok = 0
                        break
                    dan = int(danii[i])
                    if dan not in dani:
                        dani.append(dan)
                if ok == 0:
                    dani = []
                    continue
                oki = 1
                break
            listaModela = [["REDNI BR.", "ID MODELA", "NAZIV", "BROJ REDOVA", "POZICIJE SEDISTA"]]   
            sviModeli = model_aviona.ucitaj_modele_aviona("svi_modeli.txt", "|")  
            num = 1   
            for model in sviModeli:
                newList = [num, sviModeli[model]["id"], sviModeli[model]["naziv"], sviModeli[model]["broj_redova"], sviModeli[model]["pozicije_sedista"]]
                listaModela.append(newList)
                num += 1
            print(colored("\n\nPREGLED SVIH MODELA AVIONA\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print(tabulate(listaModela, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
            print("\n")
            while (True):
                model = str(input("Unesite id modela aviona: "))
                if model == "" or model is None:
                    model = sviLetovi[brojLeta]["model"]["id"]
                    break
                for i in model:
                    if ord(i) < 48 or ord(i) > 57:
                        print(colored("\n\nGRESKA: 'model' nije dobro definisano. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                        continue
                if int(model) not in sviModeli:
                    print(colored("\n\nGRESKA: 'model' ne postoji. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                    continue
                oki = 1
                break
            cena = input("Unesite cenu leta: ")
            if cena == "" or cena is None:
                cena = sviLetovi[brojLeta]["cena"]
            else:
                oki = 1
            datum1 = sviLetovi[brojLeta]["datum_pocetka_operativnosti"]
            datum2 = sviLetovi[brojLeta]["datum_kraja_operativnosti"]
            while (True):
                datumPocetkaOperativnosti = input("Unesite datum početka operativnosti leta (YYYY-MM-DD HH:MM:SS), npr. '2023-03-13 22:54:00'): ")
                if datumPocetkaOperativnosti != "" and datumPocetkaOperativnosti is not None:
                    try:     
                        datum1 = datetime.strptime(datumPocetkaOperativnosti, "%Y-%m-%d %H:%M:%S")
                        oki = 1
                    except ValueError:
                        print("GRESKA: 'datum pocetka operativnosti' nije dobro definisano. Unesite ponovo.")
                        continue
                else:
                    break
            while (True):
                datumKrajaOperativnosti = input("Unesite datum kraja operativnosti leta (YYYY-MM-DD HH:MM:SS), npr. '2023-03-13 22:54:00': ")
                if datumKrajaOperativnosti != "" and datumKrajaOperativnosti is not None:
                    try:
                        datum2 = datetime.strptime(datumKrajaOperativnosti, "%Y-%m-%d %H:%M:%S")
                        oki = 1
                        break
                    except ValueError:
                        print("GRESKA: 'datum kraja operativnosti' nije dobro definisano. Unesite ponovo.")
                        continue
                else:
                    break
            if oki == 0:
                print("\n\n", colored("LET JE NEPROMENJEN!\n", "light_red", attrs = ["bold"]))    
                print("─────────────────────────────────────────────────────────────────────────────\n\n")
                trenutno_prijavljen(trenutni_ulogovan_korisnik)
                return    
            try:   
                sviLetoviDopunjen = letovi.izmena_letova(sviLetovi, brojLeta, sifraPolazisnogAerodroma,
                                                        sifraOdredisnogAerodorma, vremePoletanja,
                                                        vremeSletanja, sletanjeSutra, prevoznik, dani,
                                                        sviModeli[int(model)], cena, datum1, datum2)
                if sletanjeSutra == "False":
                    sletanjeSutra = False
                elif sletanjeSutra == "True":
                    sletanjeSutra = True
                let = letovi.kreiraj_poseban_let(brojLeta, sifraPolazisnogAerodroma,
                                         sifraOdredisnogAerodorma, vremePoletanja, vremeSletanja,
                                         sletanjeSutra, prevoznik, dani, sviModeli[int(model)], cena,
                                         datum1, datum2)
                sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
                konkretni_letovi.podesi_sledeci_broj_sifre(sviKonkretniLetovi)
                konkretniLetovi = konkretni_letovi.kreiranje_konkretnog_leta({}, let)
                for konkretniLet in konkretniLetovi:
                    letovi.podesi_matricu_zauzetosti(sviLetovi, konkretniLetovi[konkretniLet])
                    sviKonkretniLetovi.update({konkretniLetovi[konkretniLet]["sifra"]: konkretniLetovi[konkretniLet]})
                ocisti_file("svi_letovi.txt")
                letovi.sacuvaj_letove("svi_letovi.txt", "|", sviLetoviDopunjen)
                ocisti_file("svi_konkretni_letovi.txt")
                konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)
                print("\n")
                print(colored("IZMENA LETA USPEŠNA.\n\n", "green", attrs = ["bold", "underline"]))
                print("─────────────────────────────────────────────────────────────────────────────\n")
                return
            except Exception as greska1:
                greska = colored(greska1, "light_red")
                print("\n\n", colored("IZMENA LETA NEUSPEŠNA!\n", "light_red", attrs = ["bold"]), greska, "\n\n")    
                izabrana_opcija_izmena_letova()
                return    
            
            
        elif option == "3":
            print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
            print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return  
        else:
            print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))    
            continue    
         
    
###################################################################################################

# 18) KREIRANJE MODELA AVIONA

def kreiranje_modela_obrada():
    global trenutni_ulogovan_korisnik
    sviModeli = model_aviona.ucitaj_modele_aviona("svi_modeli.txt", "|") 
    model_aviona.podesi_sledeci_id_modela(sviModeli)
    print("Molimo Vas da unesete sledeće podatke: \n")
    naziv = input("Unesite naziv modela aviona: ")
    for model in sviModeli:
        if sviModeli[model]["naziv"] == naziv:
            print(colored("\n\nGRESKA: 'naziv modela' već postoji. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")
            izabrana_opcija_kreiranje_modela_aviona()
            return
    brojRedova = input("Unesite broj redova u avionu: ")
    pozicijeSedista = str(input("Unesite pozicije sedišta u avionu ('A' - 'Z', bez zareza, jedno veliko slovo za drugim): "))
    pozicije = []
    for i in range(0, len(pozicijeSedista)):
        if ord(pozicijeSedista[i]) < 65 or ord(pozicijeSedista[i]) > 90:  
            print(colored("\n\nGRESKA: 'pozicije sedista' nisu dobro definisane. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")
            kreiranje_modela_obrada(sviModeli)
            return
        pozicije.append(pozicijeSedista[i])
    try:
        sviModeliDopunjen = model_aviona.kreiranje_modela_aviona(sviModeli, naziv, brojRedova, pozicije)
        ocisti_file("svi_modeli.txt")
        model_aviona.sacuvaj_modele_aviona("svi_modeli.txt", "|", sviModeliDopunjen)
        print("\n")
        print(colored("\nKREIRANJE MODELA AVIONA USPEŠNO!\n\n", "green", attrs = ["bold", "underline"]))
        print("─────────────────────────────────────────────────────────────────────────────\n")
        return
    except Exception as greska1:
        greska = colored(greska1, "light_red")
        print("\n\n", colored("KREIRANJE MODELA AVIONA NEUSPEŠNO!\n", "light_red", attrs = ["bold"]), greska, "\n\n")    
        izabrana_opcija_kreiranje_modela_aviona()
        return
    
def izabrana_opcija_kreiranje_modela_aviona():
    print("\n\n──────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("KREIRANJE MODELA AVIONA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    while (True):
        print(colored("Molim Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
        print(colored("1) KREIRAJ MODEL AVIONA", "red"))
        print(colored("2) POVRATAK NA MENI\n", "red"))
        opcija = str(input("\nUnesite redni broj opcije koju želite: "))
        if opcija == "1":
            print("\n")
            kreiranje_modela_obrada()
            return
        elif opcija == "2":
            print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
            print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return  
        else:
            print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))    
            continue    
 

###################################################################################################

# 17) KREIRANJE LETOVA

def kreiranje_leta_obrada():
    global trenutni_ulogovan_korisnik
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|") # dict
    print("Molimo Vas da unesete sledeće podatke: \n")
    brojLeta = input("Unesite broj leta (npr. 'ss56'): ")
    sifraPolazisnogAerodroma = input("Unesite šifru polazišnog aerodroma: ")
    sifraOdredisnogAerodorma = input("Unesite šifru odredišnog aerodroma: ")
    vremePoletanja = input("Unesite vreme poletanja (hh:mm): ")
    vremeSletanja = input("Unesite vreme sletanja (hh:mm): ")
    sletanjeSutra = str(input("Unesite 'sletanje sutra' (False/True): "))
    prevoznik = input("Unesite prevoznika: ")
    dani = []
    while (True):
        ok = 1
        danii = str(input("Unesite dane u kojim se let obavlja (0 - 6, bez zareza, jedan broj za drugim): "))
        if danii == "" or dani is None:
            print(colored("\n\nGRESKA: 'dani' je prazno. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")
            continue
        for i in range(0, len(danii)):
            if ord(danii[i]) < 48 or ord(danii[i]) > 54:  
                print(colored("\n\nGRESKA: 'dani' nije dobro definisano. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")
                ok = 0
                break
            dan = int(danii[i])
            if dan not in dani:
                dani.append(dan)
        if ok == 0:
            dani = []
            continue
        break
    listaModela = [["REDNI BR.", "ID MODELA", "NAZIV", "BROJ REDOVA", "POZICIJE SEDISTA"]]   
    sviModeli = model_aviona.ucitaj_modele_aviona("svi_modeli.txt", "|")  
    num = 1   
    for model in sviModeli:
        newList = [num, sviModeli[model]["id"], sviModeli[model]["naziv"], sviModeli[model]["broj_redova"], sviModeli[model]["pozicije_sedista"]]
        listaModela.append(newList)
        num += 1
    print(colored("\n\nPREGLED SVIH MODELA AVIONA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print(tabulate(listaModela, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
    print("\n")
    while (True):
        model = str(input("Unesite id modela aviona: "))
        if model == "" or model is None:
            print(colored("\n\nGRESKA: 'model' je prazno. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")
            continue
        for i in model:
            if ord(i) < 48 or ord(i) > 57:
                print(colored("\n\nGRESKA: 'model' nije dobro definisano. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
                continue
        if int(model) not in sviModeli:
            print(colored("\n\nGRESKA: 'model' ne postoji. Unesite ponovo.", "light_red", attrs = ["bold"]), "\n\n")    
            continue
        break
    cena = input("Unesite cenu leta: ")
    while (True):
        datumPocetkaOperativnosti = input("Unesite datum početka operativnosti leta (YYYY-MM-DD HH:MM:SS), npr. '2023-03-13 22:54:00'): ")
        try:     
            datum1 = datetime.strptime(datumPocetkaOperativnosti, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("GRESKA: 'datum pocetka operativnosti' nije dobro definisano. Unesite ponovo.")
            continue
        datumKrajaOperativnosti = input("Unesite datum kraja operativnosti leta (YYYY-MM-DD HH:MM:SS), npr. '2023-03-13 22:54:00': ")
        try:
            datum2 = datetime.strptime(datumKrajaOperativnosti, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("GRESKA: 'datum kraja operativnosti' nije dobro definisano. Unesite ponovo.")
            continue
        break
    try:
        sviLetoviDopunjen = letovi.kreiranje_letova(sviLetovi, brojLeta, sifraPolazisnogAerodroma,
                                                    sifraOdredisnogAerodorma, vremePoletanja,
                                                    vremeSletanja, sletanjeSutra, prevoznik, dani,
                                                    sviModeli[int(model)], cena, datum1, datum2)
        if sletanjeSutra == "False":
            sletanjeSutra = False
        elif sletanjeSutra == "True":
            sletanjeSutra = True
        let = letovi.kreiraj_poseban_let(brojLeta, sifraPolazisnogAerodroma,
                                         sifraOdredisnogAerodorma, vremePoletanja, vremeSletanja,
                                         sletanjeSutra, prevoznik, dani, sviModeli[int(model)], cena,
                                         datum1, datum2)
        sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
        konkretni_letovi.podesi_sledeci_broj_sifre(sviKonkretniLetovi)
        konkretniLetovi = konkretni_letovi.kreiranje_konkretnog_leta({}, let)
        for konkretniLet in konkretniLetovi:
            letovi.podesi_matricu_zauzetosti(sviLetovi, konkretniLetovi[konkretniLet])
            sviKonkretniLetovi.update({konkretniLetovi[konkretniLet]["sifra"]: konkretniLetovi[konkretniLet]})
        ocisti_file("svi_letovi.txt")
        letovi.sacuvaj_letove("svi_letovi.txt", "|", sviLetoviDopunjen)
        ocisti_file("svi_konkretni_letovi.txt")
        konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)
        print("\n")
        print(colored("KREIRANJE LETA USPEŠNO.\n\n", "green", attrs = ["bold", "underline"]))
        print("─────────────────────────────────────────────────────────────────────────────\n")
        return
    except Exception as greska1:
        greska = colored(greska1, "light_red")
        print("\n\n", colored("KREIRANJE LETA NEUSPEŠNO!\n", "light_red", attrs = ["bold"]), greska, "\n\n")    
        izabrana_opcija_kreiranje_letova()
        return

def izabrana_opcija_kreiranje_letova():
    print("\n\n──────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("KREIRANJE LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    while (True):
        print(colored("Molim Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
        print(colored("1) KREIRAJ LET", "red"))
        print(colored("2) POVRATAK NA MENI\n", "red"))
        opcija = str(input("\nUnesite redni broj opcije koju želite: "))
        if opcija == "1":
            print("\n")
            kreiranje_leta_obrada()
            return
        elif opcija == "2":
            print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
            print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return  
        else:
            print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))    
            continue


###################################################################################################

# 16) REGISTROVANJE PRODAVACA

def izabrana_opcija_registrovanje_prodavaca():
    print("\n\n──────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("REGISTRACIJA PRODAVACA", "yellow", attrs = ["underline", "bold"]), "\n")
    sviKorisnici = korisnici.ucitaj_korisnike_iz_fajla("svi_korisnici.txt", "|") # dict
    print("Molimo Vas da unesete sledeće podatke: ")
    staroKorisnickoIme = input("Staro korisničko ime (nije obavezno): ")
    novoKorisnickoIme = input("Novo korisničko ime: ")
    lozinka = input("Lozinka: ")
    ime = input("Ime: ")
    prezime = input("Prezime: ")
    email = input("Email: ")
    pasos = input("Pasoš (nije obavezno): ")
    drzavljanstvo = input("Državljanstvo (nije obavezno): ")
    telefon = input("Telefon: ")
    pol = input("Pol (nije obavezno): ")
    try:
        sviKorisniciDopunjen = korisnici.kreiraj_korisnika(sviKorisnici, False, "prodavac",
                                                           staroKorisnickoIme, novoKorisnickoIme,
                                                           lozinka, ime, prezime, email, pasos,
                                                           drzavljanstvo, telefon, pol)
        ocisti_file("svi_korisnici.txt")
        korisnici.sacuvaj_korisnike("svi_korisnici.txt", "|", sviKorisniciDopunjen)
        print("\n")
        print(colored("Prodavac", "green"), end = "")
        print(colored(" '", "light_green"), end = "")
        print(colored(novoKorisnickoIme, "light_green", attrs = ["underline"]), end = "")
        print(colored("' ", "light_green"), end = "")
        print(colored("je uspešno registrovan!\n", "green"), "\n\n")
        print("─────────────────────────────────────────────────────────────────────────────\n\n\n")
        return
    except Exception as greska1:
        greska = colored(greska1, "light_red")
        print("\n\n", colored("REGISTRACIJA NEUSPELA!\n", "light_red", attrs = ["bold"]), greska, "\n\n")    
        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
        if opcijaNazad == 'x':
            print("\n\n")
            return
        else:
            print("\n\n")
            izabrana_opcija_registrovanje_prodavaca(sviKorisnici) 
            return 


###################################################################################################

# 15) BRISANJE KARTE - ADMIN

def izabrana_opcija_brisanje_karte_admin(korisnik):
    print("\n\n──────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("BRISANJE KARATA", "yellow", attrs = ["underline", "bold"]), "\n")
    Korisnik = korisnik
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    lista = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC", "ZA BRISANJE"]]
    num = 1
    for karta in sveKarte:
        if sveKarte[karta]["obrisana"] is False:
            continue
        datum = sveKarte[karta]['datum_prodaje']
        date1 = str(datum.year) + "/" + str(datum.month) + "/" + str(datum.day)
        obrisana = "NEOZNAČENA"
        if sveKarte[karta]["obrisana"] is True:
            obrisana = "OZNAČENA"
        if sveKarte[karta]['status'] == "nerealizovana_karta":
            status = "NEREALIZOVANA"
        else:
            status = "REALIZOVANA"
        newList = [num, sveKarte[karta]["broj_karte"], 
                   sveKarte[karta]['sifra_konkretnog_leta'], date1, status,
                   str(sveKarte[karta]["kupac"]["ime"] + " " + sveKarte[karta]["kupac"]["prezime"]), obrisana]
        lista.append(newList)
        num += 1
    if len(lista) == 1:
        print(colored("\n\nTrenutno nema ni jedna karta označena za brisanje!\n", "red", attrs = ["bold"]), "\n")
        while (True):
            print(colored("\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
            print(colored("1) OPCIJA 'OZNAČI KARTU ZA BRISANJE'", "red"))
            print(colored("2) POVRATAK NA MENI\n\n", "red"))   
            opcija5 = str(input("Unesite redni broj opcije koju želite: "))
            if opcija5 == "1":
                print("\n\n")
                izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                return
            elif opcija5 == "2":
                print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
                trenutno_prijavljen(trenutni_ulogovan_korisnik)
                return   
            else:
                print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                continue
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")         
    print(tabulate(lista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
    while (True):
        print(colored("Molimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
        print(colored("1) OBRIŠI SVE KARTE", "red"))
        print(colored("2) OBRIŠI ODABRANE KARTE", "red")) 
        print(colored("3) OPCIJA 'OZNAČI KARTU ZA BRISANJE'", "red")) 
        print(colored("4) POVRATAK NA MENI\n\n", "red"))   
        option = str(input("Unesite redni broj opcije koju želite: "))
        if option == "1":
            while (True):
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("BRISANJE SVIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                print(colored("\nDa li ste sigurni da želite da izbrišete sve označene karte?\n", "light_red"))
                print(colored("1) DA", "red"))
                print(colored("2) NE\n\n", "red")) 
                opcija = str(input("Unesite redni broj opcije koju želite: "))
                if opcija == "1":
                    newKarte = {}
                    for karta in sveKarte:
                        brojKarte = sveKarte[karta]["broj_karte"]
                        if sveKarte[karta]["obrisana"] is False:
                            newKarte.update({brojKarte: sveKarte[karta]})
                        else:
                            if sveKarte[karta]["status"] == "realizovana_karta" or sveKarte[karta]["sediste"] != "":
                                sediste = sveKarte[karta]["sediste"]
                                s = sediste.split(",")
                                sifra = sveKarte[karta]["sifra_konkretnog_leta"]
                                zauzetost = sviKonkretniLetovi[sifra]["zauzetost"]
                                zauzetost[int(s[0]) - 1][int(s[0]) - 1] = False
                    ocisti_file("svi_konkretni_letovi.txt")
                    konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)  
                    ocisti_file("sve_karte.txt")
                    karte.sacuvaj_karte(newKarte, "sve_karte.txt", "|") 
                    print(colored("\n\nSve označene karte su USPEŠNO OBRISANE!\n", "green", attrs = ["bold"]))
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                    return       
                elif opcija == "2":
                    print("\n\n")
                    break
                else:
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                    continue
        elif option == "2":
            lista = {-1}
            while (True):
                ok = 1
                brojKarte = str(input("\nUnesite broj karte: "))
                if brojKarte is None or brojKarte == "":
                    print(colored("\n\nGREŠKA: 'broj karte' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                    continue
                for i in brojKarte:
                    if ord(i) < 48 or ord(i) > 57:
                        print(colored("\n\n\nGREŠKA: 'broj karte' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                        ok = 0
                        break
                if ok == 0:
                    continue
                if int(brojKarte) not in sveKarte:
                    print(colored("\n\n\nGREŠKA: 'broj karte' ne postoji. Unesite ponovo.\n", "light_red"))
                    continue
                if sveKarte[int(brojKarte)]["obrisana"] is False:
                    while (True):
                        print(colored("\n\nOva karta nije označena za brisanje.\n", "light_red"))
                        print(colored("Da li želite da odaberete i ovu kartu za brisanje?\n", "light_red"))
                        print(colored("1) DA", "red"))
                        print(colored("2) NE\n\n", "red")) 
                        x = str(input("Unesite redni broj opcije koju želite: "))
                        if x == "1":
                            lista.add(int(brojKarte))
                            print("\n\n", colored("Karta broj '", "green"), end = "")
                            print(colored(str(brojKarte), "green"), end = "")
                            print(colored("' je USPEŠNO DODANA u listu za brisanje!\n", "green", attrs = ["bold"]))
                            break
                        if x == "2":
                            break
                        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                        continue
                else:
                    lista.add(int(brojKarte))
                    print("\n\n", colored("Karta broj '", "green"), end = "")
                    print(colored(str(brojKarte), "green"), end = "")
                    print(colored("' je USPEŠNO DODANA u listu za brisanje!\n", "green", attrs = ["bold"]))
                while (True):
                    ok = 1
                    print(colored("\n\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
                    print(colored("1) DODAJ NOVU KARTU U LISTU ZA BRISANJE", "red"))
                    print(colored("2) OBRIŠI SVE ODABRANE KARTE U LISTI", "red")) 
                    print(colored("3) POVRATAK NA MENI\n\n", "red"))
                    opcija = str(input("Unesite redni broj opcije koju želite: "))
                    if opcija == "1": 
                        print("\n\n")
                        break
                    elif opcija == "2": 
                        lista.remove(-1)
                        if len(lista) == 0:
                            print(colored("\n\n\nNiste uneli ni jednu kartu za brisanje.\n", "light_red"))
                            izabrana_opcija_brisanje_karte_admin(Korisnik)
                            return
                        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                        print(colored("BRISANJE ODABRANIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                        print(colored("\nPREGLED ODABRANIH KARATA ZA BRISANJE\n\n", "yellow", attrs = ["bold"]), "\n")
                        newLista = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC", "ZA BRISANJE"]]
                        num = 1
                        for karta in sveKarte:
                            if sveKarte[karta]["broj_karte"] not in lista:
                                continue
                            datum = sveKarte[karta]['datum_prodaje']
                            date1 = str(datum.year) + "/" + str(datum.month) + "/" + str(datum.day)
                            obrisana = "NEOZNAČENA"
                            if sveKarte[karta]["obrisana"] is True:
                                obrisana = "OZNAČENA"
                            if sveKarte[karta]['status'] == "nerealizovana_karta":
                                status = "NEREALIZOVANA"
                            else:
                                status = "REALIZOVANA"
                            newList = [num, sveKarte[karta]["broj_karte"], 
                                       sveKarte[karta]['sifra_konkretnog_leta'], date1, status,
                                       str(sveKarte[karta]["kupac"]["ime"] + " " + sveKarte[karta]["kupac"]["prezime"]), obrisana]
                            newLista.append(newList)
                            num += 1
                        if len(newLista) == 1:
                            print(colored("\n\n\nTrenutno nema ni jedna karta označena za brisanje!", "red", attrs = ["bold"]), "\n")
                            print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
                            izabrana_opcija_brisanje_karte_admin(Korisnik)
                            return      
                        print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
                        print("\n\n──────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")   
                        while (True):
                            print(colored("\nDa li želite da poništite brisanje za neku kartu?\n", "light_red"))
                            print(colored("1) DA", "red"))
                            print(colored("2) NE\n\n", "red")) 
                            opcija2 = str(input("Unesite redni broj opcije koju želite: "))
                            if opcija2 == "1":
                                while (True):    
                                    if len(lista) == 0:
                                        print(colored("\n\n\nPoništili ste brisanje za sve karte.\n", "light_red"))
                                        izabrana_opcija_brisanje_karte_admin(Korisnik)
                                        return
                                    print(colored("\n\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
                                    print(colored("1) ODABERI KARTU ZA PONIŠTAVANJE BRISANJA", "red"))
                                    print(colored("2) OBRIŠI SVE ODABRANE KARTE", "red")) 
                                    opcija3 = str(input("\nUnesite redni broj opcije koju želite: "))
                                    if opcija3 == "1":
                                        while (True):
                                            ok = 1
                                            brojKarte = str(input("\nUnesite broj karte: "))
                                            if brojKarte is None or brojKarte == "":
                                                print(colored("\n\nGREŠKA: 'broj karte' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                                                continue
                                            for i in brojKarte:
                                                if ord(i) < 48 or ord(i) > 57:
                                                    print(colored("\n\n\nGREŠKA: 'broj karte' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                                                    ok = 0
                                                    break
                                            if ok == 0:
                                                continue
                                            if int(brojKarte) not in sveKarte:
                                                print(colored("\n\n\nGREŠKA: 'broj karte' ne postoji. Unesite ponovo.\n", "light_red"))
                                                continue
                                            if int(brojKarte) not in lista:
                                                print(colored("\n\n\nGREŠKA: 'broj karte' ne postoji u listi odabranih karata za brisanje. Unesite ponovo.\n", "light_red"))
                                                continue
                                            break
                                        lista.remove(int(brojKarte))  
                                        print("\n\n", colored("Karta broj '", "green"), end = "")
                                        print(colored(str(brojKarte), "green"), end = "")
                                        print(colored("' je USPEŠNO SKLONJENA sa liste za brisanje!\n", "green", attrs = ["bold"]))      
                                        continue
                                    elif opcija3 == "2":
                                        print("\n")
                                        break
                                    else:
                                        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                                        continue     
                            elif opcija2 == "2":
                                print("\n")
                                break
                            else:
                                print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                                continue 
                        while (True):    
                            print(colored("\nDa li ste sigurni da želite da izbrišete sve označene karte?\n", "light_red"))
                            print(colored("1) DA", "red"))
                            print(colored("2) NE\n\n", "red")) 
                            opcija = str(input("Unesite redni broj opcije koju želite: "))
                            if opcija == "1":
                                newKarte = {}
                                for karta in sveKarte:
                                    brojKarte = sveKarte[karta]["broj_karte"]
                                    if brojKarte not in lista:
                                        newKarte.update({brojKarte: sveKarte[karta]})
                                    else:
                                        if sveKarte[karta]["status"] == "realizovana_karta" or sveKarte[karta]["sediste"] != "":
                                            sediste = sveKarte[karta]["sediste"]
                                            s = sediste.split(",")
                                            sifra = sveKarte[karta]["sifra_konkretnog_leta"]
                                            zauzetost = sviKonkretniLetovi[sifra]["zauzetost"]
                                            zauzetost[int(s[0]) - 1][int(s[0]) - 1] = False
                                ocisti_file("svi_konkretni_letovi.txt")
                                konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)  
                                ocisti_file("sve_karte.txt")
                                karte.sacuvaj_karte(newKarte, "sve_karte.txt", "|") 
                                print(colored("\n\nSve označene karte su USPEŠNO OBRISANE!\n", "green", attrs = ["bold"]))
                                print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                                return    
                            elif opcija == "2": 
                                print("\n\n")
                                izabrana_opcija_brisanje_karte_admin(Korisnik)
                                return
                            else:
                                print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                                continue  
                    elif opcija == "3": 
                        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                        print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                        print(colored("Brisanje karata se poništava!\n", "yellow", attrs = ["bold"]), "\n")
                        print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                        trenutno_prijavljen(trenutni_ulogovan_korisnik)
                        return       
                    else:
                        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                        continue   
                continue
        elif option == "3":
            izabrana_opcija_brisanje_karte_prodavac(Korisnik)
            return
        elif option == "4":
            print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
            print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return          
        else:
            print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
            izabrana_opcija_brisanje_karte_admin(Korisnik)
            return


###################################################################################################

# 14) PREGLED PRODATIH KARATA PO PARAMETRIMA

def izabrana_opcija_pregled_prodatih_karata():
    global trenutni_ulogovan_korisnik
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("\n\nPREGLED PRODATIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print(colored("Molimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
    print(colored("1) PREGLED SVIH KARATA", "red"))
    print(colored("2) UNOS PARAMETARA PRETRAGE\n\n", "red"))
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    while (True):
        option = str(input("Unesite redni broj opcije koju želite: "))
        if option == "1":
            num = 1
            newLista = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC"]]
            for karta in sveKarte:
                datum = sveKarte[karta]['datum_prodaje']
                date1 = str(datum.year) + "/" + str(datum.month) + "/" + str(datum.day)
                if sveKarte[karta]['status'] == "nerealizovana_karta":
                    status = "NEREALIZOVANA"
                else:
                    status = "REALIZOVANA"
                newList = [num, sveKarte[karta]["broj_karte"], 
                           sveKarte[karta]['sifra_konkretnog_leta'],
                           date1, status,
                           str(sveKarte[karta]["kupac"]["ime"] + " " + sveKarte[karta]["kupac"]["prezime"])]
                newLista.append(newList)
                num += 1
            if len(newLista) == 1:
                print(colored("\n\n\nTrenutno nema ni jedna kupljena karta!", "red", attrs = ["bold"]), "\n")
                print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
                return    
            print("\n\n")           
            print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
            return
        if option == "2" or option == "1":
            print("\n\nMolimo Vas da unesete sledeće podatke: \n")
            polaziste = str(input("Unesite šifru polazišnog aerodroma: "))
            odrediste = str(input("Unesite šifru odredišnog aerodroma: "))
            datum_polaska = str(input("Unesite datum polaska (YYYY-MM-DD): "))
            datum_dolaska = str(input("Unesite datum dolaska (YYYY-MM-DD): "))
            ime_putnika = str(input("Unesite ime putnika: "))
            prezime_putnika = str(input("Unesite prezime putnika: "))
            try:
                (lista, listaParametara) = karte.pretraga_prodatih_karata(sveKarte, sviKonkretniLetovi, sviLetovi, polaziste, odrediste, datum_polaska, datum_dolaska, ime_putnika, prezime_putnika)
                newLista = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC"]]
                if len(lista) == 0:
                    print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                    print(colored("\nNiste uneli ništa od parametara.\n\n", "light_red"))
                    print(colored("PREGLED SVIH PRODATIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
                    num = 1
                    for karta in sveKarte:
                        datum = sveKarte[karta]['datum_prodaje']
                        date1 = str(datum.year) + "/" + str(datum.month) + "/" + str(datum.day)
                        if sveKarte[karta]['status'] == "nerealizovana_karta":
                            status = "NEREALIZOVANA"
                        else:
                            status = "REALIZOVANA"
                        newList = [num, sveKarte[karta]["broj_karte"], 
                                   sveKarte[karta]['sifra_konkretnog_leta'],
                                   date1, status,
                                   str(sveKarte[karta]["kupac"]["ime"] + " " + sveKarte[karta]["kupac"]["prezime"])]
                        newLista.append(newList)
                        num += 1
                    print("\n")
                    print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
                    print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
                    return    
                for i in lista:
                    newLista.append(i)
                print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                print(colored("\nIzabrali ste pretragu letova po ", "yellow"), end = "")
                lenListaParametara = len(listaParametara)
                for br in range(0, lenListaParametara):
                    if (br == lenListaParametara - 1):
                        print(colored(listaParametara[br], "yellow"), end = "")
                        print(colored(". \n", "yellow"))
                    elif (br == lenListaParametara - 2):
                        print(colored(listaParametara[br], "yellow"), end = "")  
                        print(colored(" i ", "yellow"), end = "")    
                    else:
                        print(colored(listaParametara[br], "yellow"), end = "")
                        print(colored(", ", "yellow"), end = "")
                print(colored("\nPREGLED IZABRANIH PRODATIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
                print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
                print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
                return
            except Exception as greska1:
                greska = colored(greska1, "light_red")
                print("\n\n\n", greska, "\n")   
                opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
                if opcijaNazad == 'x':
                    print("\n\n")
                    trenutno_prijavljen(trenutni_ulogovan_korisnik)
                    return
                else:
                    print("\n\n")
                    izabrana_opcija_pregled_prodatih_karata()
                    return
        else:
            print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
            opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
            if opcijaNazad == 'x':
                print("\n\n")
                trenutno_prijavljen(trenutni_ulogovan_korisnik)
                return
            print("\n\n")
            izabrana_opcija_pregled_prodatih_karata()
            return


###################################################################################################

# 13) BRISANJE KARTE PRODAVAC

def izabrana_opcija_brisanje_karte_prodavac(korisnik):
    Korisnik = korisnik
    print("\n\n──────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("BRISANJE KARTE\n", "yellow", attrs = ["underline", "bold"]), "\n")
    while (True):
        print(colored("Molimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
        print(colored("1) OZNAČI KARTU ZA BRISANJE", "red"))
        print(colored("2) PONIŠTI OZNAKU KARTE ZA BRISANJE", "red"))
        print(colored("3) PREGLED SVIH KARATA", "red"))
        print(colored("4) POVRATAK NA MENI\n\n", "red"))
        sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
        opcija = str(input("Unesite redni broj opcije koju želite: "))
        if opcija == "1":
            print(colored("\n\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
            print(colored("1) PREGLED SVIH KARATA", "red"))
            print(colored("2) DIREKTNI UNOS BROJA KARTE", "red"))
            print(colored("3) POVRATAK NA MENI\n\n", "red"))
            while (True):
                option = str(input("Unesite redni broj opcije koju želite: "))
                if option == "1":
                    num = 1
                    listaKarata = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "ZA BRISANJE"]]
                    for karta2 in sveKarte:
                        datum = sveKarte[karta2]["datum_prodaje"]
                        date1 = date(datum.year, datum.month, datum.day)
                        obrisana = "NEOZNAČENA"
                        if sveKarte[karta2]["obrisana"] is True:
                            obrisana = "OZNAČENA"
                        listaKarata.append([num, sveKarte[karta2]["broj_karte"], sveKarte[karta2]["sifra_konkretnog_leta"], date1, sveKarte[karta2]["status"], obrisana])
                        num += 1
                    if (len(listaKarata) == 1):
                        print(colored("\n\n\nGREŠKA: trenutno ne postoji ni jedna kupljena karta.\n", "light_red"))
                        return
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                    print(colored("\nPREGLED SVIH KUPLJENIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                    print(tabulate(listaKarata, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                if option == "2" or option == "1":
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")  
                    brojKarte = str(input("Unesite broj karte: "))
                    if brojKarte is None or brojKarte == "":
                        print(colored("\n\nGREŠKA: 'broj karte' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                        return
                    for i in brojKarte:
                        if ord(i) < 48 or ord(i) > 57:
                            print(colored("\n\n\nGREŠKA: 'broj karte' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                            izabrana_opcija_brisanje_karte_prodavac(Korisnik)   
                            return 
                        if int(brojKarte) not in sveKarte:
                            print(colored("\n\n\nGREŠKA: 'broj karte' ne postoji. Unesite ponovo.\n", "light_red"))
                            izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                            return
                    if sveKarte[int(brojKarte)]["obrisana"] is True:
                        print(colored("\n\nGREŠKA: karta je već označena za brisanje!\n\n", "light_red"))               
                        izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                        return
                    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
                    sveKarte[int(brojKarte)]["obrisana"] = True
                    ocisti_file("sve_karte.txt")
                    karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")  
                    print("\n\n", colored("Karta broj '", "green"), end = "")
                    print(colored(str(brojKarte), "green"), end = "")
                    print(colored("' je USPEŠNO OZNAČENA sa 'obrisana'!\n", "green", attrs = ["bold"]))
                    if korisnik["uloga"] == "prodavac":
                        print(colored("Da bi se karta potpuno izbrisala iz podataka, potrebna je dozvola admina!\n", "yellow"))
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                    return    
                elif option == "3":   
                    print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                    print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                    print("\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n\n") 
                    trenutno_prijavljen(trenutni_ulogovan_korisnik)
                    return          
                else:
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                    izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                    return
        elif opcija == "2":
            while (True):
                print(colored("\n\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
                print(colored("1) PREGLED SVIH KARATA", "red"))
                print(colored("2) DIREKTNI UNOS BROJA KARTE", "red"))
                print(colored("3) POVRATAK NA MENI\n\n", "red"))
                option = str(input("Unesite redni broj opcije koju želite: "))
                if option == "1":
                    num = 1
                    listaKarata = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "ZA BRISANJE"]]
                    for karta2 in sveKarte:
                        datum = sveKarte[karta2]["datum_prodaje"]
                        date1 = date(datum.year, datum.month, datum.day)
                        obrisana = "NEOZNAČENA"
                        if sveKarte[karta2]["obrisana"] is True:
                            obrisana = "OZNAČENA"
                        listaKarata.append([num, sveKarte[karta2]["broj_karte"], sveKarte[karta2]["sifra_konkretnog_leta"], date1, sveKarte[karta2]["status"], obrisana])
                        num += 1
                    if (len(listaKarata) == 1):
                        print(colored("\n\n\nGREŠKA: trenutno ne postoji ni jedna kupljena karta.\n", "light_red"))
                        return
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                    print(colored("\nPREGLED SVIH KUPLJENIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                    print(tabulate(listaKarata, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                if option == "2" or option == "1":
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")  
                    brojKarte = str(input("Unesite broj karte: "))
                    if brojKarte is None or brojKarte == "":
                        print(colored("\n\nGREŠKA: 'broj karte' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                        return
                    for i in brojKarte:
                        if ord(i) < 48 or ord(i) > 57:
                            print(colored("\n\n\nGREŠKA: 'broj karte' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                            izabrana_opcija_brisanje_karte_prodavac(Korisnik)   
                            return 
                        if int(brojKarte) not in sveKarte:
                            print(colored("\n\n\nGREŠKA: 'broj karte' ne postoji. Unesite ponovo.\n", "light_red"))
                            izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                            return
                    if sveKarte[int(brojKarte)]["obrisana"] is False:
                        print(colored("\n\nGREŠKA: karta je već označena sa 'neobrisana!\n\n", "light_red"))               
                        izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                        return
                    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
                    sveKarte[int(brojKarte)]["obrisana"] = False
                    ocisti_file("sve_karte.txt")
                    karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")  
                    print("\n\n", colored("Karta broj '", "green"), end = "")
                    print(colored(str(brojKarte), "green"), end = "")
                    print(colored("' je USPEŠNO OZNAČENA sa 'nije obrisana'!\n", "green", attrs = ["bold"]))
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                    return    
                elif option == "3":   
                    print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                    print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                    print("\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n\n") 
                    trenutno_prijavljen(trenutni_ulogovan_korisnik)
                    return          
                else:
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
                    izabrana_opcija_brisanje_karte_prodavac(Korisnik)
                    continue
        elif opcija == "3":
            num = 1
            listaKarata = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "ZA BRISANJE"]]
            for karta2 in sveKarte:
                datum = sveKarte[karta2]["datum_prodaje"]
                date1 = date(datum.year, datum.month, datum.day)
                obrisana = "NEOZNAČENA"
                if sveKarte[karta2]["obrisana"] is True:
                    obrisana = "OZNAČENA"
                listaKarata.append([num, sveKarte[karta2]["broj_karte"], sveKarte[karta2]["sifra_konkretnog_leta"], date1, sveKarte[karta2]["status"], obrisana])
                num += 1
            if (len(listaKarata) == 1):
                print(colored("\n\n\nGREŠKA: trenutno ne postoji ni jedna kupljena karta.\n", "light_red"))
                return
            print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n")
            print(colored("\nPREGLED SVIH KUPLJENIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print(tabulate(listaKarata, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))        
            print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────\n")
        elif opcija == "4":   
            print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
            print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
            print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return          
        else:
            print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
            izabrana_opcija_brisanje_karte_prodavac(Korisnik)
            return
    

###################################################################################################   

# 12) IZMENA KARATA

def izabrana_opcija_izmena_karata(korisnik):
    global trenutni_ulogovan_korisnik
    Korisnik = korisnik
    print("\n")
    print("\n\n──────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("IZMENA KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print(colored("Molimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
    print(colored("1) PREGLED SVIH KARATA", "red"))
    print(colored("2) DIREKTNI UNOS BROJA KARTE", "red"))
    print(colored("3) POVRATAK NA MENI\n\n", "red"))
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    option = str(input("Unesite redni broj opcije koju želite: "))
    if option == "1":
        num = 1
        listaKarata = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS"]]
        for karta2 in sveKarte:
            datum = sveKarte[karta2]["datum_prodaje"]
            date1 = date(datum.year, datum.month, datum.day)
            listaKarata.append([num, sveKarte[karta2]["broj_karte"], sveKarte[karta2]["sifra_konkretnog_leta"], date1, sveKarte[karta2]["status"]])
            num += 1
        if (len(listaKarata) == 1):
            print(colored("\n\n\nGREŠKA: trenutno ne postoji ni jedna kupljena karta.\n", "light_red"))
            return
        print("\n\n─────────────────────────────────────────────────────────────────────────────────────\n")
        print(colored("\nPREGLED SVIH KUPLJENIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
        print(tabulate(listaKarata, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
    if option == "2" or option == "1":
        print("\n\n─────────────────────────────────────────────────────────────────────────────────────\n\n")
        brojKarte = str(input("Unesite broj karte: "))
        if brojKarte is None or brojKarte == "":
            print(colored("\n\nGREŠKA: 'broj karte' je prazno. Unesite ponovo.\n\n", "light_red"))                  
            izabrana_opcija_izmena_karata(Korisnik)
            return
        for i in brojKarte:
            if ord(i) < 48 or ord(i) > 57:
                print(colored("\n\n\nGREŠKA: 'broj karte' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                izabrana_opcija_izmena_karata(Korisnik)   
                return 
        if int(brojKarte) not in sveKarte:
            print(colored("\n\n\nGREŠKA: 'broj karte' ne postoji. Unesite ponovo.\n", "light_red"))
            izabrana_opcija_izmena_karata(Korisnik)
            return
        karta = sveKarte[int(brojKarte)]
        staraSifra = karta["sifra_konkretnog_leta"]
        staroSediste = karta["sediste"]
        while (True):
            print("\n")
            print(colored("\n\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
            print(colored("1) IZMENA LETA", "red"))
            print(colored("2) IZMENA DATUMA POLASKA", "red"))
            print(colored("3) IZMENA SEDIŠTA U AVIONU", "red"))
            print(colored("4) POVRATAK NA MENI\n\n", "red"))
            opcija = str(input("Unesite redni broj opcije koju želite: "))
            if opcija == "1":
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("IZMENA LETA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                while (True):
                    ok = 1
                    novaSifra = str(input("Unesite šifru novog konkretnog leta: "))
                    if novaSifra is None or novaSifra == "":
                        print(colored("\n\nGREŠKA: 'šifra konkretnog leta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        continue
                    for i in novaSifra:
                        if ord(i) < 48 or ord(i) > 57:
                            print(colored("\n\n\nGREŠKA: 'šifra konkretnog leta' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                            ok = 0
                            break
                    if ok == 0:
                        continue
                    if int(novaSifra) not in sviKonkretniLetovi:
                        print(colored("\n\n\nGREŠKA: 'šifra konkretnog leta' ne postoji. Unesite ponovo.\n", "light_red"))
                        continue     
                    zauzetost = sviKonkretniLetovi[int(novaSifra)]["zauzetost"]
                    brSlobodnih = 0
                    for i in zauzetost:
                        for j in i:
                            if j is False:
                                brSlobodnih += 1
                    if brSlobodnih == 0:
                        print(colored("\n\n\nGREŠKA: trenutno nema slobodnih sedišta u ovom letu!\n", "light_red"))
                        break
                    staroSediste = sveKarte[int(brojKarte)]["sediste"]
                    s = staroSediste.split(",")   
                    if s[0] != "": 
                        sviKonkretniLetovi[staraSifra]["zauzetost"][int(s[0]) - 1][int(s[1]) - 1] = False
                    ocisti_file("svi_konkretni_letovi.txt")
                    konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)  
                    redovi = len(zauzetost) #4
                    kolone = len(zauzetost[0]) #6
                    lista = []
                    for i in range(0, redovi):
                        newLista = []
                        s = "RED "
                        s += str(i + 1)
                        s += ": "
                        newLista.append(s)
                        for j in range(0, kolone):
                            s = ""
                            if zauzetost[i][j] == True:
                                s += "x "
                                newLista.append(s)
                            else:
                                s += str(j + 1) + " "    
                                newLista.append(s)     
                        lista.append(newLista)
                    print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                    print(colored("\nPREGLED SEDIŠTA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                    print(tabulate(lista, tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
                    print(colored("Zauzeta sedišta su obeležena sa 'x'.\nMolimo Vas da izaberite jedno od slobodnih sedišta.\n", "yellow", attrs = ["bold"]), "\n")
                    while (True):
                        while (True):
                            ok = 1
                            red = str(input("Unesite red sedišta: "))
                            if red is None or red == "":
                                print(colored("\n\nGREŠKA: 'red sedišta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                                continue
                            for i in red:
                                if ord(i) < 48 or ord(i) > 57:
                                    print(colored("\n\nGREŠKA: 'red sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                                    ok = 0
                                    break
                            if ok == 0:
                                continue
                            if int(red) < 1 or int(red) > redovi:
                                print(colored("\n\nGREŠKA: 'red sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                                continue
                            break
                        while (True):    
                            broj = str(input("Unesite broj sedišta u odabranom " + red + ". redu: "))
                            if broj is None or broj == "":
                                print(colored("\n\nGREŠKA: 'broj sedišta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                                continue
                            ok = 1
                            for i in broj:
                                if ord(i) < 48 or ord(i) > 57:
                                    print(colored("\n\nGREŠKA: 'broj sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                                    ok = 0
                                    break
                            if ok == 0:
                                continue
                            if int(broj) < 1 or int(broj) > kolone:
                                print(colored("\n\nGREŠKA: 'broj sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                                continue
                            break
                        if zauzetost[int(red) - 1][int(broj) - 1] == True:
                            print(colored("\n\nGREŠKA: ovo sedište je već zauzeto! Unesite ponovo.\n\n", "light_red"))   
                            continue
                        else:
                            zauzetost[int(red) - 1][int(broj) - 1] = True
                            sviKonkretniLetovi[int(novaSifra)]["zauzetost"] = zauzetost
                            karta["sifra_konkretnog_leta"] = int(novaSifra)
                            karta["sediste"] = str(red) + "," + str(broj)
                            karta["status"] = "realizovana_karta"
                            sveKarte[int(brojKarte)] = karta
                            break      
                    ocisti_file("svi_konkretni_letovi.txt")
                    konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)
                    ocisti_file("sve_karte.txt")
                    karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")  
                    print(colored("\n\n\nIZMENA KARTE USPEŠNA!\n", "green", attrs = ["bold", "underline"]))            
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                    return
            elif opcija == "2":
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("IZMENA DATUMA POLASKA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                while (True):
                    noviDatum = str(input("Unesite novi datum polaska (YYYY-MM-DD): "))
                    try:
                        datumPolaska = datetime.strptime(noviDatum, '%Y-%m-%d')
                    except ValueError:
                       print("\nGREŠKA: 'datum polaska' nije definisano u formatu 'YYYY-MM-DD'. Unesite ponovo.\n")
                       continue
                    date1 = datetime(datumPolaska.year, datumPolaska.month, datumPolaska.day)
                    ok = 0
                    for let in sviKonkretniLetovi:
                        date2 = datetime(sviKonkretniLetovi[let]["datum_i_vreme_polaska"].year, sviKonkretniLetovi[let]["datum_i_vreme_polaska"].month, sviKonkretniLetovi[let]["datum_i_vreme_polaska"].day) 
                        if date2 == date1:
                            ok = 1
                            novaSifra = sviKonkretniLetovi[let]["sifra"]
                            zauzetost = sviKonkretniLetovi[let]["zauzetost"]
                            brSlobodnih = 0
                            for i in range(0, len(zauzetost)):
                                for j in range(0, len(zauzetost[i])):
                                    if zauzetost[i][j] is False:
                                        brSlobodnih += 1
                                        ok = 1
                                        break
                                if ok == 1:
                                    break
                            if brSlobodnih == 0:
                                ok = 2
                                continue
                            break
                    if ok == 0:
                        print("\nGREŠKA: u ovom datumu se ne realizuje ni jedan let. Unesite ponovo.\n")        
                        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
                        if opcijaNazad == 'x':
                            print("\n\n")
                            trenutno_prijavljen(trenutni_ulogovan_korisnik)
                            return
                        print("\n\n")
                        continue
                    if ok == 2:
                        print("\nGREŠKA: svi letovi na ovaj dan su već zauzeti! Unesite novi.")        
                        if opcijaNazad == 'x':
                            print("\n")
                            trenutno_prijavljen(trenutni_ulogovan_korisnik)
                            return
                        print("\n\n")
                        continue
                    s = staroSediste.split(",")
                    if s[0] != "":
                        sviKonkretniLetovi[staraSifra]["zauzetost"][int(s[0]) - 1][int(s[1]) - 1] = False
                        ocisti_file("svi_konkretni_letovi.txt")
                        konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)
                        redovi = len(zauzetost) #4
                        kolone = len(zauzetost[0]) #6
                        lista = []
                        for i in range(0, redovi):
                            newLista = []
                            s = "RED "
                            s += str(i + 1)
                            s += ": "
                            newLista.append(s)
                            for j in range(0, kolone):
                                s = ""
                                if zauzetost[i][j] == True:
                                    s += "x "
                                    newLista.append(s)
                                else:
                                    s += str(j + 1) + " "    
                                    newLista.append(s)     
                            lista.append(newLista)
                        print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                        print(colored("\nPREGLED SEDIŠTA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                        print(tabulate(lista, tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
                        print(colored("Zauzeta sedišta su obeležena sa 'x'.\nMolimo Vas da izaberite jedno od slobodnih sedišta.\n", "yellow", attrs = ["bold"]), "\n")
                        while (True):
                            while (True):
                                ok = 1
                                red = str(input("Unesite red sedišta: "))
                                if red is None or red == "":
                                    print(colored("\n\nGREŠKA: 'red sedišta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                                    continue
                                for i in red:
                                    if ord(i) < 48 or ord(i) > 57:
                                        print(colored("\n\nGREŠKA: 'red sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                                        ok = 0
                                        break
                                if ok == 0:
                                    continue
                                if int(red) < 1 or int(red) > redovi:
                                    print(colored("\n\nGREŠKA: 'red sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                                    continue
                                break
                            while (True):    
                                broj = str(input("Unesite broj sedišta u odabranom " + red + ". redu: "))
                                if broj is None or broj == "":
                                    print(colored("\n\nGREŠKA: 'broj sedišta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                                    continue
                                ok = 1
                                for i in broj:
                                    if ord(i) < 48 or ord(i) > 57:
                                        print(colored("\n\nGREŠKA: 'broj sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                                        ok = 0
                                        break
                                if ok == 0:
                                    continue
                                if int(broj) < 1 or int(broj) > kolone:
                                    print(colored("\n\nGREŠKA: 'broj sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                                    continue
                                break
                            if zauzetost[int(red) - 1][int(broj) - 1] == True:
                                print(colored("\n\nGREŠKA: ovo sedište je već zauzeto! Unesite ponovo.\n\n", "light_red"))   
                                continue
                            else:
                                zauzetost[int(red) - 1][int(broj) - 1] = True
                                sviKonkretniLetovi[int(novaSifra)]["zauzetost"] = zauzetost
                                karta["sediste"] = str(red) + "," + str(broj)
                                break   
                    karta["sifra_konkretnog_leta"] = int(novaSifra)      
                    sveKarte[int(brojKarte)] = karta     
                    ocisti_file("svi_konkretni_letovi.txt")
                    konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)
                    ocisti_file("sve_karte.txt")
                    karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")  
                    print(colored("\n\n\nIZMENA KARTE USPEŠNA!\n", "green", attrs = ["bold", "underline"]))            
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                    return
            elif opcija == "3":
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("IZMENA SEDIŠTA U AVIONU\n", "yellow", attrs = ["underline", "bold"]), "\n")    
                if sveKarte[int(brojKarte)]["sediste"] == "":
                    print(colored("\n\nGREŠKA: ova karta uopšte nije čekirana!\n\n", "light_red"))
                    print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
                    return
                zauzetost = sviKonkretniLetovi[staraSifra]["zauzetost"]
                redovi = len(zauzetost) #4
                kolone = len(zauzetost[0]) #6
                lista = []
                for i in range(0, redovi):
                    newLista = []
                    s = "RED "
                    s += str(i + 1)
                    s += ": "
                    newLista.append(s)
                    for j in range(0, kolone):
                        s = ""
                        if zauzetost[i][j] == True:
                            s += "x "
                            newLista.append(s)
                        else:
                            s += str(j + 1) + " "    
                            newLista.append(s)     
                    lista.append(newLista)
                print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                print(colored("\nPREGLED SEDIŠTA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                print(tabulate(lista, tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
                print(colored("Zauzeta sedišta su obeležena sa 'x'.\nMolimo Vas da izaberite jedno od slobodnih sedišta.\n", "yellow", attrs = ["bold"]), "\n")
                while (True):
                    print("\n")
                    ok = 1
                    noviRed = str(input("Unesite red novog sedišta: "))
                    if noviRed is None or noviRed == "":
                        print(colored("\n\nGREŠKA: 'red sedišta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        continue
                    for i in noviRed:
                        if ord(i) < 48 or ord(i) > 57:
                            print(colored("\n\nGREŠKA: 'red sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                            ok = 0
                            break
                    if ok == 0:
                        continue
                    if int(noviRed) < 1 or int(noviRed) > redovi:
                        print(colored("\n\nGREŠKA: 'red sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                        continue
                    break
                while (True):    
                    noviBroj = str(input("Unesite broj novog sedišta u odabranom " + noviRed + ". redu: "))
                    if noviBroj is None or noviBroj == "":
                        print(colored("\n\nGREŠKA: 'broj sedišta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        continue
                    ok = 1
                    for i in noviBroj:
                        if ord(i) < 48 or ord(i) > 57:
                            print(colored("\n\nGREŠKA: 'broj sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                            ok = 0
                            break
                    if ok == 0:
                        continue
                    if int(noviBroj) < 1 or int(noviBroj) > kolone:
                        print(colored("\n\nGREŠKA: 'broj sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                        continue
                    break
                if zauzetost[int(noviRed) - 1][int(noviBroj) - 1] == True:
                    print(colored("\n\nGREŠKA: ovo sedište je već zauzeto! Unesite ponovo.\n\n", "light_red"))   
                    izabrana_opcija_izmena_karata(Korisnik)
                    return
                else:
                    staroSediste2 = ""
                    for i in range(0, len(staroSediste)):
                        staroSediste2 += staroSediste[i]
                    s = staroSediste2.split(",")
                    print(staraSifra)
                    print(sviKonkretniLetovi[staraSifra]["zauzetost"])
                    print(s, "\n\n")
                    sviKonkretniLetovi[staraSifra]["zauzetost"][int(s[0]) - 1][int(s[1]) - 1] = False
                    ocisti_file("svi_konkretni_letovi.txt")
                    konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)
                    novoSediste = str(noviRed) + "," + str(noviBroj)
                    sveKarte[int(brojKarte)]["sediste"] = novoSediste
                    sviKonkretniLetovi[staraSifra]["zauzetost"][int(noviRed) - 1][int(noviBroj) - 1] = True
                    ocisti_file("svi_konkretni_letovi.txt")
                    konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", sviKonkretniLetovi)
                    ocisti_file("sve_karte.txt")
                    karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")  
                    print(colored("\n\n\nIZMENA KARTE USPEŠNA!\n", "green", attrs = ["bold", "underline"]))            
                    print("\n\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                    return      
            elif opcija == "4":
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                trenutno_prijavljen(trenutni_ulogovan_korisnik)
                return
            else:
               print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
               continue 
    elif option == "3":
        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
        print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
        print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
        trenutno_prijavljen(trenutni_ulogovan_korisnik)
        return          
    else:
        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
        if opcijaNazad == 'x':
            print("\n\n")
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return
        print("\n\n")
        izabrana_opcija_izmena_karata(Korisnik)
        return


###################################################################################################   

# 11) CHECK-IN PRODAVAC

def izabrana_opcija_check_in_prodavac(korisnik):
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    num = 1
    Korisnik = korisnik
    listaKarata = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS"]]
    for karta in sveKarte:
        if sveKarte[karta]["status"] == "nerealizovana_karta":
            datum = sveKarte[karta]["datum_prodaje"]
            date1 = date(datum.year, datum.month, datum.day)
            listaKarata.append([num, sveKarte[karta]["broj_karte"], sveKarte[karta]["sifra_konkretnog_leta"], date1, sveKarte[karta]["status"]])
            num += 1
    if len(listaKarata) == 1:
        print(colored("\n\nTrenutno nema ni jedna kupljena nerealizovana karta.", "red", attrs = ["bold"]))            
        while (True):   
            print("\n\nDa li želite da izabere opciju: PRODAJA KARATA?\n")
            print(colored("1) DA", "red"))
            print(colored("2) NE", "red"))
            print(colored("3) POVRATAK NA MENI\n\n", "red"))
            odgovor = str(input("Unesite redni broj opcije koju želite: "))
            if odgovor == "1":   
                izabrana_opcija_prodaja_karata(Korisnik)
                return
            elif odgovor == "2":
                print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                return
            elif odgovor == "3":
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                trenutno_prijavljen(trenutni_ulogovan_korisnik)
                return      
            else:    
                print(colored("\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))                      
    print("\n\n───────────────────────────────────────────────────────────────────────────────────\n")
    print(colored("\nPREGLED SVIH KUPLJENIH NEREALIZOVANIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print(tabulate(listaKarata, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
    print("\n\n───────────────────────────────────────────────────────────────────────────────────\n\n")
    while (True):
        ok = 1
        brojKarte = str(input("Unesite broj karte koju želite da čekirate: "))
        if brojKarte == "" or brojKarte is None:
            print(colored("\n\nGREŠKA: 'broj karte' je prazno. Unesite ponovo.\n\n", "light_red"))               
        for i in brojKarte:
            if ord(i) < 48 or ord(i) > 57:
                print(colored("\n\nGREŠKA: 'broj karte' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))    
                ok = 0
                break
        if ok == 0:
            continue
        if int(brojKarte) not in sveKarte:
            print(colored("\n\nGREŠKA: 'broj karte' ne postoji. Unesite ponovo.\n\n", "light_red"))               
            continue
        break
    izabrana_opcija_direktan_check_in(sveKarte[int(brojKarte)]["kupac"], sveKarte[int(brojKarte)])
    return


###################################################################################################   

# 10) PRODAJA KARATA
 
def izabrana_opcija_prodaja_karata(korisnik):
    Korisnik = korisnik
    global trenutni_ulogovan_korisnik
    print("\n\n──────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("PRODAJA KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print(colored("\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
    print(colored("1) PREGLED SVIH KONKRETNIH LETOVA", "red"))
    print(colored("2) DIREKTNI UNOS ŠIFRE LETA", "red"))
    print(colored("3) POVRATAK NA MENI\n\n", "red"))
    option = str(input("Unesite redni broj opcije koju želite: "))
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    sviKorisnici = korisnici.ucitaj_korisnike_iz_fajla("svi_korisnici.txt", "|")
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    if option == "1":
        lista = konkretni_letovi.pregled_svih_konkretnih_letova(sviLetovi, sviKonkretniLetovi)
        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
        print(colored("\nPREGLED SVIH KONKRETNIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n")
        print(tabulate(lista, tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
    if option == "2" or option == "1":
        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
        sifra = str(input("Unesite šifru konkretnog leta: "))
        if sifra is None or sifra == "":
            print(colored("\n\nGREŠKA: 'šifra konkretnog leta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
            izabrana_opcija_prodaja_karata(Korisnik)
            return
        for i in sifra:
            if ord(i) < 48 or ord(i) > 57:
                print(colored("\n\n\nGREŠKA: 'šifra konkretnog leta' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                izabrana_opcija_prodaja_karata(Korisnik)   
                return 
        if int(sifra) not in sviKonkretniLetovi:
            print(colored("\n\n\nGREŠKA: 'šifra konkretnog leta' ne postoji. Unesite ponovo.\n", "light_red"))
            izabrana_opcija_prodaja_karata(Korisnik)
            return
        slobodnaMesta = letovi.matrica_zauzetosti(sviKonkretniLetovi[int(sifra)])
        putnici = []
        brojSlobodnih = 0
        zaKoga = ""
        brojRedova = len(slobodnaMesta)
        for i in range(0, brojRedova):
            for j in slobodnaMesta[i]:
                if j == False:
                    brojSlobodnih += 1
        if brojSlobodnih == 0:
            print(colored("\n\n\nNažalost, trenutno nema slobodnih mesta za ovaj let.\n", "light_red", attrs = ["bold"]))  
            print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")      
            print(colored("\nDa li želite da nastavite sa kupovinom karata?\n", "yellow"))
            while (True):
                print(colored("\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
                print(colored("1) NASTAVAK PRODAJE KARATA", "red"))
                print(colored("2) POVRATAK NA MENI\n\n", "red"))
                odgovor = str(input("Unesite redni broj opcije koju želite: "))
                if odgovor == "1":   
                    izabrana_opcija_prodaja_karata(Korisnik)
                    return
                elif odgovor == "2":
                    print("\n\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                    return
                else:
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))           
        else:
            print(colored("\n\n\nBroj ukupnih slobodnih mesta na ovom letu:", "green"), colored(brojSlobodnih, "green"), colored("\n\n\n", "green"))        
            while (True):   
                print(colored("Molim Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
                print(colored("1) KUPUJEM KARTU ZA REGISTROVANOG KUPCA", "red"))
                print(colored("2) KUPUJEM KARTU ZA NEREGISTROVANOG KUPCA\n\n", "red"))
                zaKogaKarta = str(input("Unesite redni broj opcije koju želite: "))
                if zaKogaKarta == "1":
                    while (True):
                        print("\n")
                        zaKoga = str(input("Unesite korisničko ime registrovanog kupca: "))
                        if zaKoga not in sviKorisnici:
                            print(colored("\n\nGREŠKA: 'korisničko ime' ne postoji. Unesite ponovo.\n", "light_red"))
                            continue
                        break
                    print(colored("\n\nPodaci o korisniku uspešno preuzeti.\n\n", "green", attrs = ["bold"]))
                    newDict = {zaKoga: sviKorisnici[zaKoga]}
                    putnici.append(newDict)
                    break
                if zaKogaKarta == "2":
                    print(colored("\n\nUnesite sledeće podatke za neregistrovanog kupca:\n", "light_grey"))
                    while (True):
                        ok = 1
                        imeOsobe = str(input("IME: "))
                        if imeOsobe is None or imeOsobe == "":
                            print(colored("\n\nGREŠKA: 'ime osobe' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in imeOsobe:
                            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                                print(colored("\n\nGREŠKA: 'ime osobe' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(imeOsobe) > 15:
                            print(colored("\n\nGREŠKA: 'ime osobe' ne može biti duže od 15 slova. Unesite ponovo.\n\n", "light_red"))            
                            continue
                        prezimeOsobe = str(input("PREZIME: "))
                        if prezimeOsobe is None or prezimeOsobe == "":
                            print(colored("\n\nGREŠKA: 'prezime osobe' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in prezimeOsobe:
                            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                                print(colored("\n\nGREŠKA: 'prezime osobe' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(prezimeOsobe) > 20:
                            print(colored("\n\nGREŠKA: 'prezime osobe' ne može biti duže od 20 slova. Unesite ponovo.\n\n", "light_red"))
                            continue    
                        telefonOsobe = str(input("BROJ TELEFONA: "))
                        if telefonOsobe is None or telefonOsobe == "":
                            print(colored("\n\nGREŠKA: 'broj telefona' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in telefonOsobe:
                            if ord(i.lower()) < 48 or ord(i.lower()) > 57:
                                print(colored("\n\nGREŠKA: 'broj telefona' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(imeOsobe) > 10:
                            print(colored("\n\nGREŠKA: 'broj telefona' ne može biti duže od 10 slova. Unesite ponovo.\n\n", "light_red"))
                            continue
                        emailOsobe = str(input("E-MAIL: "))
                        if emailOsobe is None or emailOsobe == "":
                            print(colored("\n\nGREŠKA: 'e-mail' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        monkey1 = 0
                        checkBeforeMonkey = ""
                        checkEmail = ""
                        for i in emailOsobe:   # tamara.cvjetkovic@gmail.com
                            if monkey1:
                                checkEmail += i
                            if i == '@':
                                if checkBeforeMonkey == '':
                                    print(colored("\n\nGREŠKA: 'e-mail' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                                    ok = 0
                                    break
                                monkey1 += 1 
                            checkBeforeMonkey += i 
                        if ok == 0:
                            continue       
                        if monkey1 == 0 or monkey1 > 1:
                            print(colored("\n\nGREŠKA: 'e-mail' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                            continue
                        numOfDots = 0
                        dot1 = 0
                        checkAfterDot = ""
                        checkAfterMonkey = ""
                        for i in checkEmail:
                            if dot1:
                                checkAfterDot += i
                            if i == ".":
                                if checkAfterMonkey == '':
                                    print(colored("\n\nGREŠKA: 'e-mail' je prazno. Unesite ponovo.\n\n", "light_red"))
                                    ok = 0
                                    break
                                dot1 = 1
                                numOfDots += 1
                            checkAfterMonkey += i
                        if ok == 0:
                            continue
                        if numOfDots != 1:
                            print(colored("\n\nGREŠKA: 'e-mail' je prazno. Unesite ponovo.\n\n", "light_red"))
                            continue
                        if checkAfterDot == '':
                            print(colored("\n\nGREŠKA: 'e-mail' je prazno. Unesite ponovo.\n\n", "light_red"))
                            continue
                        break
                    putnici.append({"ime": imeOsobe, "prezime": prezimeOsobe, "telefon": telefonOsobe, "email": emailOsobe, "uloga": "korisnik", "pasos": "", "drzavljanstvo": "", "pol": ""})
                    print("\n")
                    break
                print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n\n", "light_red"))          
            while (True):
                print(colored("Da li želite da dodate saputnika?:\n", "light_grey"))
                print(colored("1) DA", "red"))
                print(colored("2) NE\n\n", "red"))
                opcija2 = str(input("Unesite redni broj opcije koju želite: "))
                if opcija2 == "1":
                    print(colored("\n\nUnesite sledeće podatke saputnika:\n", "light_grey"))
                    while (True):
                        ok = 1
                        imeOsobe = str(input("IME: "))
                        if imeOsobe is None or imeOsobe == "":
                            print(colored("\n\nGREŠKA: 'ime osobe' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in imeOsobe:
                            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                                print(colored("\n\nGREŠKA: 'ime osobe' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(imeOsobe) > 15:
                            print(colored("\n\nGREŠKA: 'ime osobe' ne može biti duže od 15 slova. Unesite ponovo.\n\n", "light_red"))            
                        prezimeOsobe = str(input("PREZIME: "))
                        if prezimeOsobe is None or prezimeOsobe == "":
                            print(colored("\n\nGREŠKA: 'prezime osobe' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in prezimeOsobe:
                            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                                print(colored("\n\nGREŠKA: 'prezime osobe' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(prezimeOsobe) > 20:
                            print(colored("\n\nGREŠKA: 'prezime osobe' ne može biti duže od 20 slova. Unesite ponovo.\n\n", "light_red"))
                        break
                    #sviNeregistrovani = korisnici.ucitaj_neregistrovane_korisnike_iz_fajla("svi_neregistrovani_korisnici.txt", "|")
                    #neregistrovani = korisnici.kreiraj_neregistrovanog(sviNeregistrovani, imeOsobe, prezimeOsobe)
                    putnici.append({"ime": imeOsobe, "prezime": prezimeOsobe, "pasos": "", "drzavljanstvo": "", "pol": ""})
                    #sviNeregistrovani.update(neregistrovani)
                    #ocisti_file("svi_neregistrovani_korisnici.txt")
                    #korisnici.sacuvaj_neregistrovane_korisnike("svi_neregistrovani_korisnici.txt", "|", sviNeregistrovani)
                    print("\n")
                    continue
                elif opcija2 == "2":
                    break
                else:
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))
            # dodao sve putnike, potvrda kupovine
            today = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
            try:
                if (zaKoga == ""):
                    (kartaNew, sveKarteNew) = karte.kupovina_karte(sveKarte, sviKonkretniLetovi, int(sifra), putnici, slobodnaMesta, putnici[0], prodavac = Korisnik, datum_prodaje = today)  
                else:
                    (kartaNew, sveKarteNew) = karte.kupovina_karte(sveKarte, sviKonkretniLetovi, int(sifra), putnici, slobodnaMesta, sviKorisnici[zaKoga], prodavac = Korisnik, datum_prodaje = today)  
                kartaNew["sediste"] = "" 
                sveKarteNew[kartaNew["broj_karte"]]["sediste"] = ""
                ocisti_file("sve_karte.txt")    
                karte.sacuvaj_karte(sveKarteNew, "sve_karte.txt", "|")
                poruka = "Kupovina karte USPEŠNA!"
                s = "┌───"
                g = "└───"
                for i in range(0, len(poruka) - 1):
                    s += "─"
                    g += "─"
                s += "┐"    
                g += "┘"
                print("\n\n")
                print(colored(s, "green"))
                print(colored("│ ", "green"), end = "")
                print(colored("Kupovina karte USPEŠNA!", "green", attrs = ["bold"]), end = "")
                print(colored(" │", "green")) 
                print(colored(g, "green"), "\n\n")
                print("\n")
                print(colored("NAPOMENA: ", "yellow", attrs = ["bold"]), end = "")
                print(colored("predlažemo Vam da odmah uradite check-in za kupca, kako biste što pre mogli izabrati njegovo željeno sedište.\n", "yellow"))
                print(colored("VAŽNO OBAVEŠTENJE: ", "yellow", attrs = ["bold"]), end = "")       
                print(colored("check-in se može obaviti najranije 48h pre poletanja.", "yellow"))
                print(colored("Ukoliko ne čekirate Vašu kartu 48h pre poletanja, Vaša karta će postati nevažeća,\nte će Vam biti onemogućen ulazak u avion i let istim.", "yellow"))
                print(colored("\nTaca Airlines® ne snosi nikakve novčane naknade, te je Vaša dužnost da uredno čekirate kartu na vreme.\n\n", "yellow"))
                print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                while (True):
                    print("Da li želite odmah da čekirate upravo kupljenu kartu za kupca?\n")
                    print(colored("1) DA", "red"))
                    print(colored("2) NE", "red"))
                    print(colored("3) POVRATAK NA MENI\n\n", "red"))
                    odgovor = str(input("Unesite redni broj opcije koju želite: "))
                    if odgovor == "1":   
                        if zaKoga != "":               
                            izabrana_opcija_direktan_check_in(sviKorisnici[zaKoga], kartaNew)
                        else:
                            izabrana_opcija_direktan_check_in(putnici[0], kartaNew)
                        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
                        break
                    elif odgovor == "2":
                        break
                    elif odgovor == "3":
                        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                        print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                        print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                        trenutno_prijavljen(trenutni_ulogovan_korisnik)
                        return  
                    else:
                        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red")) 
                        continue          
                print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n") 
                print(colored("Da li želite da vidite karte za letove povezane sa prethodnim letom?\n\n", "yellow"))
                print(colored("1) DA", "red"))
                print(colored("2) NE", "red"))
                print(colored("3) POVRATAK NA MENI\n\n", "red"))
                while (True):
                    option = str(input("Unesite redni broj opcije koju želite: "))
                    if option == "1":
                        listaPovezanihLetova = letovi.povezani_letovi(sviLetovi, sviKonkretniLetovi, sviKonkretniLetovi[int(sifra)])
                        if len(listaPovezanihLetova) == 1:
                            print(colored("\n\n\nNažalost, trenutno ne postoji ni jedan povezani let za Vaš let.\nVraćamo Vas na glavni meni.\n", "light_red", attrs = ["bold"]))
                            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                            if Korisnik["uloga"] == "korisnik":
                                ulogovan_kao_korisnik(Korisnik)
                                return
                            if Korisnik["uloga"] == "prodavac":
                                ulogovan_kao_prodavac(Korisnik) 
                                return
                            if Korisnik["uloga"] == "admin":
                                ulogovan_kao_admin(Korisnik) 
                                return       
                        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                        print(colored("\nPREGLED SVIH POVEZANIH KONKRETNIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
                        print(tabulate(listaPovezanihLetova, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                        if zaKoga != "":
                            izabrana_opcija_povezani_letovi(sviKorisnici[zaKoga], listaPovezanihLetova)     
                            return
                        else:
                            izabrana_opcija_povezani_letovi(putnici[0], listaPovezanihLetova)     
                            return
                    elif option == "2":
                        print("\n\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                        return
                    elif option == "3":
                        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                        print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                        print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                        trenutno_prijavljen(trenutni_ulogovan_korisnik)
                        return  
                    else:
                        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))    
            except Exception as greska1:
                greska = colored(greska1, "light_red")
                print("\n\n\n", greska, "\n\n")
                izabrana_opcija_prodaja_karata(Korisnik)
                return
    elif option == "3":
        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
        print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
        print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
        trenutno_prijavljen(trenutni_ulogovan_korisnik)
        return    
    else:
        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))
        izabrana_opcija_prodaja_karata(Korisnik)
        return
    
 
###################################################################################################   

# 9) PREGLED NEREALIZOVANIH KARATA
    
def izabrana_opcija_pregled_nerealizovanih_karata(korisnik):
    Korisnik = korisnik
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")  
    newLista = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS"]]
    lista = karte.pregled_nerealizovanaih_karata(Korisnik, sveKarte)
    for i in lista:
        newLista.append(i)
    if len(newLista) == 1:
        print("\n\n\n─────────────────────────────────────────────────────────────────────────────\n")
        print(colored("\nTrenutno nemate ni jednu nerealizovanu kartu.", "red", attrs = ["bold"])) 
        print("\n\n─────────────────────────────────────────────────────────────────────────────\n\n")
        return   
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
    print(colored("\nPREGLED SVIH NEREALIZOVANIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
    print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
    return
    
    
###################################################################################################   

# 8.1) IZABRANI CHECK-IN

def izabrana_opcija_check_in(korisnik):
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    global trenutni_ulogovan_korisnik
    num = 1
    Korisnik = korisnik
    listaKarata = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC"]]
    for karta in sveKarte:
        if sveKarte[karta]["kupac"] == korisnik:
            datum = sveKarte[karta]["datum_prodaje"]
            date1 = date(datum.year, datum.month, datum.day)
            listaKarata.append([num, sveKarte[karta]["broj_karte"], sveKarte[karta]["sifra_konkretnog_leta"], date1, sveKarte[karta]["status"], str(sveKarte[karta]["kupac"]["ime"] + " " + sveKarte[karta]["kupac"]["prezime"])])
            num += 1
    if len(listaKarata) == 1:
        print(colored("\n\nTrenutno nemate ni jednu kupljenu kartu.", "red", attrs = ["bold"]))            
        while (True):   
            print("\n\nDa li želite da izabere opciju: KUPOVINA KARATA?\n")
            print(colored("1) DA", "red"))
            print(colored("2) NE", "red"))
            print(colored("3) POVRATAK NA MENI\n\n", "red"))
            odgovor = str(input("Unesite redni broj opcije koju želite: "))
            if odgovor == "1":   
                izabrana_opcija_kupovina_karata(Korisnik)
                return
            elif odgovor == "2":
                print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                return
            elif odgovor == "3":
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                trenutno_prijavljen(trenutni_ulogovan_korisnik)
                return  
            else:
                print(colored("\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))                      
    print("\n\n───────────────────────────────────────────────────────────────────────────────────\n")
    print(colored("\nPREGLED SVIH KUPLJENIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print(tabulate(listaKarata, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
    print("\n\n───────────────────────────────────────────────────────────────────────────────────\n")
    while (True):
        opcijaNazad = str(input("\n\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
        if opcijaNazad == 'x':
            print("\n\n")
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return
        print("\n\n")
        ok = 1
        brojKarte = str(input("Unesite broj karte koju želite da čekirate: "))
        if brojKarte == "" or brojKarte is None:
            print(colored("\n\nGREŠKA: 'broj karte' je prazno. Unesite ponovo.\n\n", "light_red"))               
        for i in brojKarte:
            if ord(i) < 48 or ord(i) > 57:
                print(colored("\n\nGREŠKA: 'broj karte' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))    
                ok = 0
                break
        if ok == 0:
            continue
        if int(brojKarte) not in sveKarte:
            print(colored("\n\nGREŠKA: 'broj karte' ne postoji. Unesite ponovo.\n\n", "light_red"))               
            continue
        if sveKarte[int(brojKarte)]["kupac"] != korisnik:
            print(colored("\n\nGREŠKA: 'broj karte' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))               
            continue
        break
    izabrana_opcija_direktan_check_in(Korisnik, sveKarte[int(brojKarte)])
    return
    
    
# 8) DIREKTNI CHECK-IN
 
def izabrana_opcija_direktan_check_in(korisnik, karta):
    global povezani
    global trenutni_ulogovan_korisnik
    print("\n\n───────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("CHECK-IN LETA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    konkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    sviKorisnici = korisnici.ucitaj_korisnike_iz_fajla("svi_korisnici.txt", "|")  
    sifra = karta["sifra_konkretnog_leta"]
    if karta["sediste"] != "":
        print(colored("Karta je vec čekirana!\n\nAko želite da izmenite Vašu kartu, obratite nam se na mail: tacaairlines@gmail.com\nOčekujte odgovor u najkraćem mogućem roku!\n\n", "light_red"))                  
        print("───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
        return
    today = datetime.now() 
    granica = today + timedelta(hours = 48)
    if konkretniLetovi[karta["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"] < today:
        print("GREŠKA: Nije moguće uraditi check-in!\nOvaj let je već realizovan!\n\n")
        print("───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
        return
    if konkretniLetovi[karta["sifra_konkretnog_leta"]]["datum_i_vreme_polaska"] > granica:
        print("GREŠKA: Nije moguće uraditi check-in!\nCheck-in se može obaviti najranije 48h pre poletanja.\n\n")
        print("───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
        return
    opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
    if opcijaNazad == 'x':
        print("\n\n")
        trenutno_prijavljen(trenutni_ulogovan_korisnik)
        return
    print("\n\n")
    if povezani == 1:
        povezani = 0
        karta["kupac"] = korisnik
    registrovan = 0
    kupacPutuje = 0
    if len(karta["putnici"][0]) == 1:
        for key in karta["putnici"][0]:
            korisnickoIme = key
            break
        if karta["putnici"][0][korisnickoIme] == korisnik:
            kupacPutuje = 1
    else:
        if karta["kupac"]["ime"] == korisnik["ime"] and karta["kupac"]["prezime"] == korisnik["prezime"] and karta["kupac"]["telefon"] == korisnik["telefon"] and karta["kupac"]["email"] == korisnik["email"]:
            kupacPutuje = 2
    if "korisnicko_ime" in korisnik:
        registrovan = 1    
    korisnikPre = korisnik
    zauzetost = konkretniLetovi[int(sifra)]["zauzetost"]
    brSlobodnih = 0
    for i in range(0, len(zauzetost)):
        for j in range(0, len(zauzetost[i])):
            if zauzetost[i][j] is False:
                brSlobodnih += 1
    if brSlobodnih == 0:
        print(colored("GREŠKA: Nemoguće čekirati kartu! Sva sedišta u avionu su već zauzeta!\n\n", "light_red"))                  
        print("───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
        return
    konkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")         
    kupacKorisnicko = ""
    if registrovan == 1:
        kupacKorisnicko = karta["kupac"]["korisnicko_ime"]
    poruka = 0
    if karta["kupac"]["pasos"] is None or karta["kupac"]["pasos"] == "":
        print("Unesite sledeće podatke koji nedostaju za kupca (", end = "")
        print(colored("'", "light_red"), end = "")
        print(colored(karta["kupac"]["ime"], "light_red"), end = "")
        print(colored(" ", "light_red"), end = "")
        print(colored(karta["kupac"]["prezime"], "light_red"), end = "")
        print(colored("'", "light_red"), end = "")
        print("): \n")
        poruka = 1
        while (True):
            ok = 1
            pasos = str(input("Unesite broj pasoša: "))
            if pasos is None or pasos == "":
                print(colored("\n\nGREŠKA: 'broj pasoša' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                continue 
            for i in pasos:
                if ord(i) < 48 or ord(i) > 57:
                    print(colored("\n\nGREŠKA: 'broj pasoša' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                    ok = 0
                    break
            if ok == 0:
                continue    
            if len(pasos) != 9:
                print(colored("\n\nGREŠKA: 'broj pasoša' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                continue
            karta["kupac"]["pasos"] = pasos    
            korisnik["pasos"] = pasos
            if registrovan == 1:
                sviKorisnici[kupacKorisnicko]["pasos"] = pasos
            break
    if karta["kupac"]["drzavljanstvo"] is None or karta["kupac"]["drzavljanstvo"] == "":
        if poruka != 1:
            print("Unesite sledeće podatke koji nedostaju za kupca (", end = "")
            print(colored("'", "light_red"), end = "")
            print(colored(karta["kupac"]["ime"], "light_red"), end = "")
            print(colored(" ", "light_red"), end = "")
            print(colored(karta["kupac"]["prezime"], "light_red"), end = "")
            print(colored("'", "light_red"), end = "")
            print("): \n")
            poruka = 1
        while (True):
            ok = 1
            drzavljanstvo = str(input("Unesite državljanstvo: "))
            if drzavljanstvo is None or drzavljanstvo == "":
                print(colored("\n\nGREŠKA: 'državljanstvo' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                continue 
            for i in drzavljanstvo:
                if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                    print(colored("\n\nGREŠKA: 'državljanstvo' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))                  
                    ok = 0
                    break
            if ok == 0:
                continue    
            if len(drzavljanstvo) > 10:
                print(colored("\n\nGREŠKA: 'državljanstvo' ne može biti duže od 10 slova. Unesite ponovo.\n\n", "light_red"))                  
                continue
            karta["kupac"]["drzavljanstvo"] = drzavljanstvo
            korisnik["drzavljanstvo"] = drzavljanstvo
            if registrovan == 1:
                sviKorisnici[kupacKorisnicko]["drzavljanstvo"] = drzavljanstvo
            break
    if karta["kupac"]["pol"] is None or karta["kupac"]["pol"] == "":
        if poruka != 1:
            print("Unesite sledeće podatke koji nedostaju za kupca (", end = "")
            print(colored("'", "light_red"), end = "")
            print(colored(karta["kupac"]["ime"], "light_red"), end = "")
            print(colored(" ", "light_red"), end = "")
            print(colored(karta["kupac"]["prezime"], "light_red"), end = "")
            print(colored("'", "light_red"), end = "")
            print("): \n")
            poruka = 1
        while (True):
            ok = 1
            pol = str(input("Unesite pol: "))
            if pol is None or pol == "":
                print(colored("\n\nGREŠKA: 'pol' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                continue 
            for i in pol:
                if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                    print(colored("\n\nGREŠKA: 'pol' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))                  
                    ok = 0
                    break
            if ok == 0:
                continue    
            if len(pol) > 10:
                print(colored("\n\nGREŠKA: 'pol' ne može biti duže od 10 slova. Unesite ponovo.\n\n", "light_red"))                  
                continue
            karta["kupac"]["pol"] = pol
            korisnik["pol"] = pol
            if registrovan == 1:
                sviKorisnici[kupacKorisnicko]["pol"] = pol
            break   
    sveKarte[karta["broj_karte"]] = karta
    ocisti_file("sve_karte.txt")
    ocisti_file("svi_korisnici.txt")
    korisnici.sacuvaj_korisnike("svi_korisnici.txt", "|", sviKorisnici)
    karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")
    if registrovan == 1:
        for karta1 in sveKarte:
            if sveKarte[karta1]["kupac"] == korisnikPre: 
                sveKarte[karta1]["kupac"] = korisnik
            pos = 0
            for i in sveKarte[karta1]["putnici"]:
                if (len(i) == 1):  # registrovani putnik
                    for key in i:
                        korisnickoIme = key
                        break 
                    if i[korisnickoIme] == korisnikPre:
                        sveKarte[karta1]["putnici"][pos][korisnickoIme] = korisnik
                pos += 1
    ocisti_file("sve_karte.txt")
    ocisti_file("svi_korisnici.txt")
    korisnici.sacuvaj_korisnike("svi_korisnici.txt", "|", sviKorisnici)
    karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")  
    for i in range(0, len(karta["putnici"])):
        poruka = 0
        if kupacPutuje == 1:
            karta["putnici"][0][kupacKorisnicko] = korisnik
            sveKarte[karta["broj_karte"]] = karta
            ocisti_file("sve_karte.txt")
            karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")
            kupacPutuje = 0
            continue
        if kupacPutuje == 2:
            karta["putnici"][0] = korisnik
            sveKarte[karta["broj_karte"]] = karta
            ocisti_file("sve_karte.txt")
            karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")
            kupacPutuje = 0
            continue
        if (len(karta["putnici"][i]) == 1):  # registrovani saputnik
            for key in karta["putnici"][i]:
                korisnickoIme = key
                break
            putnikPre = karta["putnici"][i][korisnickoIme]
            if karta["putnici"][i][korisnickoIme]["pasos"] is None or karta["putnici"][i][korisnickoIme]["pasos"] == "":
                print("Unesite sledeće podatke koji nedostaju za putnika broj ", end = "")
                print(str(i + 1), end = "")
                print(" (", end = "")
                print(colored("'", "light_red"), end = "")
                print(colored(karta["putnici"][i][korisnickoIme]["ime"], "light_red"), end = "")
                print(colored(" ", "light_red"), end = "")
                print(colored(karta["putnici"][i][korisnickoIme]["prezime"], "light_red"), end = "")
                print(colored("'", "light_red"), end = "")
                print("): \n")
                poruka = 1
                while (True):
                    ok = 1
                    pasos = str(input("Unesite broj pasoša: "))
                    if pasos is None or pasos == "":
                        print(colored("\n\nGREŠKA: 'broj pasoša' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        continue 
                    for z in pasos:
                        if ord(z) < 48 or ord(z) > 57:
                            print(colored("\n\nGREŠKA: 'broj pasoša' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                            ok = 0
                            break
                    if ok == 0:
                        continue    
                    if len(pasos) != 9:
                        print(colored("\n\nGREŠKA: 'broj pasoša' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                        continue
                    karta["putnici"][i][korisnickoIme]["pasos"] = pasos
                    sviKorisnici[korisnickoIme]["pasos"] = pasos
                    break  
            if karta["putnici"][i][korisnickoIme]["drzavljanstvo"] is None or karta["putnici"][i][korisnickoIme]["drzavljanstvo"] == "":
                if poruka != 1:
                    print("Unesite sledeće podatke koji nedostaju za putnika broj ", end = "")
                    print(str(i + 1), end = "")
                    print(" (", end = "")
                    print(colored("'", "light_red"), end = "")
                    print(colored(karta["putnici"][i][korisnickoIme]["ime"], "light_red"), end = "")
                    print(colored(" ", "light_red"), end = "")
                    print(colored(karta["putnici"][i][korisnickoIme]["prezime"], "light_red"), end = "")
                    print(colored("'", "light_red"), end = "")
                    print("): \n")
                    poruka = 1
                while (True):
                    ok = 1
                    drzavljanstvo = str(input("Unesite državljanstvo: "))
                    if drzavljanstvo is None or drzavljanstvo == "":
                        print(colored("\n\nGREŠKA: 'državljanstvo' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        continue 
                    for z in drzavljanstvo:
                        if ord(z.lower()) < 97 or ord(z.lower()) > 122:
                            print(colored("\n\nGREŠKA: 'državljanstvo' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))                  
                            ok = 0
                            break
                    if ok == 0:
                        continue    
                    if len(drzavljanstvo) > 10:
                        print(colored("\n\nGREŠKA: 'državljanstvo' ne može biti duže od 10 slova. Unesite ponovo.\n\n", "light_red"))                  
                        continue
                    karta["putnici"][i][korisnickoIme]["drzavljanstvo"] = drzavljanstvo
                    sviKorisnici[korisnickoIme]["drzavljanstvo"] = drzavljanstvo
                    break 
            if karta["putnici"][i][korisnickoIme]["pol"] is None or karta["putnici"][i][korisnickoIme]["pol"] == "":
                if poruka != 1:
                    print("Unesite sledeće podatke koji nedostaju za putnika broj ", end = "")
                    print(str(i + 1), end = "")
                    print(" (", end = "")
                    print(colored("'", "light_red"), end = "")
                    print(colored(karta["putnici"][i][korisnickoIme]["ime"], "light_red"), end = "")
                    print(colored(" ", "light_red"), end = "")
                    print(colored(karta["putnici"][i][korisnickoIme]["prezime"], "light_red"), end = "")
                    print(colored("'", "light_red"), end = "")
                    print("): \n")
                    poruka = 1
                while (True):
                    ok = 1
                    pol = str(input("Unesite pol: "))
                    if pol is None or pol == "":
                        print(colored("\n\nGREŠKA: 'pol' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        continue 
                    for z in pol:
                        if ord(z.lower()) < 97 or ord(z.lower()) > 122:
                            print(colored("\n\nGREŠKA: 'pol' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))                  
                            ok = 0
                            break
                    if ok == 0:
                        continue    
                    if len(pol) > 10:
                        print(colored("\n\nGREŠKA: 'pol' ne može biti duže od 10 slova. Unesite ponovo.\n\n", "light_red"))                  
                        continue
                    karta["putnici"][i][korisnickoIme]["pol"] = pol
                    sviKorisnici[korisnickoIme]["pol"] = pol
                    break 
            for karta2 in sveKarte:
                if sveKarte[karta2]["kupac"] == putnikPre:
                    sveKarte[karta2]["kupac"] = sviKorisnici[korisnickoIme]
                for j in range(0, len(sveKarte[karta2]["putnici"])):
                    if (len(sveKarte[karta2]["putnici"][j]) == 1):  # registrovani putnik
                        for key in sveKarte[karta2]["putnici"][j]:
                            korisnickoIme2 = key
                            break 
                        if sveKarte[karta2]["putnici"][j][korisnickoIme2] == korisnikPre:
                            sveKarte[karta2]["putnici"][j][korisnickoIme2] = sviKorisnici[korisnickoIme]
        else:
            print("\nUnesite sledeće podatke koji nedostaju za putnika broj ", end = "")
            print(str(i + 1), end = "")
            print(" (", end = "")
            print(colored("'", "light_red"), end = "")
            print(colored(karta["putnici"][i]["ime"], "light_red"), end = "")
            print(colored(" ", "light_red"), end = "")
            print(colored(karta["putnici"][i]["prezime"], "light_red"), end = "")
            print(colored("'", "light_red"), end = "")
            print("): \n")
            while (True):  # neregistrovani saputnik
                ok = 1
                pasos = str(input("Unesite broj pasoša: "))
                if pasos is None or pasos == "":
                    print(colored("\n\nGREŠKA: 'broj pasoša' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                    continue 
                for z in pasos:
                    if ord(z) < 48 or ord(z) > 57:
                        print(colored("\n\nGREŠKA: 'broj pasoša' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                        ok = 0
                        break
                if ok == 0:
                    continue    
                if len(pasos) != 9:
                    print(colored("\n\nGREŠKA: 'broj pasoša' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                    continue
                karta["putnici"][i]["pasos"] = pasos
                break
            while (True):
                ok = 1
                drzavljanstvo = str(input("Unesite državljanstvo: "))
                if drzavljanstvo is None or drzavljanstvo == "":
                    print(colored("\n\nGREŠKA: 'državljanstvo' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                    continue 
                if len(drzavljanstvo) > 10:
                    print(colored("\n\nGREŠKA: 'državljanstvo' ne sme biti duže od 10 slova. Unesite ponovo.\n\n", "light_red"))                  
                    continue
                for z in drzavljanstvo:
                    if ord(z.lower()) < 97 or ord(z.lower()) > 122:
                        print(colored("\n\nGREŠKA: 'državljanstvo' nijee dobro definisano. Unesite ponovo.\n\n", "light_red"))                  
                        ok = 0
                        break
                if ok == 0:
                    continue    
                karta["putnici"][i]["drzavljanstvo"] = drzavljanstvo
                break
            while (True):
                ok = 1
                pol = str(input("Unesite pol: "))
                if pol is None or pol == "":
                    print(colored("\n\nGREŠKA: 'pol' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                    continue
                for z in pol:
                    if ord(z.lower()) < 97 or ord(z.lower()) > 122:
                        print(colored("\n\nGREŠKA: 'pol' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))                  
                        ok = 0
                        break
                if ok == 0:
                    continue    
                if len(pol) > 10:
                    print(colored("\n\nGREŠKA: 'pol' ne sme biti duži od 10 slova. Unesite ponovo.\n\n", "light_red"))                  
                    continue
                karta["putnici"][i]["pol"] = pol   
                break  
            print("\n")
    zauzetost = konkretniLetovi[int(sifra)]["zauzetost"]    
    redovi = len(zauzetost) #4
    kolone = len(zauzetost[0]) #6
    lista = []
    for i in range(0, redovi):
        newLista = []
        s = "RED "
        s += str(i + 1)
        s += ": "
        newLista.append(s)
        for j in range(0, kolone):
            s = ""
            if zauzetost[i][j] == True:
                s += "x "
                newLista.append(s)
            else:
                s += str(j + 1) + " "    
                newLista.append(s)     
        lista.append(newLista)
    print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
    print(colored("\nPREGLED SEDIŠTA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print(tabulate(lista, tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")            
    print(colored("Zauzeta sedišta su obeležena sa 'x'.\nMolimo Vas da izaberite jedno od slobodnih sedišta.\n", "yellow", attrs = ["bold"]), "\n")
    while (True):
        while (True):
            ok = 1
            red = str(input("Unesite red sedišta: "))
            if red is None or red == "":
                print(colored("\n\nGREŠKA: 'red sedišta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                continue
            for i in red:
                if ord(i) < 48 or ord(i) > 57:
                    print(colored("\n\nGREŠKA: 'red sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                    ok = 0
                    break
            if ok == 0:
                continue
            if int(red) < 1 or int(red) > redovi:
                print(colored("\n\nGREŠKA: 'red sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                continue
            break
        while (True):    
            broj = str(input("Unesite broj sedišta u odabranom " + red + ". redu: "))
            if broj is None or broj == "":
                print(colored("\n\nGREŠKA: 'broj sedišta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                continue
            ok = 1
            for i in broj:
                if ord(i) < 48 or ord(i) > 57:
                    print(colored("\n\nGREŠKA: 'broj sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))                  
                    ok = 0
                    break
            if ok == 0:
                continue
            if int(broj) < 1 or int(broj) > kolone:
                print(colored("\n\nGREŠKA: 'broj sedišta' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))
                continue
            break
        if zauzetost[int(red) - 1][int(broj) - 1] == True:
            print(colored("\n\nGREŠKA: ovo sedište je već zauzeto! Unesite ponovo.\n\n", "light_red"))   
            continue
        else:
            zauzetost[int(red) - 1][int(broj) - 1] = True
            konkretniLetovi[int(sifra)]["zauzetost"] = zauzetost
            karta["sediste"] = str(red) + "," + str(broj)
            karta["status"] = "realizovana_karta"
            break
    sveKarte[karta["broj_karte"]] = karta
    ocisti_file("svi_konkretni_letovi.txt")
    ocisti_file("svi_korisnici.txt")
    ocisti_file("sve_karte.txt")
    karte.sacuvaj_karte(sveKarte, "sve_karte.txt", "|")
    korisnici.sacuvaj_korisnike("svi_korisnici.txt", "|", sviKorisnici)
    konkretni_letovi.sacuvaj_kokretan_let("svi_konkretni_letovi.txt", "|", konkretniLetovi)
    poruka = "Čekiranje karte USPEŠNO!"
    s = "┌───"
    g = "└───"
    for i in range(0, len(poruka) - 1):
        s += "─"
        g += "─"
    s += "┐"    
    g += "┘"
    print("\n\n")
    print(colored(s, "green"))
    print(colored("│ ", "green"), end = "")
    print(colored("Čekiranje karte USPEŠNO!", "green", attrs = ["bold"]), end = "")
    print(colored(" │", "green")) 
    print(colored(g, "green"), "\n\n")
    listaPovezanihLetova = letovi.povezani_letovi(sviLetovi, konkretniLetovi, konkretniLetovi[int(sifra)])
    listaKarata = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS"]]
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    num = 1
    for karta2 in sveKarte:
        if sveKarte[karta2]["status"] == "realizovana_karta":
            continue
        if "korisnicko_ime" not in sveKarte[karta2]["kupac"]:
            if sveKarte[karta2]["kupac"]["ime"] == korisnik["ime"] and sveKarte[karta2]["kupac"]["prezime"] == korisnik["prezime"] and sveKarte[karta2]["kupac"]["telefon"] == korisnik["telefon"] and sveKarte[karta2]["kupac"]["email"] == korisnik["email"]:
                ok = 0  
                for let in listaPovezanihLetova:
                    if let[0] == sveKarte[karta2]["sifra_konkretnog_leta"]:
                        ok = 1
                        break
                if ok == 0:
                    continue
                else:    
                    datum = sveKarte[karta2]["datum_prodaje"]
                    date1 = date(datum.year, datum.month, datum.day)
                    listaKarata.append([num, sveKarte[karta2]["broj_karte"], sveKarte[karta2]["sifra_konkretnog_leta"], date1, sveKarte[karta2]["status"]])
                    num += 1    
        if sveKarte[karta2]["kupac"] == korisnik:   
            ok = 0  
            for let in listaPovezanihLetova:
                if let[0] == sveKarte[karta2]["sifra_konkretnog_leta"]:
                    ok = 1
                    break
            if ok == 0:
                continue
            else:    
                datum = sveKarte[karta2]["datum_prodaje"]
                date1 = date(datum.year, datum.month, datum.day)
                listaKarata.append([num, sveKarte[karta2]["broj_karte"], sveKarte[karta2]["sifra_konkretnog_leta"], date1, sveKarte[karta2]["status"]])
                num += 1
    if len(listaKarata) == 1:
        return
    while (True):
        print(colored("\nDa li želite da čekirate i kartu za povezani let?\n\n", "yellow"))
        print(colored("1) DA", "red"))
        print(colored("2) NE", "red"))
        print(colored("3) POVRATAK NA MENI\n\n", "red"))
        while (True):
            option = str(input("Unesite redni broj opcije koju želite: "))
            if option == "1":
                num = 1
                listaKarata = [["REDNI BR.", "BROJ KARTE", "ŠIFRA LETA", "DATUM PRODAJE", "STATUS", "KUPAC"]]
                for karta2 in sveKarte:
                    if sveKarte[karta2]["status"] == "realizovana_karta":
                        continue;
                    if sveKarte[karta2]["kupac"] == korisnik:
                        datum = sveKarte[karta2]["datum_prodaje"]
                        date1 = date(datum.year, datum.month, datum.day)
                        listaKarata.append([num, sveKarte[karta2]["broj_karte"], sveKarte[karta2]["sifra_konkretnog_leta"], date1, sveKarte[karta2]["status"], str(sveKarte[karta2]["kupac"]["ime"] + " " + sveKarte[karta2]["kupac"]["prezime"])])
                        num += 1
                        continue
                    if "korisnicko_ime" not in sveKarte[karta2]["kupac"]:
                        if sveKarte[karta2]["kupac"]["ime"] == korisnik["ime"] and sveKarte[karta2]["kupac"]["prezime"] == korisnik["prezime"] and sveKarte[karta2]["kupac"]["telefon"] == korisnik["telefon"] and sveKarte[karta2]["kupac"]["email"] == korisnik["email"]:  
                            datum = sveKarte[karta2]["datum_prodaje"]
                            date1 = date(datum.year, datum.month, datum.day)
                            listaKarata.append([num, sveKarte[karta2]["broj_karte"], sveKarte[karta2]["sifra_konkretnog_leta"], date1, sveKarte[karta2]["status"]])
                            num += 1        
                print("\n\n───────────────────────────────────────────────────────────────────────────────────\n")
                print(colored("\nPREGLED SVIH KUPLJENIH NEREALIZOVANIH KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
                print(colored("\nKUPAC: ", "yellow"), end = "")
                str1 = str(karta["kupac"]["ime"])
                str2 = str(karta["kupac"]["prezime"])
                print(colored("'", "yellow", attrs = ["bold"]), end = "")
                print(colored(str1, "yellow", attrs = ["bold"]), end = " ")
                print(colored(str2, "yellow", attrs = ["bold"]), end = "")
                print(colored("'", "yellow", attrs = ["bold"]), "\n\n")
                print(tabulate(listaKarata, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                print("\n\n───────────────────────────────────────────────────────────────────────────────────\n\n")
                listaPovezanihLetova = letovi.povezani_letovi(sviLetovi, konkretniLetovi, konkretniLetovi[int(sifra)])
                listaKarata = []
                sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
                Korisnik = korisnik
                for kartaa in sveKarte:
                    if sveKarte[karta2]["status"] == "realizovana_karta":
                        continue;
                    if "korisnicko_ime" not in sveKarte[karta2]["kupac"]:
                        if sveKarte[karta2]["kupac"]["ime"] == korisnik["ime"] and sveKarte[karta2]["kupac"]["prezime"] == korisnik["prezime"] and sveKarte[karta2]["kupac"]["telefon"] == korisnik["telefon"] and sveKarte[karta2]["kupac"]["email"] == korisnik["email"]:
                            ok = 0  
                            for let in listaPovezanihLetova:
                                if let[0] == sveKarte[karta2]["sifra_konkretnog_leta"]:
                                    ok = 1
                                    break
                            if ok == 0:
                                continue
                            else:    
                                listaKarata.append(sveKarte[kartaa])
                                num += 1
                        continue        
                    if sveKarte[kartaa]["kupac"] == korisnik:   
                        ok = 0  
                        for let in listaPovezanihLetova:
                            if let[0] == sveKarte[kartaa]["sifra_konkretnog_leta"]:
                                ok = 1
                                break
                        if ok == 0:
                            continue
                        else:    
                            listaKarata.append(sveKarte[kartaa])
                            num += 1
                if len(listaKarata) == 0:
                    print(colored("\n\nNe postoji ni jedna kupljena karta za povezane letove.", "light_red", attrs = ["bold"]), "\n\n")
                    while (True):   
                        if (trenutni_ulogovan_korisnik["uloga"] == "prodavac"):
                            print("\n\nDa li želite da izaberete opciju: PRODAJA KARATA?\n")
                        if (trenutni_ulogovan_korisnik["uloga"] == "korisnik"):      
                            print("\n\nDa li želite da izaberete opciju: KUPOVINA KARATA?\n")
                        print(colored("1) DA", "red"))
                        print(colored("2) NE", "red"))
                        print(colored("3) POVRATAK NA MENI\n\n", "red"))
                        odgovor = str(input("Unesite redni broj opcije koju želite: "))
                        if odgovor == "1":  
                            if (trenutni_ulogovan_korisnik["uloga"] == "prodavac"):
                                izabrana_opcija_prodaja_karata(trenutni_ulogovan_korisnik)
                            if (trenutni_ulogovan_korisnik["uloga"] == "korisnik"):
                                izabrana_opcija_kupovina_karata(trenutni_ulogovan_korisnik)
                            return
                        elif odgovor == "2":
                            print("\n")
                            #print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                            return
                        elif odgovor == "3":
                            print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                            print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                            print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                            trenutno_prijavljen(trenutni_ulogovan_korisnik)
                            return 
                        else:
                            print(colored("\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))                      
                            continue
                jednom = 0
                while (True):
                    if jednom == 1:
                        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
                        if opcijaNazad == 'x':
                            print("\n\n")
                            trenutno_prijavljen(trenutni_ulogovan_korisnik)
                            return
                        print("\n\n")
                    povezaniBroj = str(input("\nUnesite broj karte Vašeg povezanog leta: "))
                    if povezaniBroj is None or povezaniBroj == "":
                        print(colored("\n\nGREŠKA: 'broj karte' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                        jednom = 1
                        continue
                    for i in povezaniBroj:
                        if ord(i) < 48 or ord(i) > 57:
                            print(colored("\n\nGREŠKA: uneseni 'broj karte' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))       
                            jednom = 1
                            continue
                    ok = 0
                    for kartaa in listaKarata:
                        if kartaa["broj_karte"] == int(povezaniBroj):
                            ok = 1
                            if kartaa["sediste"] != "" or kartaa["status"] == "realizovana_karta":
                                print(colored("\n\n\nGREŠKA: ova karta je već čekirana! Unesite ponovo.\n\n", "light_red"))    
                                ok = 2
                                break  
                    if ok == 2:
                        jednom = 1
                        continue
                    if ok == 0:
                        print(colored("\n\n\nGREŠKA: uneseni 'broj karte' nije dobro definisan. Unesite ponovo.\n\n", "light_red"))    
                        jednom = 1
                        continue
                    else:
                        if registrovan == 1:
                            povezani = 1
                            izabrana_opcija_direktan_check_in(sviKorisnici[kupacKorisnicko], sveKarte[int(povezaniBroj)])
                            return 
                        else:
                            povezani = 1
                            izabrana_opcija_direktan_check_in(karta["kupac"], sveKarte[int(povezaniBroj)])
                            return         
            elif option == "2":
                print("\n\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                return
            elif option == "3":
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                trenutno_prijavljen(trenutni_ulogovan_korisnik)
                return 
            else: 
                print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))    
                continue
    
   
###################################################################################################   
 
# 7.1) KUPOVINA KARATA ZA POVEZANE LETOVE

def izabrana_opcija_povezani_letovi(korisnik, listaPovezanihLetova):
    global trenutni_ulogovan_korisnik
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("POVEZANI LETOVI\n", "yellow", attrs = ["underline", "bold"]), "\n")
    opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
    if opcijaNazad == 'x':
        print("\n\n")
        trenutno_prijavljen(trenutni_ulogovan_korisnik)
        return
    print("\n\n")
    Korisnik = korisnik
    listaPovezanihLetovaa = listaPovezanihLetova
    while (True):
        sifra = str(input("Unesite šifru konkretnog leta: "))  
        if sifra is None or sifra == "":
            print(colored("\n\nGREŠKA: 'šifra konkretnog leta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
            continue
        for i in sifra:
            ok = 1
            if ord(i) < 48 or ord(i) > 57:
                print(colored("\n\n\nGREŠKA: 'šifra konkretnog leta' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                ok = 0
                break
        if ok == 0:
            continue
        ok = 0
        for i in listaPovezanihLetova:
            if i[0] == int(sifra):
                ok = 1
        if ok == 0:
            print(colored("\n\n\nGREŠKA: unesena 'šifra konkretnog leta' nije u datim povezanim letovima. Unesite ponovo.\n", "light_red"))
            continue
        else:
            break
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")            
    slobodnaMesta = letovi.matrica_zauzetosti(sviKonkretniLetovi[int(sifra)])
    putnici = []
    brojSlobodnih = 0
    brojRedova = len(slobodnaMesta)
    for i in range(0, brojRedova):
        for j in slobodnaMesta[i]:
            if j == False:
                brojSlobodnih += 1
    if brojSlobodnih == 0:
        print(colored("\n\n\nNažalost, trenutno nema slobodnih mesta za ovaj let.\n", "light_red"))        
        while (True):
            print("\nDa li želite da nastavite sa kupovinom karata?\n")
            print(colored("1) DA", "red"))
            print(colored("2) NE", "red"))
            print(colored("3) POVRATAK NA MENI\n\n", "red"))
            odgovor = str(input("Unesite redni broj opcije koju želite: "))
            if odgovor == "1":   
                izabrana_opcija_povezani_letovi(Korisnik, listaPovezanihLetovaa)
                return
            elif odgovor == "2":
                print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
                return
            elif odgovor == "3":
                print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                trenutno_prijavljen(trenutni_ulogovan_korisnik)
                return  
            else:
                print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red")) 
                continue          
    else:
        print(colored("\n\n\nBroj ukupnih slobodnih mesta na ovom letu: ", "green"), colored(brojSlobodnih, "green"), colored("\n\n", "green"))        
        if "korisnicko_ime" in Korisnik:
            putnici.append({Korisnik["korisnicko_ime"]: Korisnik})
        else:
            putnici.append(Korisnik)        
        while (True):
            print(colored("\n\nDa li želite da dodate saputnika?\n", "light_grey"))
            print(colored("1) DA", "red"))
            print(colored("2) NE\n\n", "red"))
            opcija2 = str(input("Unesite redni broj opcije koju želite: "))
            if opcija2 == "1":
                print(colored("\n\nUnesite sledeće podatke saputnika:\n", "light_grey"))
                imeOsobe = str(input("IME: "))
                prezimeOsobe = str(input("PREZIME: "))
                putnici.append({"ime": imeOsobe, "prezime": prezimeOsobe, "pasos": "", "drzavljanstvo": "", "pol": ""})
                continue
            elif opcija2 == "2":
                break
            else:
                print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))
        # dodao sve putnike, potvrda kupovine
        today = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
        try:
            if trenutni_ulogovan_korisnik["uloga"] == "prodavac":
                (kartaNew, sveKarteNew) = karte.kupovina_karte(sveKarte, sviKonkretniLetovi, int(sifra), putnici, slobodnaMesta, Korisnik, prodavac = trenutni_ulogovan_korisnik, datum_prodaje = today) 
            else:    
                (kartaNew, sveKarteNew) = karte.kupovina_karte(sveKarte, sviKonkretniLetovi, int(sifra), putnici, slobodnaMesta, Korisnik, prodavac = "", datum_prodaje = today)  
            kartaNew["sediste"] = ""
            sveKarteNew[kartaNew["broj_karte"]]["sediste"] = ""
            ocisti_file("sve_karte.txt")    
            karte.sacuvaj_karte(sveKarteNew, "sve_karte.txt", "|")
            poruka = "Kupovina karte za povezani let USPEŠNA!"
            s = "┌───"
            g = "└───"
            for i in range(0, len(poruka) - 1):
                s += "─"
                g += "─"
            s += "┐"    
            g += "┘"
            print("\n\n")
            print(colored(s, "green"))
            print(colored("│ ", "green"), end = "")
            print(colored("Kupovina karte za povezani let USPEŠNA!", "green", attrs = ["bold"]), end = "")
            print(colored(" │", "green")) 
            print(colored(g, "green"), "\n\n")
            print("\n")
            print(colored("NAPOMENA: ", "yellow", attrs = ["bold"]), end = "")
            print(colored("predlažemo Vam da odmah uradite check-in, kako biste što pre mogli izabrati svoje željeno sedište.\n", "yellow"))
            print(colored("VAŽNO OBAVEŠTENJE: ", "yellow", attrs = ["bold"]), end = "")       
            print(colored("check-in se može obaviti najkasnije 48h pre poletanja.", "yellow"))
            print(colored("Ukoliko ne čekirate Vašu kartu 48h pre poletanja, Vaša karta će postati nevažeća,\nte će Vam biti onemogućen ulazak u avion i let istim.", "yellow"))
            print(colored("\nTaca Airlines® ne snosi nikakve novčane naknade, te je Vaša dužnost da uredno čekirate kartu na vreme.\n\n", "yellow"))
            print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
            while (True):
                print("\nDa li želite odmah da čekirate Vašu upravo kupljenu kartu?\n")
                print(colored("1) DA", "red"))
                print(colored("2) NE", "red"))
                print(colored("3) POVRATAK NA MENI\n\n", "red"))
                odgovor = str(input("Unesite redni broj opcije koju želite: "))
                if odgovor == "1":   
                    izabrana_opcija_direktan_check_in(Korisnik, kartaNew)
                    break
                elif odgovor == "2":
                    break
                elif odgovor == "3":
                    print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                    print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                    print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                    trenutno_prijavljen(trenutni_ulogovan_korisnik)
                    return 
                else: 
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red")) 
                    continue     
            print(colored("\n\nDa li želite da vidite karte za letove povezane sa prethodnim letom?\n\n", "yellow"))
            print(colored("1) DA", "red"))
            print(colored("2) NE", "red"))
            print(colored("3) POVRATAK NA MENI\n\n", "red"))
            while (True):
                option = str(input("Unesite redni broj opcije koju želite: "))
                if option == "1":
                    listaPovezanihLetovaa = letovi.povezani_letovi(sviLetovi, sviKonkretniLetovi, sviKonkretniLetovi[int(sifra)])
                    if len(listaPovezanihLetovaa) == 1:
                        print(colored("\n\n\nNažalost, trenutno ne postoji ni jedan povezani let za Vaš let.\nVraćamo Vas na glavni meni.\n", "light_red", attrs = ["bold"]))
                        print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                        return
                    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                    print(colored("\nPREGLED SVIH POVEZANIH KONKRETNIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
                    print(tabulate(listaPovezanihLetovaa, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                    izabrana_opcija_povezani_letovi(Korisnik, listaPovezanihLetovaa)     
                    return
                elif option == "2":
                    print("\n\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                    return
                elif odgovor == "3":
                    print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                    print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                    print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                    trenutno_prijavljen(trenutni_ulogovan_korisnik)
                    return 
                else: 
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))         
        except Exception as greska1:
            greska = colored(greska1, "light_red")
            print("\n\n\n", greska, "\n\n")   
            izabrana_opcija_povezani_letovi(Korisnik, listaPovezanihLetovaa)
            return

        
# 7) KUPOVINA KARATA

def izabrana_opcija_kupovina_karata(korisnik):
    Korisnik = korisnik
    global trenutni_ulogovan_korisnik
    print("\n\n──────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("KUPOVINA KARATA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print(colored("Molimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
    print(colored("1) PREGLED SVIH KONKRETNIH LETOVA", "red"))
    print(colored("2) DIREKTNI UNOS ŠIFRE LETA", "red"))
    print(colored("3) POVRATAK NA MENI\n\n", "red"))
    option = str(input("Unesite redni broj opcije koju želite: "))
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    sveKarte = karte.ucitaj_karte_iz_fajla("sve_karte.txt", "|")
    if option == "1":
        lista = konkretni_letovi.pregled_svih_konkretnih_letova(sviLetovi, sviKonkretniLetovi)
        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
        print(colored("\nPREGLED SVIH KONKRETNIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n")
        print(tabulate(lista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
    if option == "2" or option == "1":
        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
        sifra = str(input("Unesite šifru konkretnog leta: "))
        if sifra is None or sifra == "":
            print(colored("\n\nGREŠKA: 'šifra konkretnog leta' je prazno. Unesite ponovo.\n\n", "light_red"))                  
            izabrana_opcija_kupovina_karata(Korisnik)
            return
        for i in sifra:
            if ord(i) < 48 or ord(i) > 57:
                print(colored("\n\n\nGREŠKA: 'šifra konkretnog leta' nije dobro definisana. Unesite ponovo.\n", "light_red"))
                izabrana_opcija_kupovina_karata(Korisnik)   
                return 
        if int(sifra) not in sviKonkretniLetovi:
            print(colored("\n\n\nGREŠKA: 'šifra konkretnog leta' ne postoji. Unesite ponovo.\n", "light_red"))
            izabrana_opcija_kupovina_karata(Korisnik)
            return
        slobodnaMesta = letovi.matrica_zauzetosti(sviKonkretniLetovi[int(sifra)])
        putnici = []
        brojSlobodnih = 0
        brojRedova = len(slobodnaMesta)
        for i in range(0, brojRedova):
            for j in slobodnaMesta[i]:
                if j == False:
                    brojSlobodnih += 1
        if brojSlobodnih == 0:
            print(colored("\n\n\nNažalost, trenutno nema slobodnih mesta za ovaj let.\n", "light_red", attrs = ["bold"]))  
            print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")      
            print(colored("\nDa li želite da nastavite sa kupovinom karata?\n", "yellow"))
            while (True):
                print(colored("\nMolimo Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
                print(colored("1) NASTAVAK KUPOVINE KARATA", "red"))
                print(colored("2) POVRATAK NA MENI\n\n", "red"))
                odgovor = str(input("Unesite redni broj opcije koju želite: "))
                if odgovor == "1":   
                    izabrana_opcija_kupovina_karata(Korisnik)
                    return
                elif odgovor == "2":
                    print("\n\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                    return
                else:
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))           
        else:
            print(colored("\n\n\nBroj ukupnih slobodnih mesta na ovom letu:", "green"), colored(brojSlobodnih, "green"), colored("\n\n\n", "green"))        
            while (True):   
                print(colored("Molim Vas izaberite jednu od sledećih opcija:\n", "light_grey"))
                print(colored("1) KUPUJEM KARTU ZA SEBE", "red"))
                print(colored("2) KUPUJEM KARTU ZA DRUGU OSOBU", "red"))
                print(colored("3) POVRATAK NA MENI\n\n", "red"))
                zaKogaKarta = str(input("Unesite redni broj opcije koju želite: "))
                if zaKogaKarta == "1":
                    print(colored("\n\nPodaci o korisniku uspešno preuzeti.\n\n", "green", attrs = ["bold"]))
                    newDict = {Korisnik["korisnicko_ime"]: Korisnik}
                    putnici.append(newDict)
                    break
                elif zaKogaKarta == "2":
                    print(colored("\n\nUnesite sledeće podatke za osobu za koju kupujete kartu:\n", "light_grey"))
                    while (True):
                        ok = 1
                        imeOsobe = str(input("IME: "))
                        if imeOsobe is None or imeOsobe == "":
                            print(colored("\n\nGREŠKA: 'ime osobe' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in imeOsobe:
                            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                                print(colored("\n\nGREŠKA: 'ime osobe' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(imeOsobe) > 15:
                            print(colored("\n\nGREŠKA: 'ime osobe' ne može biti duže od 15 slova. Unesite ponovo.\n\n", "light_red"))            
                            continue
                        prezimeOsobe = str(input("PREZIME: "))
                        if prezimeOsobe is None or prezimeOsobe == "":
                            print(colored("\n\nGREŠKA: 'prezime osobe' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in prezimeOsobe:
                            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                                print(colored("\n\nGREŠKA: 'prezime osobe' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(prezimeOsobe) > 20:
                            print(colored("\n\nGREŠKA: 'prezime osobe' ne može biti duže od 20 slova. Unesite ponovo.\n\n", "light_red"))
                            continue
                        break
                    putnici.append({"ime": imeOsobe, "prezime": prezimeOsobe, "pasos": "", "drzavljanstvo": "", "pol": ""})
                    print("\n")
                    break
                elif zaKogaKarta == "3":
                    print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                    print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                    print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                    trenutno_prijavljen(trenutni_ulogovan_korisnik)
                    return  
                else:
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n\n", "light_red"))          
            while (True):
                print(colored("Da li želite da dodate saputnika?:\n", "light_grey"))
                print(colored("1) DA", "red"))
                print(colored("2) NE\n\n", "red"))
                opcija2 = str(input("Unesite redni broj opcije koju želite: "))
                if opcija2 == "1":
                    print(colored("\n\nUnesite sledeće podatke saputnika:\n", "light_grey"))
                    while (True):
                        ok = 1
                        imeOsobe = str(input("IME: "))
                        if imeOsobe is None or imeOsobe == "":
                            print(colored("\n\nGREŠKA: 'ime osobe' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in imeOsobe:
                            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                                print(colored("\n\nGREŠKA: 'ime osobe' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(imeOsobe) > 15:
                            print(colored("\n\nGREŠKA: 'ime osobe' ne može biti duže od 15 slova. Unesite ponovo.\n\n", "light_red"))            
                            continue
                        prezimeOsobe = str(input("PREZIME: "))
                        if prezimeOsobe is None or prezimeOsobe == "":
                            print(colored("\n\nGREŠKA: 'prezime osobe' je prazno. Unesite ponovo.\n\n", "light_red"))                  
                            continue
                        for i in prezimeOsobe:
                            if ord(i.lower()) < 97 or ord(i.lower()) > 122:
                                print(colored("\n\nGREŠKA: 'prezime osobe' nije dobro definisano. Unesite ponovo.\n\n", "light_red"))
                                ok = 0
                                break
                        if ok == 0:
                            continue
                        if len(prezimeOsobe) > 20:
                            print(colored("\n\nGREŠKA: 'prezime osobe' ne može biti duže od 20 slova. Unesite ponovo.\n\n", "light_red"))
                            continue
                        break
                    putnici.append({"ime": imeOsobe, "prezime": prezimeOsobe, "pasos": "", "drzavljanstvo": "", "pol": ""})
                    print("\n")
                    continue
                elif opcija2 == "2":
                    break
                else:
                    print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))
            # dodao sve putnike, potvrda kupovine
            today = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
            try:
                (kartaNew, sveKarteNew) = karte.kupovina_karte(sveKarte, sviKonkretniLetovi, int(sifra), putnici, slobodnaMesta, Korisnik, prodavac = "", datum_prodaje = today)  
                kartaNew["sediste"] = ""
                sveKarteNew[kartaNew["broj_karte"]]["sediste"] = ""
                ocisti_file("sve_karte.txt")    
                karte.sacuvaj_karte(sveKarteNew, "sve_karte.txt", "|")
                poruka = "Kupovina karte USPEŠNA!"
                s = "┌───"
                g = "└───"
                for i in range(0, len(poruka) - 1):
                    s += "─"
                    g += "─"
                s += "┐"    
                g += "┘"
                print("\n\n")
                print(colored(s, "green"))
                print(colored("│ ", "green"), end = "")
                print(colored("Kupovina karte USPEŠNA!", "green", attrs = ["bold"]), end = "")
                print(colored(" │", "green")) 
                print(colored(g, "green"), "\n\n")
                print("\n")
                print(colored("NAPOMENA: ", "yellow", attrs = ["bold"]), end = "")
                print(colored("predlažemo Vam da odmah uradite check-in, kako biste što pre mogli izabrati svoje željeno sedište.\n", "yellow"))
                print(colored("VAŽNO OBAVEŠTENJE: ", "yellow", attrs = ["bold"]), end = "")       
                print(colored("check-in se može obaviti najkasnije 48h pre poletanja.", "yellow"))
                print(colored("Ukoliko ne čekirate Vašu kartu 48h pre poletanja, Vaša karta će postati nevažeća,\nte će Vam biti onemogućen ulazak u avion i let istim.", "yellow"))
                print(colored("\nTaca Airlines® ne snosi nikakve novčane naknade, te je Vaša dužnost da uredno čekirate kartu na vreme.\n\n", "yellow"))
                print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                while (True):
                    print("Da li želite odmah da čekirate Vašu upravo kupljenu kartu?\n")
                    print(colored("1) DA", "red"))
                    print(colored("2) NE", "red"))
                    print(colored("3) POVRATAK NA MENI\n\n", "red"))
                    odgovor = str(input("Unesite redni broj opcije koju želite: "))
                    if odgovor == "1":   
                        izabrana_opcija_direktan_check_in(Korisnik, kartaNew)
                        break
                    elif odgovor == "2":
                        break
                    elif odgovor == "3":
                        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                        print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                        print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                        trenutno_prijavljen(trenutni_ulogovan_korisnik)
                        return 
                    else: 
                        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red")) 
                        continue          
                #print("\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n") 
                print(colored("\nDa li želite da vidite karte za letove povezane sa prethodnim letom?\n\n", "yellow"))
                print(colored("1) DA", "red"))
                print(colored("2) NE", "red"))
                print(colored("3) POVRATAK NA MENI\n\n", "red"))
                while (True):
                    option = str(input("Unesite redni broj opcije koju želite: "))
                    if option == "1":
                        listaPovezanihLetova = letovi.povezani_letovi(sviLetovi, sviKonkretniLetovi, sviKonkretniLetovi[int(sifra)])
                        if len(listaPovezanihLetova) == 1:
                            print(colored("\n\n\nNažalost, trenutno ne postoji ni jedan povezani let za Vaš let.\nVraćamo Vas na glavni meni.\n", "light_red", attrs = ["bold"]))
                            print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                            if Korisnik["uloga"] == "korisnik":
                                ulogovan_kao_korisnik(Korisnik)
                                return
                            if Korisnik["uloga"] == "prodavac":
                                ulogovan_kao_prodavac(Korisnik) 
                                return
                            if Korisnik["uloga"] == "admin":
                                ulogovan_kao_admin(Korisnik) 
                                return       
                        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
                        print(colored("\nPREGLED SVIH POVEZANIH KONKRETNIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
                        print(tabulate(listaPovezanihLetova, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
                        print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                        izabrana_opcija_povezani_letovi(Korisnik, listaPovezanihLetova)     
                        return
                    elif option == "2":
                        print("\n\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n")
                        return
                    elif option == "3":
                        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
                        print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
                        print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
                        trenutno_prijavljen(trenutni_ulogovan_korisnik)
                        return
                    else:
                        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n\n", "light_red"))    
            except Exception as greska1:
                greska = colored(greska1, "light_red")
                print("\n\n\n", greska, "\n")   
                izabrana_opcija_kupovina_karata(Korisnik)
                return
    elif option == "3":
        print("\n\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
        print(colored("POVRATAK NA MENI\n", "yellow", attrs = ["underline", "bold"]), "\n")
        print("\n─────────────────────────────────────────────────────────────────────────────────────\n\n") 
        trenutno_prijavljen(trenutni_ulogovan_korisnik)
        return  
    else:
        print(colored("\n\n\nGREŠKA: Uneseni broj nije u dobrom formatu. Unesite ponovo.\n", "light_red"))
        izabrana_opcija_kupovina_karata(Korisnik)
        return
    
    
###################################################################################################   

# 6) FLEKSIBILNI POLASCI

def izabrana_opcija_fleks_polasci():
    global trenutni_ulogovan_korisnik
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("FLEKSIBILNI POLASCI\n", "yellow", attrs = ["underline", "bold"]), "\n")
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    sviKonkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    print("Molimo Vas da unesete sledeće podatke: ")
    polaziste = str(input("Unesite šifru polazišnog aerodroma: "))
    odrediste = str(input("Unesite šifru odredišnog aerodroma: "))
    datum_polaska = str(input("Unesite datum polaska (YYYY-MM-DD): "))
    datum_dolaska = str(input("Unesite datum dolaska (YYYY-MM-DD): "))
    broj_fleks_dana = str(input("Unesite broj fleksibilnih dana: "))
    try:
        lista = letovi.fleksibilni_polasci(sviLetovi, sviKonkretniLetovi, polaziste, odrediste, datum_polaska, datum_dolaska, broj_fleks_dana)
        newLista = [["BROJ", "LET", "ŠPA", "ŠOA", "POLETANJE", "SLETANJE", "PREVOZNIK", "MODEL", " CENA "]]
        for l in lista:      
            newLista.append(l)
        print("\n\n─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
        print(colored("\nPREGLED FLEKSIBILNIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
        print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
        print("\n─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
        return
    except Exception as greska1:
        greska = colored(greska1, "light_red")
        print("\n\n\n", greska, "\n")   
        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
        if opcijaNazad == 'x':
            print("\n\n")
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return
        else:
            print("\n\n")
            izabrana_opcija_fleks_polasci()
            return


###################################################################################################   

# 5) 10 NAJJEFTINIJIH LETOVA

def izabrana_opcija_10_najjeftinijih():
    global trenutni_ulogovan_korisnik
    print("\n\n──────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("PREGLED 10 NAJJEFTINIJIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    print("Molimo Vas da unesete sledeće podatke: ")
    polaziste = str(input("Unesite šifru polazišnog aerodroma: "))
    odrediste = str(input("Unesite šifru odredišnog aerodroma: "))
    try:
        lista = letovi.trazenje_10_najjeftinijih_letova(sviLetovi, polaziste, odrediste)
        newLista = [["BR.", "LET", "POLETANJE", "SLETANJE", "DPO", "DKO", "PREVOZNIK", "DANI", "MODEL", " CENA "]]
        for l in lista:      
            newLista.append(l)
        print("\n\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
        print(colored("\nPREGLED 10 NAJJEFTINIJIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
        print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
        print("\n────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
        return
    except Exception as greska1:
        greska = colored(greska1, "light_red")
        print("\n\n\n", greska, "\n")   
        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
        if opcijaNazad == 'x':
            print("\n\n")
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return
        else:
            print("\n\n")
            izabrana_opcija_10_najjeftinijih()
            return
    
    
###################################################################################################   

# 4) PRETRAGA LETOVA

def izabrana_opcija_pretraga_letova():
    global trenutni_ulogovan_korisnik
    print("\n\n──────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("PRETRAGA LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    print("Molimo Vas da unesete sledeće podatke: ")
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    konkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    polaziste = str(input("Unesite šifru polazišnog aerodroma: "))
    odrediste = str(input("Unesite šifru odredišnog aerodroma: "))
    datumPolaska = str(input("Unesite datum polaska (YYYY-MM-DD): "))
    datumDolaska = str(input("Unesite datum dolaska (YYYY-MM-DD): "))
    vremePoletanja = str(input("Unesite vreme poletanja (hh:mm): "))
    vremeSletanja = str(input("Unesite vreme sletanja (hh:mm): "))
    prevoznik = str(input("Unesite ime prevoznika: "))          
    headeri = {"sifra": "ŠIFRA",
               "broj_leta": "BROJ LETA", 
               "sifra_polazisnog_aerodroma": "ŠPA",
               "sifra_odredisnog_aerodorma": "ŠOA",
               "datum_i_vreme_polaska": "DATUM I VREME POLASKA", 
               "datum_i_vreme_dolaska": "DATUM I VREME DOLASKA",
               "prevoznik": "PREVOZNIK",
               "cena": "CENA"}
    newLista = []
    newLista.append(headeri)
    try:
        (lista, listaParametara) = letovi.pretraga_letova_proveri_sve(sviLetovi, konkretniLetovi, str(polaziste), str(odrediste), str(datumPolaska),
                                   str(datumDolaska), str(vremePoletanja), str(vremeSletanja), str(prevoznik))
        if len(lista) == 0:
            print("\n\n──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
            print(colored("\nNiste uneli ništa od parametara.\n\n", "light_red"))
            print(colored("PREGLED SVIH KONKRETNIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
            for let in konkretniLetovi:
                brojLeta = konkretniLetovi[let]["broj_leta"]
                newDict = {"sifra": konkretniLetovi[let]["sifra"],
                           "broj_leta": brojLeta, 
                           "datum_i_vreme_polaska": konkretniLetovi[let]["datum_i_vreme_polaska"],
                           "sifra_polazisnog_aerodroma": sviLetovi[brojLeta]["sifra_polazisnog_aerodroma"],
                           "sifra_odredisnog_aerodorma": sviLetovi[brojLeta]["sifra_odredisnog_aerodorma"], 
                           "datum_i_vreme_dolaska": konkretniLetovi[let]["datum_i_vreme_dolaska"],
                           "prevoznik": sviLetovi[brojLeta]["prevoznik"],
                           "cena": float("{:.2f}".format(sviLetovi[brojLeta]["cena"]))}
                newLista.append(newDict)
            print(tabulate(newLista,  headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
            print("\n\n──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
            return    
        else:
            for i in lista:
                newLista.append(i)
        print("\n\n──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
        print(colored("\nIzabrali ste pretragu letova po ", "yellow"), end = "")
        lenListaParametara = len(listaParametara)
        for br in range(0, lenListaParametara):
            if (br == lenListaParametara - 1):
                print(colored(listaParametara[br], "yellow"), end = "")
                print(colored(". \n", "yellow"))
            elif (br == lenListaParametara - 2):
                print(colored(listaParametara[br], "yellow"), end = "")  
                print(colored(" i ", "yellow"), end = "")    
            else:
                print(colored(listaParametara[br], "yellow"), end = "")
                print(colored(", ", "yellow"), end = "")
        print(colored("\nPREGLED IZABRANIH KONKRETNIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n\n")
        print(tabulate(newLista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"), "\n")
        print("\n\n──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n")
        return
    except Exception as greska1:
        greska = colored(greska1, "light_red")
        print("\n\n\n", greska, "\n")   
        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
        if opcijaNazad == 'x':
            print("\n\n")
            trenutno_prijavljen(trenutni_ulogovan_korisnik)
            return
        else:
            print("\n\n")
            izabrana_opcija_pretraga_letova()
            return
        

###################################################################################################

# 3) PREGLED NEREALIZOVANIH LETOVA

def pregled_nerealizovanih_letova():
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("PREGLED NEREALIZOVANIH LETOVA\n", "yellow", attrs = ["underline", "bold"]), "\n")
    sviLetovi = letovi.ucitaj_letove_iz_fajla("svi_letovi.txt", "|")
    konkretniLetovi = konkretni_letovi.ucitaj_konkretan_let("svi_konkretni_letovi.txt", "|")
    listaLetova = letovi.pregled_nerealizovanih_letova(konkretniLetovi)
    num = 1
    lista = [["BR.", "BR. LETA", "ŠIFRA", "ŠPA", "ŠOA", "POLETANJE", "SLETANJE", "DPO", "DKO", "PREVOZNIK", "CENA"]]
    for let in listaLetova:
        brojLeta = let["broj_leta"]
        x1 = let["broj_leta"]
        x12 = let["sifra"]
        x2 = sviLetovi[brojLeta]["sifra_polazisnog_aerodroma"]
        x3 = sviLetovi[brojLeta]["sifra_odredisnog_aerodorma"]
        x4 = sviLetovi[brojLeta]["vreme_poletanja"] + "h"
        x5 = sviLetovi[brojLeta]["vreme_sletanja"] + "h"
        x66 = let["datum_i_vreme_polaska"]
        x6 = str(str(x66.year) + "/" + str(x66.month) + "/" + str(x66.day))
        x77 = let["datum_i_vreme_dolaska"]
        x7 = str(str(x77.year) + "/" + str(x77.month) + "/" + str(x77.day))
        x8 = sviLetovi[brojLeta]["prevoznik"]
        x10 = sviLetovi[brojLeta]["model"]["naziv"]
        x111 = sviLetovi[brojLeta]["cena"]
        x11 = float("{:.2f}".format(x111))
        lista.append([num, x1, x12, x2, x3, x4, x5, x6, x7, x8, x11])
        num += 1
    print(tabulate(lista, headers = 'firstrow', tablefmt = 'simple_grid', numalign = "center", stralign = "center"))
    print("\n\n───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("\n")
    return


####################################################################################################

# 2) PRIJAVA NA SISTEM

def dobrodoslica_ulogovanog_layout(korisnik: dict):
    print_time()
    print("Trenutno ste prijavljeni kao '", end = "")
    print(korisnik["korisnicko_ime"], end = "")
    print("'.")
    print("Vaša uloga je '", end = "")
    print(korisnik["uloga"], end = "")
    print("'\n\n")
    print("\nUkoliko želite da se odjavite, idite na 'ODJAVA SA SISTEMA' na meniju.\n\n")
    s = "┌──────────────"
    g = "└──────────────"
    for i in range(0, len(korisnik["korisnicko_ime"]) - 1):
        s += "─"
        g += "─"
    s += "┐"    
    g += "┘"
    print(colored(s, "green"))
    print(colored("│ Zdravo, '", "green"), end = "")
    print(colored(korisnik["korisnicko_ime"], "green"), end = "")
    print(colored("'! │", "green")) 
    print(colored(g, "green"), "\n\n")    
    return


###################################################################################################

def ulogovan_kao_korisnik(korisnik: dict):
    dobrodoslica_ulogovanog_layout(korisnik)
    print(colored("Dobro došli na meni za prijavljene korisnike!", "light_red", attrs = ["bold", "underline"]), end = "")
    print(" 👋\n")
    print("Molim Vas izaberite jednu od opcija:\n")
    print(colored("1) PREGLED NEREALIZOVANIH LETOVA", "red"))
    print(colored("2) PRETRAGA LETOVA", "red"))
    print(colored("3) PREGLED 10 NAJJEFTINIJIH LETOVA", "red"))
    print(colored("4) FLEKSIBILNI POLASCI", "red"))
    print(colored("5) KUPOVINA KARATA", "red"))
    print(colored("6) PRIJAVA NA LET (CHECK-IN)", "red"))
    print(colored("7) PREGLED NEREALIZOVANIH KARATA", "red"))
    print(colored("8) ODJAVA SA SISTEMA", "red"))
    print(colored("9) IZLAZAK IZ APLIKACIJE", "red"))
    ok = 0
    korisnickoIme = korisnik["korisnicko_ime"]
    while (ok == 0):
        opcija = str(input("\nUnesite redni broj opcije koju želite: "))
        if opcija == "1":
            ok = 1
            pregled_nerealizovanih_letova()
        elif opcija == "2": 
            ok = 1
            izabrana_opcija_pretraga_letova()
        elif opcija == "3": 
            ok = 1
            izabrana_opcija_10_najjeftinijih()
        elif opcija == "4": 
            ok = 1
            izabrana_opcija_fleks_polasci()
        elif opcija == "5": 
            ok = 1
            izabrana_opcija_kupovina_karata(korisnik)
        elif opcija == "6": 
            ok = 1
            izabrana_opcija_check_in(korisnik) 
        elif opcija == "7": 
            ok = 1 
            izabrana_opcija_pregled_nerealizovanih_karata(korisnik)   
        elif opcija == "8": 
            ok = 1    
            korisnici.logout(korisnickoIme)
            glavni_meni_layout()
        elif opcija == "9": 
            ok = 1    
            izlazak_iz_aplikacije()    
        else:
            greska = colored("GRESKA! Unešeni redni broj opcije nije dobro definisan. Molim Vas unesite ponovo.", "red")
            print("\n\n", greska, "\n\n") 
            print("───────────────────────────────────────────────────────────────────────────────────────")
            print("\n")
            ulogovan_kao_korisnik(korisnik)
            return
    ulogovan_kao_korisnik(korisnik)
    return
    
    
def ulogovan_kao_prodavac(korisnik: dict):   
    dobrodoslica_ulogovanog_layout(korisnik)
    print(colored("Dobro došli na meni za prijavljene prodavce!", "cyan", attrs = ["bold", "underline"]), end = "")
    print(" 🎫\n")
    print("Molim Vas izaberite jednu od opcija:\n")
    print(colored("1) PREGLED NEREALIZOVANIH LETOVA", "cyan"))
    print(colored("2) PRETRAGA LETOVA", "cyan"))
    print(colored("3) PREGLED 10 NAJJEFTINIJIH LETOVA", "cyan"))
    print(colored("4) FLEKSIBILNI POLASCI", "cyan"))
    print(colored("5) PRODAJA KARATA", "cyan"))
    print(colored("6) PRIJAVA NA LET (CHECK-IN)", "cyan"))
    print(colored("7) IZMENA KARTE", "cyan"))
    print(colored("8) BRISANJE KARTE", "cyan"))
    print(colored("9) PRETRAGA PRODATIH KARATA", "cyan"))
    print(colored("10) ODJAVA SA SISTEMA", "cyan"))
    print(colored("11) IZLAZAK IZ APLIKACIJE", "cyan"))
    ok = 0
    korisnickoIme = korisnik["korisnicko_ime"]
    while (ok == 0):
        opcija = str(input("\nUnesite redni broj opcije koju želite: "))
        if opcija == "1":
            ok = 1
            pregled_nerealizovanih_letova()
        elif opcija == "2": 
            ok = 1
            izabrana_opcija_pretraga_letova()
        elif opcija == "3": 
            ok = 1
            izabrana_opcija_10_najjeftinijih()
        elif opcija == "4": 
            ok = 1
            izabrana_opcija_fleks_polasci()
        elif opcija == "5": 
            ok = 1
            izabrana_opcija_prodaja_karata(korisnik)
        elif opcija == "6": 
            ok = 1
            izabrana_opcija_check_in_prodavac(korisnik) 
        elif opcija == "7": 
            ok = 1 
            izabrana_opcija_izmena_karata(korisnik)   
        elif opcija == "8": 
            ok = 1 
            izabrana_opcija_brisanje_karte_prodavac(korisnik)  
        elif opcija == "9": 
            ok = 1 
            izabrana_opcija_pregled_prodatih_karata()      
        elif opcija == "10": 
            ok = 1    
            korisnici.logout(korisnickoIme)
            glavni_meni_layout()
        elif opcija == "11": 
            ok = 1    
            izlazak_iz_aplikacije()    
        else:
            greska = colored("GRESKA! Unešeni redni broj opcije nije dobro definisan. Molim Vas unesite ponovo.", "red")
            print("\n\n", greska, "\n\n") 
            print("───────────────────────────────────────────────────────────────────────────────────────")
            print("\n")
            ulogovan_kao_prodavac(korisnik)
            return
    ulogovan_kao_prodavac(korisnik)
    return


def ulogovan_kao_admin(korisnik: dict):   
    dobrodoslica_ulogovanog_layout(korisnik)
    print(colored("Dobro došli na VIP meni za admine!", "light_yellow", attrs = ["bold", "underline"]), end = "")
    print(" ⭐\n")
    print("Molim Vas izaberite jednu od opcija:\n")
    print(colored("1) PREGLED NEREALIZOVANIH LETOVA", "yellow"))
    print(colored("2) PRETRAGA LETOVA", "yellow"))
    print(colored("3) PREGLED 10 NAJJEFTINIJIH LETOVA", "yellow"))
    print(colored("4) FLEKSIBILNI POLASCI", "yellow"))
    print(colored("5) PRETRAGA PRODATIH KARATA", "yellow"))
    print(colored("6) BRISANJE KARTE", "yellow"))
    print(colored("7) REGISTRACIJA NOVIH PRODAVACA", "yellow"))
    print(colored("8) KREIRANJE LETOVA", "yellow"))
    print(colored("9) IZMENA LETOVA", "yellow"))
    print(colored("10) IZVESTAVANJE", "yellow"))
    print(colored("11) KREIRANJE MODELA AVIONA", "yellow"))
    print(colored("12) ODJAVA SA SISTEMA", "yellow"))
    print(colored("13) IZLAZAK IZ APLIKACIJE", "yellow"))
    ok = 0
    korisnickoIme = korisnik["korisnicko_ime"]
    while (ok == 0):
        opcija = str(input("\nUnesite redni broj opcije koju želite: "))
        if opcija == "1":
            ok = 1
            pregled_nerealizovanih_letova()
        elif opcija == "2": 
            ok = 1
            izabrana_opcija_pretraga_letova()
        elif opcija == "3": 
            ok = 1
            izabrana_opcija_10_najjeftinijih()
        elif opcija == "4": 
            ok = 1
            izabrana_opcija_fleks_polasci()
        elif opcija == "5": 
            ok = 1
            izabrana_opcija_pregled_prodatih_karata()
        elif opcija == "6": 
            ok = 1
            izabrana_opcija_brisanje_karte_admin(korisnik)  
        elif opcija == "7": 
            ok = 1 
            izabrana_opcija_registrovanje_prodavaca()
        elif opcija == "8": 
            ok = 1 
            izabrana_opcija_kreiranje_letova()
        elif opcija == "9": 
            ok = 1 
            izabrana_opcija_izmena_letova()
        elif opcija == "10": 
            ok = 1 
            izabrana_opcija_izvestavanje()  
        elif opcija == "11": 
            ok = 1     
            izabrana_opcija_kreiranje_modela_aviona()    
        elif opcija == "12": 
            ok = 1    
            korisnici.logout(korisnickoIme)
            glavni_meni_layout()
        elif opcija == "13": 
            ok = 1    
            izlazak_iz_aplikacije()    
        else:
            greska = colored("GRESKA! Unešeni redni broj opcije nije dobro definisan. Molim Vas unesite ponovo.", "red")
            print("\n\n", greska, "\n\n") 
            print("───────────────────────────────────────────────────────────────────────────────────────")
            print("\n")
            ulogovan_kao_admin(korisnik)
            return
    ulogovan_kao_admin(korisnik)
    return
 
###################################################################################################   
   
def trenutno_prijavljen(korisnik: dict):
    uloga = korisnik["uloga"]
    if uloga == "korisnik":
        ulogovan_kao_korisnik(korisnik)
        return
    if uloga == "prodavac":
        ulogovan_kao_prodavac(korisnik)
        return
    if uloga == "admin":
        ulogovan_kao_admin(korisnik)
        return

###################################################################################################
    
def prijava_obrada(sviKorisnici: dict):
    global trenutni_ulogovan_korisnik
    print("Molimo Vas da unesete sledeće podatke: ")
    korisnickoImeKorisnika = input("Unesite korisničko ime: ")
    lozinkaKorisnika = input("Unesite lozinku: ")
    try:
        korisnik = korisnici.login(sviKorisnici, korisnickoImeKorisnika, lozinkaKorisnika)
        trenutni_ulogovan_korisnik = korisnik
        print("\n")
        print(colored("PRIJAVA USPEŠNA.\n", "green", attrs = ["bold", "underline"]))
        print(colored("Dobrodošli,", "green"), end = "")
        print(colored(" '", "light_green"), end = "")
        print(colored(korisnickoImeKorisnika, "light_green"), end = "")
        print(colored("'! ", "light_green"), "\n\n")
        print("─────────────────────────────────────────────────────────────────────────────\n")
        trenutno_prijavljen(korisnik)    
        return 
    except Exception as greska1:
        greska = colored(greska1, "light_red")
        print("\n\n", colored("PRIJAVA NEUSPELA!\n", "light_red", attrs = ["bold"]), greska, "\n\n")    
        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
        if opcijaNazad == 'x':
            print("\n\n")
            return
        else:
            print("\n\n")
            prijava_obrada(sviKorisnici)    
            return

def izabrana_opcija_prijava():
    print("\n\n─────────────────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("PRIJAVA", "yellow", attrs = ["underline", "bold"]), "\n")
    sviKorisnici = korisnici.ucitaj_korisnike_iz_fajla("svi_korisnici.txt", "|")
    prijava_obrada(sviKorisnici)
    glavni_meni_layout()  
        
 
###################################################################################################

# 1) REGISTRACIJA NOVOG KORISNIKA
   
def izabrana_opcija_registracija():
    print("\n\n──────────────────────────────────────────────────────────────────\n")
    print("\n", colored("Izabrali ste opciju: ", "yellow"), end = "")
    print(colored("REGISTRACIJA KORISNIKA", "yellow", attrs = ["underline", "bold"]), "\n")
    sviKorisnici = korisnici.ucitaj_korisnike_iz_fajla("svi_korisnici.txt", "|") # dict
    print("Molimo Vas da unesete sledeće podatke: ")
    staroKorisnickoIme = input("Staro korisničko ime (nije obavezno): ")
    novoKorisnickoIme = input("Novo korisničko ime: ")
    lozinka = input("Lozinka: ")
    ime = input("Ime: ")
    prezime = input("Prezime: ")
    email = input("Email: ")
    pasos = input("Pasoš (nije obavezno): ")
    drzavljanstvo = input("Državljanstvo (nije obavezno): ")
    telefon = input("Telefon: ")
    pol = input("Pol (nije obavezno): ")
    try:
        sviKorisniciDopunjen = korisnici.kreiraj_korisnika(sviKorisnici, False, "korisnik",
                                                           staroKorisnickoIme, novoKorisnickoIme,
                                                           lozinka, ime, prezime, email, pasos,
                                                           drzavljanstvo, telefon, pol)
        ocisti_file("svi_korisnici.txt")
        korisnici.sacuvaj_korisnike("svi_korisnici.txt", "|", sviKorisniciDopunjen)
        print("\n")
        print(colored("Korisnik", "green"), end = "")
        print(colored(" '", "light_green"), end = "")
        print(colored(novoKorisnickoIme, "light_green", attrs = ["underline"]), end = "")
        print(colored("' ", "light_green"), end = "")
        print(colored("je uspešno registrovan!\nMožete se prijaviti na aplikaciju preko opcije iz glavnog menija: 2) PRIJAVA!", "green"), "\n\n")
        print("─────────────────────────────────────────────────────────────────────────────\n\n\n")
        return
    except Exception as greska1:
        greska = colored(greska1, "light_red")
        print("\n\n", colored("REGISTRACIJA NEUSPELA!\n", "light_red", attrs = ["bold"]), greska, "\n\n")    
        opcijaNazad = str(input("\nAko želite nazad na meni, unesite 'x', u suprotnome, unesite bilo šta drugo da nastavite: "))
        if opcijaNazad == 'x':
            print("\n\n")
            return
        else:
            print("\n\n")
            izabrana_opcija_registracija() 
            return
   
     
###################################################################################################


# ------------------///  GLAVNI MENI -> LAYOUT  \\\------------------

def glavni_meni_layout():
    print(colored("Dobro došli na glavni meni!\n\n", "light_red", attrs = ["bold", "underline"]))
    print("Molim Vas izaberite jednu od opcija:\n")
    print(colored("1) REGISTRACIJA", "red"))
    print(colored("2) PRIJAVA", "red"))
    print(colored("3) PREGLED NEREALIZOVANIH LETOVA", "red"))
    print(colored("4) PRETRAGA LETOVA", "red"))
    print(colored("5) PREGLED 10 NAJJEFTINIJIH LETOVA", "red"))
    print(colored("6) FLEKSIBILNI POLASCI", "red"))
    print(colored("7) IZLAZAK IZ APLIKACIJE", "red"))
    ok = 0
    while (ok == 0):
        opcija = str(input("\nUnesite redni broj opcije koju želite: "))
        if opcija == "1":
            ok = 1
            izabrana_opcija_registracija()
        elif opcija == "2": 
            ok = 1
            izabrana_opcija_prijava()
        elif opcija == "3": 
            ok = 1
            pregled_nerealizovanih_letova()
        elif opcija == "4": 
            ok = 1
            izabrana_opcija_pretraga_letova()
        elif opcija == "5": 
            ok = 1
            izabrana_opcija_10_najjeftinijih()
        elif opcija == "6": 
            ok = 1
            izabrana_opcija_fleks_polasci()
        elif opcija == "7": 
            ok = 1
            izlazak_iz_aplikacije()
        else:
            greska = colored("GREŠKA! Unešeni redni broj opcije nije dobro definisan. Molim Vas unesite ponovo.", "red")
            print("\n\n", greska, "\n\n") 
            print("───────────────────────────────────────────────────────────────────────────────────────")
            print("\n\n")
            glavni_meni_layout()
    glavni_meni_layout()
    
    
###################################################################################################


def dobrodosli_layout():
    print("\n")
    print_time()
    print(colored("\n┌─────────────┐", "red", attrs = ["bold", "dark"]))
    print(colored("│ ", "red", attrs = ["dark"]), end = "")
    print(colored("Dobrodošli!", "red", attrs = ["bold", "dark"]), end = "")
    print(colored(" │", "red", attrs = ["dark"]))
    print(colored("└─────────────┘", "red", attrs = ["bold", "dark"]))
    print("\n\nHvala Vam što koristite našu aplikaciju!\n") 
    print("Ako imate bilo kakvih pitanja ili primedbi u vezi aplikacije, možete nas kontaktirati:")
    print("- službeni mail: tacaairlines@gmail.com")
    print("- broj telefona: +381 65 114 6648, +381 65 116 2248\n")
    print(colored("\nUživajte!\n", "green", attrs = ["bold", "underline"]))
    print("\n──────────────────────────────────────────────────────────────────────────────────────\n")
    print("\n")
    return

def answer():   
    dobrodosli_layout() 
    glavni_meni_layout()
    print("\n")
    return


###################################################################################################


if __name__ == '__main__':
    answer()


###################################################################################################


"""
         TO-DO LIST
         
- na pregled karata polazak i dolazak leta

"""

