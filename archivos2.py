import numpy as np
import os

# Función para mostrar los archivos enumerados y permitir la selección
def seleccionar_archivo(archivos):
    # Pedir al usuario que seleccione un archivo usando un número
    opcion = 0
    
    while opcion not in range(1, len(archivos)+1):
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion not in range(1, len(archivos)+1):
                print("Valor no válido, vuelva a intentarlo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    if opcion in range(1,len(archivos)+1):
        return archivos[opcion-1]

def listar_archivos_txt(directorio):
    archivos = os.listdir(directorio)
    num = 1
    print("\n Lista de Archivos: ")
    for archivo in archivos:
        print(f"[{num}] {archivo}")
        num += 1
    return archivos

def preparar_simplex(filename):
    # Leer el archivo de texto
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Procesar las líneas
    restricciones = []
    for line in lines:
        # Convertir la línea en una lista de números flotantes
        row = list(map(float, line.strip().split()))
        restricciones.append(row)
    
    # Convertimos la lista de restricciones en un array de numpy
    restricciones = np.array(restricciones)
    
    # Obtener la función objetivo (primera fila), que es la primera línea del archivo
    funcion_objetivo = restricciones[0, :-1]
    
    # Añadir ceros para las variables de holgura (una por cada restricción)
    num_restricciones = len(restricciones) - 1  # Número de restricciones
    num_variables = len(funcion_objetivo)        # Número de variables originales
    num_variables_holgura = num_restricciones   # Las variables de holgura

    # La matriz inicial de coeficientes tendrá las variables originales y las de holgura
    matriz = np.zeros((num_restricciones + 1, num_variables + num_variables_holgura + 1))
    
    # Llenamos la matriz con los coeficientes de las restricciones
    for i in range(num_restricciones):
        matriz[i, :num_variables] = restricciones[i + 1, :-1]      # Coeficientes de las restricciones
        matriz[i, num_variables + i] = 1  # Variable de holgura (1 para cada restricción)
        matriz[i, -1] = restricciones[i + 1, -1]  # Resultado de la restricción
    
    # Modificar la función objetivo: convertirla en negativa
    matriz[0, :num_variables] = -funcion_objetivo
    matriz[0, -1] = 0  # La última columna de la función objetivo es 0 (para el valor de Z)
    
    return matriz



