import time

# Zugangsdaten
nutzer_liste = {
    "Dmitry": "1122",
    "Svetlana": "4455",
    "Yaroslav": "2008"
}

print("--- MYSICHERHEITSSYSTEM (V. 1.1) ---")
user = input("Benutzername eingeben: ")

# Check ob der User existiert
if user not in nutzer_liste:
    print("Fehler: Dieser Nutzer ist im System nicht bekannt.")
else:
    print(f"Hallo {user}. Sie haben jetzt 30 Sekunden fuer den Sicherheitscode.")


    start_punkt = time.time()

    passwort = input("Sicherheitscode: ")

    # Zeit berechnen
    ende_punkt = time.time()
    vergangene_zeit = ende_punkt - start_punkt

    # Check 1: Ist die Zeit abgelaufen?
    if vergangene_zeit > 30:
        print("\n!!! ALARM !!!")
        print(f"Zeitueberschreitung!")
        print("Zugriff wurde aus Sicherheitsgruenden blockiert.")

    else:
        # Check 2: Ist das Passwort richtig?
        if passwort == nutzer_liste[user]:
            print("\nZUGRIFF ERTEILT.")
            print(f"System entsperrt in {round(vergangene_zeit, 1)} Sekunden.")
        else:
            print("\nZUGRIFF VERWEIGERT!")
            print("Der eingegebene Code ist falsch.")
