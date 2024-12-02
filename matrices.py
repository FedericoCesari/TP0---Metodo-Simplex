# Agrega la ecuacion a maximizar a la matriz
def new_maxfunct(num_variables, num_restricciones):
    maximizar = []
    print("Ingrese el valor de las variables")
    for i in range(num_variables):
        valor_valido = False
        while not valor_valido:
            try:
                valor = int(input(f"X{i + 1}: "))
                if valor > 0:
                    maximizar.append(valor * -1)
                    valor_valido = True
                else:
                    print("El valor debe ser un número entero mayor a 0.")
            except ValueError:
                print("La variable debe tener un valor numérico.")

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
            valor_valido = False  
            while not valor_valido: 
                try:
                    valor = int(input(f"X{variable + 1}: "))
                    if valor >= 0:
                        restriccion.append(valor)
                        valor_valido = True
                    else:
                        print("El valor debe ser un número mayor o igual a 0.")
                except ValueError:
                    print("La variable debe tener un valor numérico.")
        
        for j in range(num_restricciones):  # Agrego un '0' por restricción
            restriccion.append(0)

# Agrego la variable de Holguera a la restriccion actual.
        restriccion[num_variables + i] = 1
        disponibilidad_valida=False
        while not disponibilidad_valida:
            try:
                valor = int(input("Disponibilidad del recurso: "))  
                if valor > 0: 
                    restriccion.append(valor)  
                    disponibilidad_valida=True 
                else:
                    print("El valor debe ser un número mayor a 0.")
                        
            except ValueError:  # Si el valor no es un número entero
                print("La variable debe tener un valor numérico.")

        simplex.append(restriccion)
    return
