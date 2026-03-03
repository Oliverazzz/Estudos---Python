import numpy as np

vendas = np.array([
    [120, 150, 90, 200, 210, 500, 600],  # Semana 1
    [130, 140, 100, 180, 220, 450, 550],  # Semana 2
    [110, 100, 80, 150, 190, 400, 350],  # Semana 3
    [150, 160, 120, 210, 250, 600, 700]  # Semana 4
])

mediafds = np.mean((vendas[:, 5:]), axis=0)  # média das vendas do fds
# matriz atualizada com bônus da black friday
blackfriday = (vendas[:, 4:]) * 1.2
sp = blackfriday > 500
spp = vendas[sp]  # vendas maiores que 500

print(mediafds)
