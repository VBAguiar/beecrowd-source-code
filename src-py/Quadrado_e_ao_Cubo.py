n = int(input())
base = 1

for c in range(0, n):
	num = base
	while True:
		print(num, end=' ')
		print(pow(num, 2), end=' ')
		print(pow(num, 3), end='')
		print()
		break
	base += 1
