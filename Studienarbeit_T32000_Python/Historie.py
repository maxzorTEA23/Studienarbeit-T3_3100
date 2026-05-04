import pandas as pd
from datetime import datetime

def schreibe_historie(aktion, barcode, x, y):

    zeit = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    neuer_eintrag = pd.DataFrame([{
        "Zeit": zeit,
        "Aktion": aktion,
        "Barcode": barcode,
        "Lagerplatz_x": x,
        "Lagerplatz_y": y
    }])

    try:
        historie = pd.read_csv("Historie.csv")
        historie = pd.concat([historie, neuer_eintrag], ignore_index=True)
    except FileNotFoundError:
        historie = neuer_eintrag

    historie.to_csv("Historie.csv", index=False)