# Exercício 03 - Gráfico de distribuição população masculina por grupo de idade - Barras horizontais

import matplotlib.pyplot as plt

grupo = ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 24', '25 a 29', '30 a 34',
         '35 a 39', '40 a 44', '45 a 49', '50 a 54', '55 a 59', '60 a 64', '65 a 69',
         '70 a 74', '75 a 79', '80 a 84', '85 a 89', '90 a 94', '95 a 99', '>= 100']

pop_masc_2010 = [7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014,
                 4834995, 3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247]

plt.figure(figsize=(8, 6))

plt.barh(grupo, pop_masc_2010, align='center',color='Darkturquoise')

plt.title("População masculina no Brasil por faixa etária (2010)")

plt.xlabel("População")

plt.ylabel("Faixa etária (anos)")

plt.grid(b=True, color='gray', linestyle=':', linewidth=0.5)

plt.show()