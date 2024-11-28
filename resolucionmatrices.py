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
        col_variables.append(col)  # Guardo la columna // Numero de variable

        valor = simplex[fila][col]
        # Convierto pivote en 1 y modifico el resto de la fila
        for i in range(len(simplex[fila])):
            # f(x) = x / valor_pivote
            simplex[fila][i] = simplex[fila][i] / valor
        # Convierto numeros superiores e inferiores en 0.
        for i in range(len(simplex)):
            if simplex[i][col] != 0 and i != fila:
                valor = simplex[i][col]
                for j in range(len(simplex[i])):
                    simplex[i][j] = simplex[i][j] - (valor * simplex[fila][j])

        # Guardar la matriz actual
        matricessalida.matrices_generadas.append(np.array(simplex))
        
        print("")
        for i in range(len(simplex)):
            if i != fila:
                print(f"{Style.BRIGHT}{simplex[i]}")
                continue
            fila = "["
            for j in range(len(simplex[i])):
                if j == len(simplex[i])-1:
                    fila = fila + str(simplex[i][j])
                    continue
                if j != col:
                    fila = fila + str(simplex[i][j]) + ", "
                    continue
                pivote = f"{Back.CYAN}{simplex[i][j]}{Back.RESET}, "
                fila += pivote
            fila += "]"
            print(fila)

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
