#GALEASSO FEDERICO 4C 6/10/2022 ESEMPIO BREAK E CONTINUE

import os
def clearScreen():
	os.system("clear")
clearScreen()

contarosso=0
biglie=['rosso', 'giallo', 'giallo', 'rosso', 'rosso', 'giallo']
for b in biglie:
	if b=='rosso':
		continue
	contarosso=contarosso+1
print("Le biglie rosse sono", contarosso)
