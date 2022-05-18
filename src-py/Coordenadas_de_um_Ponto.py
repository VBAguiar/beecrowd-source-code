n = list(map(float, input().split()))

x, y = n[0], n[1]

if x == 0 and y == 0:
	print('Origem')
	exit()

if x == 0:
	print('Eixo Y')

if y == 0:
	print('Eixo X')
	
if x > 0 and y > 0:
	print('Q1')

if x < 0 and y > 0:
	print('Q2') 

if x < 0 and y < 0:
	print('Q3')

if x > 0 and y < 0:
	print('Q4')

