using System;
using System.IO;
using System.Collections.Generic;

namespace DocManagerApp
{
    class Program
    {
        // Name der Datei zum Speichern / Имя файла для хранения данных
        private const string DataFile = "dokumente.txt";

        static void Main()
        {
            // Hauptmenü-Schleife / Главный цикл меню
            while (true)
            {
                Console.WriteLine("\n--- DOKUMENTEN-MANAGER ---");
                Console.WriteLine("1. Dokument hinzufügen");
                Console.WriteLine("2. Alle anzeigen");
                Console.WriteLine("3. Suchen");
                Console.WriteLine("4. Beenden");
                Console.Write("\nAuswahl: ");

                var input = Console.ReadLine();

                if (input == "4") break;

                switch (input)
                {
                    case "1":
                        AddDocument();
                        break;
                    case "2":
                        ShowAll();
                        break;
                    case "3":
                        FindDocument();
                        break;
                    default:
                        Console.WriteLine("Falsche Eingabe.");
                        break;
                }
            }
        }

        static void AddDocument()
        {
            Console.Write("Name des Dokuments: ");
            var title = Console.ReadLine()?.Trim();

            if (string.IsNullOrEmpty(title)) return;

            // Speichert den Namen in einer neuen Zeile / Запись в новую строку
            File.AppendAllLines(DataFile, new[] { title });
            Console.WriteLine("Erfolgreich gespeichert!");
        }

        static void ShowAll()
        {
            if (!File.Exists(DataFile))
            {
                Console.WriteLine("Keine Dokumente gefunden.");
                return;
            }

            Console.WriteLine("\nGespeicherte Dokumente:");
            // Liest alle Zeilen nacheinander / Чтение всех строк
            foreach (var line in File.ReadLines(DataFile))
            {
                Console.WriteLine($"- {line}");
            }
        }

        static void FindDocument()
        {
            if (!File.Exists(DataFile)) return;

            Console.Write("Suchbegriff eingeben: ");
            var query = Console.ReadLine()?.ToLower().Trim();

            if (string.IsNullOrEmpty(query)) return;

            Console.WriteLine("Suchergebnisse:");
            bool found = false;

            foreach (var line in File.ReadLines(DataFile))
            {
                if (line.ToLower().Contains(query))
                {
                    Console.WriteLine($"> {line}");
                    found = true;
                }
            }

            if (!found) Console.WriteLine("Nichts gefunden.");
        }
    }
}