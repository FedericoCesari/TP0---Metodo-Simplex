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
    opcion = int(input("Seleccione el número del archivo: ")) - 1

    # Verificar si la opción es válida
    while 0 > opcion > len(archivos):
        print("\n Opción inválida. Intente de nuevo.")
        opcion = int(input("Seleccione el número del archivo: ")) - 1
    else:
        return archivos[opcion]  # Devuelve el nombre del archivo seleccionado
