# Hauptprogramm
# Import Bibliotheken
import snap7
import time
from snap7.util import get_bool,set_bool, get_int
# Aufruf Schreib und Lese Funktionen
from Einlagern_CSV import Einlesen_CSV
from Auslagern import Auslagern
from Scanner import Scanner 
print("import")
# Verbindung zur SPS aufbauen
plc = snap7.client.Client()
plc.connect("192.168.0.20",0,1)
# Flag für "Einlagerung erfolgt" ,durch SPS, setzen  
letzter_zustand = False
data_quittung = plc.db_read(41,28,1)
print("1")
print(data_quittung)
print("2")
set_bool(data_quittung,0,1, False)

# Scleife in der Prozesse laufen
try:
    while True:
        Data_Lesen = plc.db_read(41,28,1)
        Einlagerung_erfolgt = get_bool(Data_Lesen,0,0)
        Umlagerung_erfolgt = get_bool(Data_Lesen,0,1)

        data_uebernommen = plc.db_read(41,4,1)
        set_bool(data_uebernommen,0,0,False)
        print(Einlagerung_erfolgt)
        # CSV Datei beschreiben nach Einlagerungsprozess
        if (Einlagerung_erfolgt and not letzter_zustand) or (Umlagerung_erfolgt and not letzter_zustand):

            Einlesen_CSV(plc)

            data_quittung = plc.db_read(41,28,1)

            # ✅ Einlagerung quittieren
            if Einlagerung_erfolgt:
                set_bool(data_quittung, 0, 0, True)

            # ✅ Umlagerung quittieren
            if Umlagerung_erfolgt:
                set_bool(data_quittung, 0, 1, True)

            plc.db_write(41,28,data_quittung)

            time.sleep(0.2)

            data_quittung = plc.db_read(41,28,1)

            if Einlagerung_erfolgt:
                set_bool(data_quittung, 0, 0, False)

            if Umlagerung_erfolgt:
                set_bool(data_quittung, 0, 1, False)

            plc.db_write(41,28,data_quittung)
        letzter_zustand = Einlagerung_erfolgt or Umlagerung_erfolgt
        # Scanner Flag setzen
        print("hallo")
        code_Scanner = Scanner()
        print("Gescannt:",code_Scanner )
        #print("roh:",type(code_Scanner))
        time.sleep(2)
        # Auslagerungsprozess Auftragsbasiert starten
        if code_Scanner:
            Auslagern(plc,code_Scanner)
            # Flag an SPS senden das Daten überschrieben wurden 
            print("vor:", list(plc.db_read(41,4,1)))
            data_uebernommen = plc.db_read(41,4,1)
            set_bool(data_uebernommen,0,0,True)
            plc.db_write(41, 4, data_uebernommen)
            print("nach:", list(plc.db_read(41,4,1)))
            time.sleep(2)
            print("2s später:", list(plc.db_read(41,4,1)))
            while get_int(plc.db_read(19,26,2),0) != 9:
                time.sleep(0.05)
            data_uebernommen = plc.db_read(41,4,1)
            set_bool(data_uebernommen,0,0,False)
            plc.db_write(41, 4, data_uebernommen)
            print("SPS Fertig")
            
except KeyboardInterrupt:
    print("Programm beendet")

finally:
    # Trennen der SPS Verbindung
    plc.disconnect()
    print("Verbindung getrennt")




