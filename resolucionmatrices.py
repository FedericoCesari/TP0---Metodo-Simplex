import matricessalida
import numpy as np
from colorama import Fore, Style,Back

def encontrarColPivote(simplex):
    max_negative = 0
    columna = -1
    # Encuentra columna del pivote en la funcion a maximizar.
    for i in range(len(simplex[0])):
        if simplex[0][i] < max_negative:
            max_negative = simplex[0][i]
            columna = i  # Indice valor mas negativo // Columa del pivote
    return columna


def encontrarfilapivote(simplex, columna):
    # Primer valor a comparar para encontrar fila del pivote
    pivote = simplex[1][len(simplex[1]) - 1] / simplex[1][columna]
    # Empiezo en 1 porque la primer fila contiene la funcion a maximizar
    fila = 1
    for i in range(2, len(simplex)):  # Encuentra fila del pivote
        if simplex[i][columna] == 0:
            continue
        valor = simplex[i][len(simplex[i]) - 1] / simplex[i][columna]
        if valor < pivote:
            pivote = valor
            fila = i
    return fila


def maximizacion(simplex, matrices_generadas):
    fila_variables = []
    col_variables = []

    col = encontrarColPivote(simplex)
    fila = encontrarfilapivote(simplex, col)

    while col != -1:
        fila_variables.append(fila)  # Guardo la fila de la variable X
        col_variables.append(col)  # Guardo la columna // Número de variable

        valor = simplex[fila][col]
        # Convierto el pivote en 1 y modifico el resto de la fila
        for i in range(len(simplex[fila])):
            simplex[fila][i] = simplex[fila][i] / valor
        # Convierto números superiores e inferiores en 0.
        for i in range(len(simplex)):
            if simplex[i][col] != 0 and i != fila:
                valor = simplex[i][col]
                for j in range(len(simplex[i])):
                    simplex[i][j] = simplex[i][j] - (valor * simplex[fila][j])

        # Guardo la matriz actual para ir haciendo un seguimiento
        matricessalida.matrices_generadas.append(np.array(simplex))

        print("")

        # Cálculo del ancho máximo de cada columna
        n_columnas = len(simplex[0])
        ancho_columnas = []
        for j in range(n_columnas):
            # Calculo el ancho máximo de cada columna, considerando los valores de la matriz
            max_len = max(len(f"{float(simplex[i][j]):.2f}") for i in range(len(simplex)))
            ancho_columnas.append(max_len)

        # Imprimo la matriz
        for i in range(len(simplex)):
            fila = ""

            # Revisamos si estamos en la fila del pivote
            if i == fila:
                # Si es la fila del pivote, la destaco con color cian
                fila = "["
                for j in range(len(simplex[i])):
                    # Resalto el pivote
                    if j == col:
                        fila += f"{Back.CYAN}{simplex[i][j]:.2f}{Back.RESET}, "
                    else:
                        fila += f"{simplex[i][j]:>{ancho_columnas[j]}.2f}, "
                fila = fila[:-2] + "]"  # Elimino la última coma y cierro el corchete
                print(fila)  # Imprimo la fila del pivote con el resaltado
            else:
                # Si no es la fila del pivote, la imprimo normalmente
                print(
                    f"{Style.BRIGHT}{' '.join([f'{float(x):>{ancho_columnas[j]}.2f}' for j, x in enumerate(simplex[i])])}{Style.RESET_ALL}")

        # Actualizo el pivote para la siguiente iteración
        col = encontrarColPivote(simplex)
        fila = encontrarfilapivote(simplex, col)
        continue

    print("")
    print(f"{Fore.RED}Resultado:")

    for i in range(len(fila_variables)):
        valor = simplex[fila_variables[i]][len(simplex[fila_variables[i]]) - 1]
        variable = col_variables[i] + 1
        print(f"| X{variable}: {round(valor, 3)} |")
    return
