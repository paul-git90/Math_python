"""
Concatenare si calcul geometric
"""
nume = 'Paul'
prenume = 'Eugen'
print(f'Clientul se numeste: {nume + ' ' + prenume}')

# ##################################################### - Perimetrul triunghiului
# Perimetrul unui triunghi - P=a+b+c
latura1 = 5
latura2 = 4
latura3 = 6
perimetru = latura1 + latura2 + latura3
print(f'Perimetrul triunghiului este: {perimetru}')

# ---------------------
def calculeaza_perimetru_triunghi(latura1, latura2, latura3):
    perimetru = latura1 + latura2 + latura3
    return perimetru
# Exemplu de utilizare
latura1 = 5
latura2 = 4
latura3 = 6
perimetru = calculeaza_perimetru_triunghi(latura1, latura2, latura3)
print(f"Perimetrul triunghiului este: {perimetru}")

# ##################################################### - Perimetrul cercului
# Perimetrul unui cerc - P=2×π×r
import math
raza = 5
perimetrul_cerc = 2 * math.pi * raza
print(f'Perimetrul cercului este: {perimetrul_cerc}')

# ---------------------
import math
def calculeaza_perimetru_cerc(raza):
    perimetru = 2 * math.pi * raza
    return perimetru
# Exemplu de utilizare
raza = 5
perimetru = calculeaza_perimetru_cerc(raza)
print(f"Perimetrul cercului cu raza {raza} este: {perimetru}")

# ##################################################### - Perimetrul patratului
# Perimetrul unui patrat - P=4×l
l_patrat = 5
perimetrul = 4 * l_patrat
print(f'Perimetrul patratului este: {perimetrul}')

# ---------------------
def calculeaza_perimetru_patrat(latura):
    perimetru = 4 * latura
    return perimetru
# Exemplu de utilizare
latura = 5
perimetru = calculeaza_perimetru_patrat(latura)
print(f"Perimetrul pătratului cu latura {latura} este: {perimetru}")

# ##################################################### - Aria triunghiului
# Aria triunghiului abc: r^4(s*(s-(a/b/c))
a = 5
b = 6
c = 7
s = (a + b + c) / 2
print(f'Rezultatul semi-perimetrul triunghiului abc: {s}')
aria = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f'Aria triunghiului este: {aria}')

# ---------------------
import math

def calculeaza_aria_triunghi(a, b, c):
    # Calculăm semi-perimetrul
    s = (a + b + c) / 2
    # Calculăm aria folosind formula lui Heron
    aria = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return aria
# Exemplu de utilizare
a = 5
b = 6
c = 7
aria = calculeaza_aria_triunghi(a, b, c)
print(f"Aria triunghiului este: {aria}")

# ##################################################### - Aria cercului
# Aria cercului A=π×r^2
import math
raza = 5
aria_cerc = math.pi * raza ** 2
print(f'Aria cercului este: {aria_cerc}')

# ---------------------
import math

def calculeaza_aria_cerc(raza):
    aria = math.pi * raza ** 2
    return aria

# Exemplu de utilizare
raza = 5
aria = calculeaza_aria_cerc(raza)
print(f"Aria cercului cu raza {raza} este: {aria}")

# ##################################################### - Aria patratului
# Aria patratului aria=l^2
latura = l1 = l2 = l3 = l4 = 5
Aria = latura ** 2
print(f'Aria patratului este: {Aria}')

# ---------------------
def calculeaza_aria_patrat(latura):
    aria = latura ** 2
    return aria

# Exemplu de utilizare
latura = 5
aria = calculeaza_aria_patrat(latura)
print(f"Aria pătratului cu latura {latura} este: {aria}")

# ##################################################### - ex: Dicționar cu argumente
def print_details(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


# Dicționar cu argumente
details = {"name": "Alice", "age": 30, "city": "New York"}
# Decomprimarea dicționarului în argumente cuvinte cheie
print_details(**details)

# ---------------------
def print_my_dict(nume, varsta, oras, masina):
    print(f'Name: {nume}, Age: {varsta}, City: {oras}, Car: {masina}')


my_dict = {'nume': "Florin", 'varsta': 45, 'oras': "Bacau", 'masina': "Opel"}

print_my_dict(**my_dict)



