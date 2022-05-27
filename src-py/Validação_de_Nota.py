lista = []
cont = 0

while True:
	if cont == 2:
		break
		
	nota = float(input())
	
	if nota >= 0 and nota <= 10:
		lista.append(nota)
		cont += 1 
	else:
		print('nota invalida')
soma = 0
for c in lista:
	soma += c

print(f'media = {soma / 2:.2f}')
