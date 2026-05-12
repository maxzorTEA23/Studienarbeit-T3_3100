# Hauptprogramm
# Import Bibliotheken
import snap7
from snap7.util import get_bool,set_bool
# Aufruf Schreib und Lese Funktionen
from Einlagern_CSV import Einlagern_CSV
from Auslagern import Auslagern
# Verbindung zur SPS aufbauen
plc = snap7.client.Client()
plc.connect("192.168.0.20",0,1)
# Flag für "Einlagerung erfolgt" ,durch SPS, setzen  

# Scleife in der Prozesse laufen
try:
    while True:
       
        Data_Einlagerung = plc.db_read(41,28,1)
        Einlagerung_erfolgt = get_bool(Data_Einlagerung,0,0)
        # CSV Datei beschreiben nach Einlagerungsprozess
        if Einlagerung_erfolgt:
            Einlagern_CSV(plc)
        # Scanner Flag setzen
        code_Scanner = "1041573"
        # Auslagerungsprozess Auftragsbasiert starten
        if code_Scanner:
            Auslagern(plc,code_Scanner)
            # Flag an SPS senden das Daten überschrieben wurden 
            data_uebernommen = plc.db_read(41,4,1)
            set_bool(data_uebernommen,0,0,True)
            plc.db_write(41, 4, data_uebernommen)

except KeyboardInterrupt:
    print("Programm beendet")

finally:
    # Trennen der SPS Verbindung
    plc.disconnect()
    print("Verbindung getrennt")




