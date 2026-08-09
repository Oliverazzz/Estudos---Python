import numpy as np

A = [8.0, 7.5, 9.0]

B = [5.0, 4.0, 6.0]

C = [10.0, 9.5, 10.0]

D = [7.0, 2.0, 5.0]

matriz = np.vstack((A, B, C, D))

bonus = np.clip(matriz + .5, 0, 10)

medias = bonus.mean(axis=1)

ps = medias >= 7

nps = medias < 7

print(f"""Alunos que passaram: {ps}
Alunos que não passaram: {nps}
Médias: {medias}""")