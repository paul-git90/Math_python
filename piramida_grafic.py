"""
piramida calcul si grafic
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def calculeaza_volum_piramida(aria_bazei, inaltimea):
    volum = (1/3) * aria_bazei * inaltimea
    return volum


def plot_piramide(aria_bazei, inaltimea):
    # Definirea vârfurilor piramidei
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, 1]])

    # Definirea fețelor piramidei
    faces = [[vertices[0], vertices[1], vertices[4]],
             [vertices[1], vertices[2], vertices[4]],
             [vertices[2], vertices[3], vertices[4]],
             [vertices[3], vertices[0], vertices[4]],
             [vertices[0], vertices[1], vertices[2], vertices[3]]]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for face in faces:
        x = [point[0] for point in face + [face[0]]]
        y = [point[1] for point in face + [face[0]]]
        z = [point[2] for point in face + [face[0]]]
        ax.plot(x, y, z, 'b-')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    ax.set_title('Piramida')

    plt.show()


# Exemplu de utilizare
aria_bazei = 25
inaltimea = 89
volum = calculeaza_volum_piramida(aria_bazei, inaltimea)
print(f"Volumul piramidei este: {volum}")

plot_piramide(aria_bazei, inaltimea)

