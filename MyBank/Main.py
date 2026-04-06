import json

# Die Kontodaten # Данные клиентов
konten = [
    {"nr": "101", "pin": "1234", "name": "Dmitry", "geld": 500.0},
    {"nr": "202", "pin": "2008", "name": "Yaroslav", "geld": 125000.0},
    {"nr": "303", "pin": "9876", "name": "Elisabeth", "geld": 50.0}
]

print("--- Willkommen am Geldautomaten ---")
eingabe_nr = input("Kontonummer: ")

# Konto suchen # Поиск аккаунта
mein_konto = None
for k in konten:
    if k["nr"] == eingabe_nr:
        mein_konto = k
        break
# System # Система
if mein_konto == None:
    print("Nummer nicht gefunden.")
else:
    eingabe_pin = input(f"Hallo {mein_konto['name']}, bitte PIN: ")

    if eingabe_pin == mein_konto["pin"]:
        print(f"Login OK. Kontostand: {mein_konto['geld']} Euro")

        print("1 - Geld abheben")
        print("2 - Abbrechen")
        wahl = input("Wahl: ")

        if wahl == "1":
            betrag = float(input("Betrag: "))

            if betrag <= mein_konto["geld"]:
                mein_konto["geld"] = mein_konto["geld"] - betrag
                print("Auszahlung erfolgt...")
                print(f"Neuer Kontostand: {mein_konto['geld']} Euro")
            else:
                print("Nicht genug Guthaben!")
        else:
            print("Sitzung beendet.")
    else:
        print("PIN falsch!")
input("Zum Schließen des Fensters Enter drücken...")