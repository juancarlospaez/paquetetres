import pandas as pd
import random

def ndfaleatorio():
    numero_aleatorio = random.randint(10, 30)  # Número entre 1 y 100 (ambos incluidos)
    print(numero_aleatorio) 

    # Crear un DataFrame
    data = {"Categoría": ["A", "B", "C", "D"],
            "Cantidad": [numero_aleatorio, 2, 3, 4]
           }

    df = pd.DataFrame(data)
    Variable = df["Cantidad"].sum()

    return(f"SUMA columna {int(Variable)}")

if __name__ == "__main__":

    print("Suma de la columna:  ", ndfaleatorio())
    print("Ejecucion desde el sistema")