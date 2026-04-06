print("--- TEXT ANALYSE TOOL ---")
text = input("Gib deinen Text ein:\n").strip()

if not text:
    print("Der Text ist leer.")
else:
    # Text in eine Liste von Wörtern umwandeln
    raw_words = text.split()
    word_count = len(raw_words)

    # Dictionary für die Worthäufigkeit initialisieren
    word_freq = {}

    for word in raw_words:
        # Satzzeichen entfernen und in Kleinschreibung umwandeln
        clean_word = word.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
        # Das Zählen
        if clean_word in word_freq:
            word_freq[clean_word] += 1
        else:
            word_freq[clean_word] = 1
    # Ergebnis formatieren und ausgeben
    print(f"\nErgebnis:")
    print(f"Gesamtanzahl der Wörter: {word_count}")
    print("---------------------------------")
    print("Häufigkeit der Wörter:")

    # Sortierte Ausgabe der Wörter
    for word in word_freq:
        print(f" - {word}: {word_freq[word]}")

print("\n---------------------------------")
input("Zum Schließen des Fensters Enter drücken...")