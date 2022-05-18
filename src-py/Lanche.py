n = list(map(int, input().split()))


lanches = {'1': 4.00, '2': 4.50, '3': 5.00, '4': 2.00, '5': 1.50}
lanche, vezes = n[0], n[1]

for k, v in lanches.items():
	if int(k) == lanche:
		print(f'Total: R$ {v*vezes:.2f}')
