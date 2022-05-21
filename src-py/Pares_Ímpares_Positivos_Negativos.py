contPar = 0
contImpares = 0
contPositivos = 0
contNegativos = 0
lista = []

for c in range(1, 6):
	n = int(input()); lista.append(n)

for n in lista:
	if n >= 1:
		contPositivos += 1
	elif n < 0:
		contNegativos += 1
	
	if n % 2 == 0:
		contPar += 1
	else:
		contImpares += 1

print(f'{contPar} valor(es) par(es)')
print(f'{contImpares} valor(es) impar(es)')
print(f'{contPositivos} valor(es) positivo(s)')
print(f'{contNegativos} valor(es) negativo(s)')
