def notas():
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
	
	continuar = ' '

	while continuar not in '12':
		continuar = str(input('novo calculo (1-sim 2-nao)\n')).strip()[0]

	if continuar == '2':
		exit()

if __name__ == "__main__":
	while True:
		notas()
