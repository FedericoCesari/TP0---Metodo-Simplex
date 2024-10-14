import numpy as np
import pandas as pd
matrices_generadas=[]
def save_matrices_to_csv(matrices_generadas, salidas):
    with open('salidas.csv', 'w', newline='') as f:
        for index, matrix in enumerate(matrices_generadas):
            df = pd.DataFrame(matrix)
            df.index.name = 'Fila'
            df.columns.name = 'Columna'
            df.to_csv(f, header=True, index=True)
            f.write('\n')  # Añadir una línea en blanco entre matrices