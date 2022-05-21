n = int(input())
lista = []

for x in range(1, n+1):
	n = int(input())
	lista.append(n)

for x in lista:
	if x == 0:
		print('NULL')
	else:
		if x % 2 == 0:
			if x >= 1:
				print('EVEN POSITIVE')
			else:
				print('EVEN NEGATIVE')
		else:
			if x >= 1:
				print('ODD POSITIVE')
			else:
				print('ODD NEGATIVE')
