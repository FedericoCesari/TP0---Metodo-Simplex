# Agrega la ecuacion a maximizar a la matriz
def new_maxfunct(num_variables, num_restricciones):
    maximizar = []
    print("Ingrese el valor de las variables")
    for i in range(num_variables):
        valor = input(f"X{i + 1}: ")

        if valor.isdigit():
            valor = int(valor) * -1
            maximizar.append(valor)
        else:
            print("La variable debe tener un valor numerico")
            i -= 1
            continue

# Agrego un '0' por restriccion y uno por la disponibilidad.
    for i in range(num_restricciones + 1):
        maximizar.append(0)
    print(f"Funcion a maximizar: {maximizar}", "\n")

    return maximizar


# Agrega las restricciones a la matriz
def create_restriction(simplex, num_variables, num_restricciones):
    for i in range(num_restricciones):
        restriccion = []

        print("Ingrese el valor de las variables de restricción")
        for variable in range(num_variables):
            valor = input(f"X{variable + 1}: ")

            if valor.isdigit():
                valor = int(valor)
                restriccion.append(valor)
            else:
                print("La variable debe tener un valor numerico")
                variable -= 1
                continue

        for j in range(num_restricciones):  # Agrego un '0' por restriccion.
            restriccion.append(0)

# Agrego la variable de Holguera a la restriccion actual.
        restriccion[num_variables + i] = 1

        valor = input("Disponibilidad del recurso: ")

        if valor.isdigit():
            valor = int(valor)
            restriccion.append(valor)
        else:
            print("La disponibilidad debe tener un valor numerico")
            variable -= 1
            continue
        print(f"Restriccion {i + 1}: {restriccion}", "\n")

        simplex.append(restriccion)
    return
