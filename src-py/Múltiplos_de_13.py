x = int(input())
y = int(input())

listanum = []

if y < x:
	temp = x
	x = y
	y = temp

for n in range(x, y+1):
	if n % 13 == 0:
		pass
	else:
		listanum.append(n)

print(sum(listanum))
