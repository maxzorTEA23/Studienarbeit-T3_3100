# Import Bibliotheken
from SPS import Schreiben
from Historie import schreibe_historie
import pandas as pd
from snap7.util import get_int, get_bool, get_real, get_string, set_int,set_string,set_bool
# Funktion zur Steuerung des Auftragsbasierenden Auslagerns
def Auslagern(plc):
    # Bestehende CSV Tabelle auslesen
    table = pd.read_csv("CSV_Daten.csv")
    table.columns = table.columns.str.strip()
    # Barcode Scannen
    Code_Scanner = "1234"   # als String
    # Sicherstellen das eine Zeile gefiltert wird auf Scanner wert
    row = table.loc[table["Barcode"].astype(str) == Code_Scanner]
    # Überprüfen ob die Zeile Leer ist 
    if not row.empty:
        # erste Zeile auswählen welche gefunden wurde
        Entry = row.iloc[0]
        # Feststellen ob Material eingelagert wurde
        if pd.isna(Entry["Lagerplatz x"]) or pd.isna(Entry["Lagerplatz y"]):
            print("Material nicht eingelagert!")
            return
        # Lagerplätze und Barcode setzen 
        Lagerplatz_x = int(Entry["Lagerplatz x"])
        Lagerplatz_y = int(Entry["Lagerplatz y"])
        Barcode = int(Entry["Barcode"])
        # Schreiben der Werte in SPS Code über Snap7
        Schreiben(plc, Lagerplatz_x, Lagerplatz_y, Barcode)
        schreibe_historie("Auslagerung", Barcode,Lagerplatz_x,Lagerplatz_y)
        print(f"Auslagerung gestartet: {Barcode} → ({Lagerplatz_x}, {Lagerplatz_y})")

    else:
        # Fehlermeldung falls Barcode nicht gefunden wird 
        print("Barcode nicht gefunden")
