import serial
"""print(serial.VERSION)
ser = serial.Serial(port = 'COM3', baudrate=9600, timeout=1)
print("Warte auf QR-Code...")
while True:
    data = ser.read(1)
    if data:
        print(data.hex(), data)
        # Hier können Sie die Funktion zum Auslagern aufrufen, z.B.:
        # Auslagern(plc, data)
        """

ser = serial.Serial(
    port='COM3',        # anpassen!
    baudrate=19200,
    timeout=1
)

print("Verbindung offen:", ser.is_open)
print("Port:",ser.port)
ser.write(b'LON\r')
print("Daten gesendet, warte auf Antwort...")
#Funktion zum Verarbeiten der Daten vom Scanner
def Scanner():
    while True: 
        data = ser.readline().decode('latin-1', errors='ignore').strip()
        print("Rohdaten:", data)
        data = ''.join(c for c in data if c.isdigit())
        print(data)
        if data:
            print("Empfangene Daten:", data)
            return data
        # Hier können Sie die Funktion zum Auslagern aufrufen, z.B.:
        # Auslagern(plc, data)


