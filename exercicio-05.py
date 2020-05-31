# Exercício 5 - Conjunto de dados apresentado em gráfico informativo usando matplotlib

# Taxa PRODES Amazônia - 2004 a 2019 (km²)

# terrabrasilis.dpi.inpe.br/app/dashboard/deforestation/biomes/legal_amazon/rates

import matplotlib.pyplot as plt

ano = [1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 
       2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
plt.figure(figsize=(8, 6))
plt.bar(ano, [21050, 17770, 13730, 11030, 13786, 14896, 14896, 29059, 18161, 13227, 17383, 17259, 18226,
              18165, 21650, 25396, 27772, 19014, 14286, 11651, 12911, 7464, 7000, 6418, 4571, 5891, 5012, 
              6207, 7893, 6947, 7536, 9762], align='center', color='Navajowhite')

plt.title("Taxa PRODES Amazônia Legal")
plt.xlabel("Ano")
plt.ylabel("Desmatamento (km²)")

plt.show()

