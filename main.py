import os
import time as t
from knihy import *

#FUNKCE
#pridani knih
def addbook():
    poradiknihy = str(input("Zadejte poradi knihy: "))
    knizka = f"kniha{poradiknihy}"
    nazevknihy = str(input("Zadejte název knihy: "))
    nazevautora = str(input("Zadejte jméno autora: "))
    isbn = str(input("Zadejte ISBN knihy: "))
    veci = {
        "název": nazevknihy,
        "autor": nazevautora,
        "ISBN": isbn,
        "dostupnost": "ANO"}
    knihy[knizka] = veci

pujceneknihy = {}

#pujceni knihy
def borrowbook():
    nazevknihy = str(input("Zadejt název knihy: "))
    for klic, kniha in knihy.items():
        if nazevknihy in kniha["název"]:
            pujceneknihy[klic] = knihy[klic]
            del knihy[klic]    
            print(pujceneknihy) 
            print(knihy)
            break
        else:
            print("Kniha není k dispozici")

#registrace
slozka_hesel = "users.txt"

registration_exists = os.path.exists(slozka_hesel) and os.path.getsize(slozka_hesel) > 0

if registration_exists:
    print("Přihlášení:")
    jmeno = input("Zadejte uživatelské jméno: ")
    heslo = input("Zadejte heslo: ")

    with open(slozka_hesel, "r") as file:
        users = file.readlines()

    for user in users:
        uziv_jmeno, uziv_heslo = user.strip().split(",")
        if jmeno == uziv_jmeno and heslo == uziv_heslo:
            print("Přihlášení bylo úspěšné!")
            break
    else:
        print("Nesprávné uživatelské jméno nebo heslo.")

else:
    print("Registrace nového uživatele:")
    jmeno = input("Zadejte uživatelské jméno: ")
    heslo = input("Zadejte heslo: ")

    with open(slozka_hesel, "w") as file:
        file.write(f"{jmeno},{heslo}")

    print("Registrace byla úspěšná! Nyní se můžete přihlásit.")

#menu
while True:
    menu = int(input("""Zadejte operaci:
1 - váš seznam půjčených knih
2 - seznam všech knih
3 - vaše osobní údaje
4 - Přídání nové knihy
5 - Pujčení knihy                 
6 - Ukončit program
Pište zde: """))

    if menu == 6:
        print("Ukončuji program")
        exit()

    if menu == 3:
        print(f"Jméné: {jmeno}")
        print(f"Heslo: {heslo}")
        t.sleep(2.5)

    if menu == 2:
        for kniha in knihy.values():
            print(kniha["název"])
        t.sleep(4)

    if menu == 4:
        addbook()

    if menu == 5:
        borrowbook()
        