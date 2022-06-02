g = a = d = 0

while True:
	n = int(input())
	
	if n == 1:
		a += 1
	elif n == 2:
		g += 1
	elif n == 3:
		d += 1
	
	if n == 4:
		break

print('MUITO OBRIGADO')
print(f'Alcool: {a}')
print(f'Gasolina: {g}')
print(f'Diesel: {d}')
