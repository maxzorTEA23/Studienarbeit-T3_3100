# Import Bibliotheken
from SPS import Schreiben
from Historie import schreibe_historie
from snap7.util import set_bool 
import pandas as pd
# Funktion zur Steuerung des Auftragsbasierenden Auslagerns
def Auslagern(plc, Code_Scanner):
    # Bestehende CSV Tabelle auslesen
    table = pd.read_csv("CSV_Daten.csv", sep=";")
    table.columns = table.columns.str.strip()
    # Barcode Scannen
    # Sicherstellen das eine Zeile gefiltert wird auf Scanner wert
    print(list(table.columns))
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
        Material = str(Entry["Materialname"])
        # Schreiben der Werte in SPS Code über Snap7
        Schreiben(plc, Lagerplatz_x, Lagerplatz_y, Material)
        schreibe_historie("Auslagerung", Barcode,Lagerplatz_x,Lagerplatz_y)
        print(f"Auslagerung gestartet: {Barcode} → ({Lagerplatz_x}, {Lagerplatz_y})")
        
       

    else:
        # Fehlermeldung falls Barcode nicht gefunden wird 
        print("Barcode nicht gefunden")
