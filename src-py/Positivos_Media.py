lista = []
listaPositivos = []
cont = 0

for c in range(0, 6):
	n = float(input()); lista.append(n)
	n = None

for c in lista:
	if c >= 1:
		cont += 1
		listaPositivos.append(c)
print(f'{cont} valores positivos')
print(f'{sum(listaPositivos) / len(listaPositivos):.1f}')
