"""
Calculul ariei unei forme geometrice depinde de tipul formei.
"""
import math

def calculeaza_aria(forma, **parametri):
    if forma == "patrat":
        latura = parametri.get("latura")
        return latura ** 2
    elif forma == "dreptunghi":
        lungime = parametri.get("lungime")
        latime = parametri.get("latime")
        return lungime * latime
    elif forma == "triunghi":
        baza = parametri.get("baza")
        inaltime = parametri.get("inaltime")
        return 0.5 * baza * inaltime
    elif forma == "cerc":
        raza = parametri.get("raza")
        return math.pi * (raza ** 2)
    else:
        return None

# Exemple de utilizare
print(f"Aria pătratului este: {calculeaza_aria('patrat', latura=25)}")
print(f"Aria dreptunghiului este: {calculeaza_aria('dreptunghi', lungime=7, latime=4)}")
print(f"Aria triunghiului este: {calculeaza_aria('triunghi', baza=6, inaltime=3)}")
print(f"Aria cercului este: {calculeaza_aria('cerc', raza=5)}")
