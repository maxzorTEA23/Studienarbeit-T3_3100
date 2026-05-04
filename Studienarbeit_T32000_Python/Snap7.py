
import snap7
from snap7.util import get_int, get_bool, get_real, get_string, set_int,set_string
def Einlesen(plc,Materialname, Lagerplatz):
    Data = plc.db_read
    Lagerplatz = get_int(Data,0)
    Materialname = get_string(Data,2)
def Schreiben(plc, Materialnummer, Lagerplatz):
    data = bytearray(2)
    set_int(data,0,Materialnummer)
    plc.db_Write
    