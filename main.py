import os
from knihy import *

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
        "dostupnost": "ANO"
    }

    knihy[knizka] = veci
    print(knihy)

