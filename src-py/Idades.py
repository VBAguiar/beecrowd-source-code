lista = []

while True:
	n = int(input())
	if n < 0:
		break
	
	lista.append(n)

media = sum(lista) / len(lista)


print(f'{media:.2f}')
