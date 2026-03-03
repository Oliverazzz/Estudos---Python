import numpy as np


temp = np.array([2.5, 23.1, 85.0, 22.8, 21.9, 90.0, 23.5])

filtro = temp < 50

arr = temp[filtro]

clear = np.where(temp > 50, (np.mean(arr)), temp)

norm = np.min(clear) / (np.max(clear) - np.min(clear))

print(f"""Análise: {temp}
Filtrado: {arr}
Normalizado: {norm}""")

