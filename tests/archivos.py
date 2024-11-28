import os


def cargar_matriz_desde_archivo(ruta_archivo):
    matriz = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Convertir la línea en una lista de floats
            elementos = linea.split()
            fila = []
            for i in range(len(elementos)):
                # Convertir cada elemento a float
                fila.append(float(elementos[i]))
            matriz.append(fila)  # Agregar la fila a la matriz
    return matriz


def listar_archivos_txt(directorio):
    archivos = os.listdir(directorio)
    num = 1
    print("\n Lista de Archivos: ")
    for archivo in archivos:
        print(f"[{num}] {archivo}")
        num += 1
    return archivos


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

    if opcion in range(1, len(archivos)+1):
        return archivos[opcion-1]
