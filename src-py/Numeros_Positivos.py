lista = []
cont = 0

for c in range(0, 6):
	n = float(input()); lista.append(n)
	n = None

for c in lista:
	if c >= 1:
		cont += 1

print(f'{cont} valores positivos')
