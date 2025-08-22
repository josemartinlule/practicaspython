import random
import matplotlib.pyplot as plt

def simular_galton(n_canicas=3000, niveles=12):
    """
    Simula la máquina de Galton.
    Cada canica pasa por 'niveles' obstáculos donde puede ir a la izquierda o derecha.
    Devuelve una lista con el número de contenedor en el que cayó cada canica.
    """
    resultados = []

    for _ in range(n_canicas):
        contenedor = 0
        for _ in range(niveles):
            # La canica tiene 50% de probabilidad de ir a la derecha
            if random.choice([True, False]):
                contenedor += 1
        resultados.append(contenedor)

    return resultados


def graficar_resultados(resultados, niveles=12):
    """
    Grafica un histograma con los resultados de la simulación.
    """
    plt.hist(resultados, bins=niveles+1, edgecolor='black', align='left')
    plt.title("Simulación de la Máquina de Galton")
    plt.xlabel("Contenedor")
    plt.ylabel("Número de canicas")
    plt.xticks(range(niveles+1))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


if __name__ == "__main__":
    # Parámetros de la simulación
    n_canicas = 3000
    niveles = 12

    # Ejecutar simulación
    resultados = simular_galton(n_canicas, niveles)

    # Graficar resultados
    graficar_resultados(resultados, niveles)