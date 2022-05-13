n = list(map(int, input().split()))

A, B, C = n[0], n[1], n[2]

MaiorAB = (abs(A - B) + A + B) // 2
MaiorAC = (abs(A - C) + A + C) // 2

if MaiorAB >= MaiorAC:
	Maior = MaiorAB
else:
	Maior = MaiorAC
print(f'{Maior} eh o maior')
