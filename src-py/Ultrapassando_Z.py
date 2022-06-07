x = int(input())
z = int(input())
cont = 0
soma = x

while z <= x:
	z = int(input())

while True:
	cont += 1
	if soma > z:
		break
	
	x += 1
	soma += x

print(cont) 
