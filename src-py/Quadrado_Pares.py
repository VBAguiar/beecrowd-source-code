n = int(input())

for c in range(1, n+ 1, 1):
	if c % 2 == 0:
		print(f'{c}^2 = {pow(c, 2)}')
