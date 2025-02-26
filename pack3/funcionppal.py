import pandas as pd


import random


def ndfaleatorio():


    numero_aleatorio = random.randint(10, 30)  # Número entre 1 y 100 (ambos incluidos)
    print(numero_aleatorio) 


    # Crear un DataFrame
    data = {
        "Categoría": ["A", "B", "C", "D"],
        "Cantidad": [numero_aleatorio, 2, 3, 4]
    }
    df = pd.DataFrame(data)


    print(df["Cantidad"].sum())


    df = pd.DataFrame(data)
    # Mostrar el DataFrame
    return(f"SUMA columna {df["Cantidad"].sum()}")

if __name__ == "__main__":

    print("Suma de la columna:  ", ndfaleatorio())
    print("Ejecucion desde el sistema")