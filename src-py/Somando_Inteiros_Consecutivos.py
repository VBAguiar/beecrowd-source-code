linha = list(map(int, input().split()))
listnum = []

for c in linha:
	if c >= 1:
		listnum.append(c)

a, n = listnum[0], listnum[1] 
soma = 0

for c in range(1, n+1):
	soma += a
	a += 1

print(soma)
