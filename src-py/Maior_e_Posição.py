lista = []

for c in range(0, 100):
	n = int(input())
	lista.append(n)
pos = max(lista)
print(max(lista))
print(lista.index(pos) + 1)
