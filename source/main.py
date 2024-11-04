import matrices
import resolucionmatrices
import archivos
import matricessalida
import numpy as np
from colorama import Style

print(f"{Style.BRIGHT}Bienvenido al sistema de resolución SIMPLEX\n")
print("Para empezar, elija una de las siguientes opciones:\n")
print("[1] Carga manual")
print("[2] Carga por archivo")
version_simplex = 0

while version_simplex not in (1, 2):
    try:
        version_simplex = int(input(f"Ingrese una opción: "))
        if version_simplex not in (1, 2):
            print("Valor no válido, vuelva a intentarlo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

if version_simplex == 1:

    num_variables = int(input(f"{Style.BRIGHT}Ingrese numero de variables: "))
    num_restricciones = int(input("Ingrese numero de restricciones: "))
    print("")

    simplex = []

    simplex.append(matrices.new_maxfunct(num_variables, num_restricciones))
    matrices.create_restriction(simplex, num_variables, num_restricciones)

    original = simplex  # Guardo la matriz con la que se va a trabajar
    for i in range(len(simplex)):
        print(f"{Style.BRIGHT}{simplex[i]}")

    # Inicializar la matriz simplex
    matricessalida.matrices_generadas.append(np.array(simplex))

    resolucionmatrices.maximizacion(simplex, matricessalida.matrices_generadas)

    # Guarda las matrices en un archivo CSV
    matricessalida.save_matrices_to_csv(matricessalida.matrices_generadas, 'salidas.csv')
    print("Matrices guardadas en 'salidas.csv'")


elif version_simplex == 2:
    directorio = "../Archivos Matrices"

    lista_archivos = archivos.listar_archivos_txt(directorio)
    seleccion = archivos.seleccionar_archivo(lista_archivos)
    ruta = directorio + "/" + seleccion
    simplex = archivos.cargar_matriz_desde_archivo(ruta)

    original = simplex  # Guardo la matriz con la que se va a trabajar
    for i in range(len(simplex)):
        print(simplex[i])

    matricessalida.matrices_generadas.append(np.array(simplex))

    resolucionmatrices.maximizacion(simplex, matricessalida.matrices_generadas)

    matricessalida.save_matrices_to_csv(matricessalida.matrices_generadas, 'salidas.csv')
    print("Matrices guardadas en 'salidas.csv'")


