"""
Calcul volumul unei sfere
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


def calculeaza_volum_sfera(raza):
    volum = (4/3) * math.pi * raza ** 3
    return volum


# Exemplu de utilizare
raza = 5
volum = calculeaza_volum_sfera(raza)
print(f"Volumul sferei cu raza {raza} este: {volum}")

# generare imagine 3D


def plot_sphere(rotation_angle_x, rotation_angle_y, rotation_angle_z, scaling_factor):
    # Generează coordonatele punctelor pe sferă
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(theta), np.sin(phi))
    y = np.outer(np.sin(theta), np.sin(phi))
    z = np.outer(np.ones(np.size(theta)), np.cos(phi))

    # Creează o figură tridimensională
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Plotează sfera
    ax.plot_surface(x, y, z, color='b', alpha=0.5)

    # Rotirea și scalarea sferii
    ax.view_init(rotation_angle_x, rotation_angle_y)
    ax.set_xlim([-scaling_factor, scaling_factor])
    ax.set_ylim([-scaling_factor, scaling_factor])
    ax.set_zlim([-scaling_factor, scaling_factor])

    # Etichetele axelor
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Titlul figurii
    ax.set_title('Sfera Interactivă')

    # Afișează sfera
    plt.show()


# Creează interfața grafică interactivă
interactive_plot = interactive(plot_sphere,
                               rotation_angle_x=widgets.IntSlider(min=0, max=360, step=1, value=10),
                               rotation_angle_y=widgets.IntSlider(min=0, max=360, step=1, value=10),
                               rotation_angle_z=widgets.IntSlider(min=0, max=360, step=1, value=10),
                               scaling_factor=widgets.FloatSlider(min=1, max=10, step=0.1, value=5))
