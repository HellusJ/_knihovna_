import os
import matplotlib.pyplot as plt
import time as t
from knihy import *
from datetime import date

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
    print("Kniha byla úspěšně přidána")

pujceneknihy = {}

dneska = date.today()

#pujceni knihy
def borrowbook():
    nazevknihy = str(input("Zadejte název knihy: "))

    for klic, kniha in knihy.items():
        if kniha["název"] == nazevknihy:
            pujceneknihy[klic] = knihy[klic]
            del knihy[klic]
            print("Kniha byla úspěšně půjčena.")
            print(f"Datum výpůjčky: {dneska}")
            print(f"Název knihy: {nazevknihy}")
            print(f"Uživatel: {jmeno}")
            break
    else:
        print("Kniha není k dispozici")

#vraceni knihy
def returnbook():
    if not pujceneknihy:
        print("Nemáte žádné půjčené knihy")

    else:
        vraceni = str(input("Napište název knihy, kterou chcete vrátit: "))
        for klic, kniha in pujceneknihy.items():
            if kniha["název"] == vraceni:
                knihy[klic] = pujceneknihy[klic]
                print("Kniha úspěšně vrácena")
                del pujceneknihy[klic]
                break

#graf podle autoru
autori_count = {}
def getchart():
    for kniha in knihy.values():
        autor = kniha["autor"]
        if autor in autori_count:
            autori_count[autor] += 1
        else:
            autori_count[autor] = 1

    autori = list(autori_count.keys())
    pocet_knih = list(autori_count.values())

    x = list(autori)
    y = list(pocet_knih)

    plt.bar(x, y, color="green", label="Počet knih k autorovi")

    plt.xlabel("Autoři")
    plt.ylabel("Počet knih k autorovi")
    plt.title("Počet dostupných knih podle autorů")
    plt.legend()
    plt.show()
    
#Registrace
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
            print("")
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
6 - Vrátit knihu    
7 - Zobrazit graf podle autorů         
8 - Ukončit program
Pište zde: """))
    print("")

    if menu == 8:
        print("Ukončuji program")
        exit()
    
    if menu == 7:
        getchart()

    if menu == 6:
        returnbook()
        input()

    if menu == 5:
        borrowbook()
        input()

    if menu == 4:
        addbook()
        input()   

    if menu == 3:
        print(f"Jméné: {jmeno}")
        print(f"Heslo: {heslo}")
        input()

    if menu == 2:
        for kniha in knihy.values():
            print(kniha["název"])
        input()

    if menu == 1:
        if not pujceneknihy:
            print("Žádné půjčené knihy")
        else:
            for Kniha in pujceneknihy.values():
                print(Kniha["název"])
        input()