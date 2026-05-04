# Import Bibliotheken
from SPS import Einlesen
from Historie import schreibe_historie
import pandas as pd
from snap7.util import set_bool
# Funktion zum Lesen der Variablen Lagerplätze und RFID_Code, aus der SPS -> danach Schreiben in bestehende CSV 
def Einlagern_CSV(plc):
    # Einlesen der bestehenden CSV Tabelle
    table = pd.read_csv('CSV_Daten.csv', sep=";")
    table.columns = table.columns.str.strip()
    # Einlesen der Werte nach Einlagerung von SPS
    Lagerplatz_x, Lagerplatz_y, rfid_code_1, rfid_code_2= Einlesen(plc)
    RFID_Code = f"{rfid_code_1}-{rfid_code_2}"
    # überprüfung ob Code vorhanden (RFID vgl Barcode)
    row = table.loc[table["Barcode"] == RFID_Code]
    # Joining anhand des Codes 
    if not row.empty:
        table.loc[table["Barcode"] == RFID_Code, "Lagerplatz x"] = Lagerplatz_x
        table.loc[table["Barcode"] == RFID_Code, "Lagerplatz y"] = Lagerplatz_y
    # Speichern der neuen Tabelle mit aktualisierten Werten
    table.to_csv("CSV_Daten.csv",sep=";", index=False)
    schreibe_historie("Einlagerung", RFID_Code,Lagerplatz_x,Lagerplatz_y)
    print(table)
    

Einlagern_CSV(1)