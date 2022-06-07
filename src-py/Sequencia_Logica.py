n = int(input())
num = 1
cont = 0
for c in range(0, n):	
	while True:
		print(f'{num} {num * num} {num * num * num}')
		cont += 1
		if cont == 1:
			print(f'{num} {num * num + 1} {num * num * num + 1}')
			break
	cont = 0 
	num += 1

