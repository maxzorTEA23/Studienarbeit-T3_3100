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

    data_rfid_1 = plc.db_read(34, 6, 4)  # STRING[10] = 12 Byte
    rfid_code_1 = get_string(data_rfid_1, 0)

    data_rfid_2 = plc.db_read(34, 10, 4)  # STRING[10] = 12 Byte
    rfid_code_2 = get_string(data_rfid_2, 0)
    return lagerplatz_x, lagerplatz_y, rfid_code_1, rfid_code_2
# Funktion zum Schreiben von Werten auf SPS Variablen
def Schreiben(plc, Lagerplatz_x, Lagerplatz_y, Barcode):

    data_x = bytearray(2) # Festlegen des Array Bereiches 
    set_int(data_x, 0, Lagerplatz_x) # Umwandlung Python Datentyp in Bytes 
    plc.db_write(41, 0, data_x)   # Schreiben mit db_Write äquivalent zum lesen (db_read)
    # ...
    data_y = bytearray(2)
    set_int(data_y, 0, Lagerplatz_y)
    plc.db_write(41, 2, data_y)   # Byte 2

    