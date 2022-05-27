n = int(input())

for c in range(1, n+1):
	x, y = list(map(int, input().split()))
	
	try:
		div = x / y
		print(f'{div:.1f}')
	except Exception:
		print('divisao impossivel')
	
