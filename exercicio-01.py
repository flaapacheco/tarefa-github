# Exercício 01 - Manuseando séries temporais

# Calcular a distância euclidiana entre as séries

import numpy as np

s1 = np.array([168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 323, 106, 1055, 170])

s2 = np.array([168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 180, 106, 1055, 200])

diferenca = s1 - s2

quad_dif = diferenca**2

soma = np.sum(quad_dif)

raiz_quad = np.sqrt(soma)

print('Distância euclidiana:\n',int(raiz_quad))

# Calcular a série temporal com os valores médios entre s1 e s2

media = np.mean(np.array([s1,s2]), axis =0)
print('Média:\n', media)

# Calcular a série temporal com os valores máximos de cada instante entre s1 e s2

maximo = np.maximum(s1,s2)
print('Máximo:\n', maximo)

# Calcular a série temporal com os valores mínimos de cada instante entre s1 e s2

minimo = np.minimum(s1,s2)
print('Mínimo:\n', minimo)