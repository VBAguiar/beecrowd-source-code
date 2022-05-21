lista = []
cont = 0

for c in range(1, 6):
	n = int(input()); lista.append(n)

for n in lista:
	if n % 2 ==0:
		cont += 1 

print(f'{cont} valores pares')
