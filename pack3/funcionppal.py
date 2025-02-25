import pandas as pd


import random

numero_aleatorio = random.randint(10, 30)  # Número entre 1 y 100 (ambos incluidos)
print(numero_aleatorio) 


# Crear un DataFrame
data = {
    "Categoría": ["A", "B", "C", "D"],
    "Cantidad": [numero_aleatorio, 20, 30, 40]
}
df = pd.DataFrame(data)


print(df["Cantidad"].sum())

def ndfaleatorio():

    df = pd.DataFrame(data)
    # Mostrar el DataFrame
    return(df["Cantidad"].sum())

if __name__ == "__main__":
    print("Ejecucion desde el sistema")