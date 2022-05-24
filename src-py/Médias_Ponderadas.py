from math import prod

n = int(input())
lista = []

for c in range(1, n+1):
	n = list(map(str, input().split()))
	lista.append(n)


media = 2 + 3 + 5
media2 = [2, 3, 5] 
for c in range(0, len(lista)):
	num = 0
	for x in range(0, len(lista[c])):
		num += float(lista[c][x]) * media2[x] 
	print(f'{num / media:.1f}')
	num = 0
