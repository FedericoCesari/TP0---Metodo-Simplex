import matrices
import resolucionmatrices
import archivos

print("Bienvenido al sistema de resolución SIMPLEX\n")
print("Para empezar, elija una de las siguientes opciones:\n")
version_simplex = int(input(" si desea ingresar las variables manualmente ingrese 1:\n Si desea ingresar la matriz desde un archivo .txt ingrese 2:\n "))

if version_simplex == 1:

    num_variables = int(input("Ingrese numero de variables: "))
    num_restricciones = int(input("Ingrese numero de restricciones: "))
    print("")

    simplex = []

    simplex.append(matrices.new_maxfunct(num_variables, num_restricciones))
    matrices.create_restriction(simplex, num_variables, num_restricciones)

    original = simplex  # Guardo la matriz con la que se va a trabajar
    for i in range(len(simplex)):
        print(simplex[i])

    resolucionmatrices.maximizacion(simplex)

elif version_simplex == 2:
    directorio = "Archivos Matrices"

    lista_archivos = archivos.listar_archivos_txt(directorio)
    seleccion = archivos.seleccionar_archivo(lista_archivos)
    ruta = directorio + "/" + seleccion
    simplex = archivos.cargar_matriz_desde_archivo(ruta)

    original = simplex  # Guardo la matriz con la que se va a trabajar
    for i in range(len(simplex)):
        print(simplex[i])

    resolucionmatrices.maximizacion(simplex)

else:
    version_simplex = int(input("Valor ingresado no válido, vuelva a intentarlo"))


