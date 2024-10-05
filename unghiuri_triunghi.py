"""
Calcul unghiuri triunghi
"""

import math


def calculeaza_unghiuri(a, b, c):
    # Calculăm cosinusul fiecărui unghi folosind legea cosinusului
    cos_alpha = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_beta = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_gamma = (a**2 + b**2 - c**2) / (2 * a * b)

    # Convertim cosinusul în unghi folosind funcția arccosinus (acos) din modulul math
    alpha = math.degrees(math.acos(cos_alpha))
    beta = math.degrees(math.acos(cos_beta))
    gamma = math.degrees(math.acos(cos_gamma))

    return alpha, beta, gamma

# Exemplu de utilizare
a = 12
b = 6
c = 6
alpha, beta, gamma = calculeaza_unghiuri(a, b, c)
print(f"Măsura unghiului alpha: {alpha} grade")
print(f"Măsura unghiului beta: {beta} grade")
print(f"Măsura unghiului gamma: {gamma} grade")

# Generare imagine triunghi

import matplotlib.pyplot as plt


def plot_triangle(vertices):
    # Extrage coordonatele x și y ale vârfurilor triunghiului
    x = [vertex[0] for vertex in vertices + [vertices[0]]]
    y = [vertex[1] for vertex in vertices + [vertices[0]]]

    # Plotează liniile triunghiului
    plt.plot(x, y, 'b-')

    # Marchează vârfurile triunghiului
    plt.plot(x, y, 'ro')

    # Adaugă etichete pe vârfuri
    for i, vertex in enumerate(vertices):
        plt.text(vertex[0], vertex[1], f'P{i+1}', fontsize=12)

    # Setează limitele axelor
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)

    # Etichetele axelor
    plt.xlabel('x')
    plt.ylabel('y')

    # Afiseaza imaginea
    plt.title('Triunghi')
    plt.grid(True)
    plt.show()

# Coordonatele vârfurilor triunghiului (P1, P2, P3)
vertices = [(20, 3), (8, 15), (2, 2)]  # P1(0,0), P2(6,0), P3(3,10.3923) (calculat folosind trigonometria)
plot_triangle(vertices)
