# Import Bibliotheken
from snap7.util import get_int, get_bool, get_real, get_string, set_int,set_string
# Programm zum Einlesen und Schreiben von und auf die SPS

# Funktion zum Einlesen der Werte von SPS
def Einlesen(plc):
    # Ansprechen der Datenbausteine bzw der einzelnen Datenwörter (in Byte) Einlagern

    data_x_ue = plc.db_read(1, 2, 2) # int = 2 Byte
    lagerplatz_x_ue = get_int(data_x_ue, 0)
    print("X:", lagerplatz_x_ue)
    data_y_ue = plc.db_read(1, 4, 2) # int = 2 Byte
    lagerplatz_y_ue = get_int(data_y_ue, 0)
    print("Y:", lagerplatz_y_ue)
    #TODO umlagern ...

    data_ArtikelNummer = plc.db_read(23, 14844, 22)  # STRING[10] = 12 Byte
    Artikelnummer = get_string(data_ArtikelNummer, 0)
    print(Artikelnummer)
    return lagerplatz_x_ue,lagerplatz_y_ue, Artikelnummer
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

    