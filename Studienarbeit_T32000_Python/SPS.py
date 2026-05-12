# Import Bibliotheken
from snap7.util import get_int, get_bool, get_real, get_string, set_int,set_string
# Programm zum Einlesen und Schreiben von und auf die SPS

# Funktion zum Einlesen der Werte von SPS
def Einlesen(plc):
    # Ansprechen der Datenbausteine bzw der einzelnen Datenwörter (in Byte)
    data_x = plc.db_read(2, 8, 2) # Auslesen der Adressen über db_read # Adresse DB2DBW8
    lagerplatz_x = get_int(data_x, 0) # umwandeln der Datentypen in Python Format 
    # ...
    data_y = plc.db_read(2, 2, 2) # int = 2 Byte
    lagerplatz_y = get_int(data_y, 0)

    data_ArtikelNummer = plc.db_read(34, 16, 22)  # STRING[10] = 12 Byte
    Artikelnummer = get_string(data_ArtikelNummer, 0)
    return lagerplatz_x, lagerplatz_y, data_ArtikelNummer
# Funktion zum Schreiben von Werten auf SPS Variablen
def Schreiben(plc, Lagerplatz_x, Lagerplatz_y, Material):

    data_x = bytearray(2) # Festlegen des Array Bereiches 
    set_int(data_x, 0, Lagerplatz_x) # Umwandlung Python Datentyp in Bytes 
    plc.db_write(41, 0, data_x)   # Schreiben mit db_Write äquivalent zum lesen (db_read)
    # ...
    data_y = bytearray(2)
    set_int(data_y, 0, Lagerplatz_y)
    plc.db_write(41, 2, data_y)   # Byte 2

    #data_Barcode = bytearray(22)
    #set_int(data_Barcode, 0, Barcode)
    #plc.db_write(41, , data_Barcode)
    print(Material)
    data_Material = bytearray(22)
    set_string(data_Material, 0, Material,20)
    plc.db_write(41, 6, data_Material)   # Byte 2

    