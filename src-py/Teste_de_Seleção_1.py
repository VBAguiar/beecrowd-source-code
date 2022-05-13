n = list(map(int, input().split()))

A, B, C, D = n[0], n[1], n[2], n[3]

if (B > C) and (D > A):
	if (C + D) > (A + B):
		if (C>=0) and (D>=0):
			if A % 2 == 0:
				print('Valores aceitos')
				exit()
print('Valores nao aceitos')
