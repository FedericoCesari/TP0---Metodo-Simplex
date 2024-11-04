import matrices
import resolucionmatrices
import matricessalida
import archivos2
import numpy as np


def menu_principal():
    print("Elija una de las siguientes opciones:\n")
    print("[1] Carga manual")
    print("[2] Carga por archivo")
    version_simplex = 0

    while version_simplex not in (1, 2):
        try:
            version_simplex = int(input("Ingrese una opción: "))
            if version_simplex not in (1, 2):
                print("Valor no válido, vuelva a intentarlo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

        if version_simplex == 1:
            ingreso_manual()
        elif version_simplex == 2:
            carga_por_archivo()


def ingreso_manual():
    num_variables = int(input("Ingrese numero de variables: "))
    num_restricciones = int(input("Ingrese numero de restricciones: "))
    print("")

    simplex = []

    simplex.append(matrices.new_maxfunct(num_variables, num_restricciones))
    matrices.create_restriction(simplex, num_variables, num_restricciones)

    original = simplex  # Guardo la matriz con la que se va a trabajar
    for i in range(len(simplex)):
        print(simplex[i])

    # Inicializar la matriz simplex
    matricessalida.matrices_generadas.append(np.array(simplex))

    resolucionmatrices.maximizacion(simplex, matricessalida.matrices_generadas)

    # Al final, guarda las matrices en un archivo CSV
    matricessalida.save_matrices_to_csv(matrices_generadas, 'salidas.csv')
    print("Matrices guardadas en 'salidas.csv'")


def carga_por_archivo():
    directorio = "Archivos Matrices"

    lista_archivos = archivos2.listar_archivos_txt(directorio)
    seleccion = archivos2.seleccionar_archivo(lista_archivos)
    ruta = directorio + "/" + seleccion

    if archivos2.verificacion(ruta):
        simplex = archivos2.preparar_simplex(ruta)

        original = simplex  # Guardo la matriz con la que se va a trabajar
        for i in range(len(simplex)):
            print(simplex[i])

        matricessalida.matrices_generadas.append(np.array(simplex))

        resolucionmatrices.maximizacion(simplex, matricessalida.matrices_generadas)

        matricessalida.save_matrices_to_csv(matricessalida.matrices_generadas, 'salidas.csv')
        print("Matrices guardadas en 'salidas.csv'")
    else:
        print("\nEl archivo ingresado contiene valores no numéricos, verifique el archivo o intentelo con uno diferente\n")
        menu_principal()


print("Bienvenido al sistema de resolución SIMPLEX\n")
menu_principal()
