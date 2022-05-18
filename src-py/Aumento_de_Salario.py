salario = float(input())

if salario > 2000.00:
	div = 4
	percetual = salario * (div/100)

elif salario <= 2000.00 and salario >= 1200.01:
	div = 7
	percetual = salario * (div/100)
	
elif salario <= 1200.00 and salario >= 800.01:
	div = 10
	percetual = salario * (div/100)
	
elif salario <= 800.00 and salario >= 400.01:
	div = 12
	percetual = salario * (div/100)
	
else: 
	div = 15
	percetual = salario * (div/100)

print(f'Novo salario: {salario + percetual:.2f}')
print(f'Reajuste ganho: {percetual:.2f}')
print(f'Em percentual: {div} %')
