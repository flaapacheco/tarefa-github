# Exercício 4 - Distribuição das populações feminina e masculina lado a lado - Barras horizontais

# brasilemsintese.ibge.gov.br/populacao/populacao-por-sexo-e-grupo-de-idade-2010.html
# www.kite.com/python/docs/matplotlib.pyplot.tight_layout

import matplotlib.pyplot as plt

grupo = ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 24', '25 a 29', '30 a 34',
         '35 a 39', '40 a 44', '45 a 49', '50 a 54', '55 a 59', '60 a 64', '65 a 69',
         '70 a 74', '75 a 79', '80 a 84', '85 a 89', '90 a 94', '95 a 99', '>= 100']

pop_fem_2010 = [6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796,
                6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724,
                211594, 66806, 16989]

pop_masc_2010 = [7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014,
                 4834995, 3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247]

plt.figure(figsize=(6, 5))

# lado esquerdo - população feminina
plt.subplot(121)
plt.gca().invert_xaxis() # inverter orientação das barras
plt.barh(grupo, pop_fem_2010, align='center',color='Yellowgreen')
plt.xticks(rotation=90)
plt.xlabel("População feminina")
plt.yticks([]) # desabilitar o rótulo do eixo y

# lado direito - população masculina
plt.subplot(122)
plt.barh(grupo, pop_masc_2010, align='center', color='Darkturquoise')
plt.xlabel("População masculina")
plt.xticks(rotation = 90)

# parte final
plt.tight_layout(pad=2.2) # espaço entre o eixo y e a parte esquerda do gráfico p/ não haver sobreposição
plt.ylabel("Faixa etária (anos)")
plt.suptitle("Pirâmide etária do Brasil (2010)") # título centralizado para os dois axes
plt.show()