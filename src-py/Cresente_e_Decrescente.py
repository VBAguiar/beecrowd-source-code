lista = []

while True:
	n1, n2 = list(map(int, input().split()))
	
	if n1 == n2:
		break
	lista.append([n1, n2])	

for l in lista:
	n1, n2 = l

	if n1 < n2:
		print('Crescente')
	elif n1 > n2:
		print('Decrescente')
