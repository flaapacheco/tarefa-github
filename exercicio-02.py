# Exercício 02 - Gráfico de distribuição população feminina por grupo de idade - Barras verticais

import matplotlib.pyplot as plt

grupo = ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 24', '25 a 29', '30 a 34',
         '35 a 39', '40 a 44', '45 a 49', '50 a 54', '55 a 59', '60 a 64', '65 a 69',
         '70 a 74', '75 a 79', '80 a 84', '85 a 89', '90 a 94', '95 a 99', '>= 100']

pop_fem_2010 = [6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796,
                6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724,
                211594, 66806, 16989] # não pode ter separador com .

plt.figure(figsize=(8, 6)) # primeiro define as configurações do gráfico que vai ser plotado

plt.bar(grupo, pop_fem_2010, align='center', color='Yellowgreen') # conteúdo e formato do gráfico

plt.title("População feminina no Brasil por faixa etária (2010)")

plt.xlabel("Faixa etária (anos)")
plt.xticks(grupo, rotation=90)

plt.ylabel("População")

plt.grid(b=True, color='gray', linestyle=':', linewidth=0.5)

plt.show()