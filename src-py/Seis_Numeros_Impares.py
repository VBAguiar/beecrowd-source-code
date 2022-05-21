n = int(input())
	
def gNum(n):
	NUM = []
	for n in range(n, n+12):
		NUM.append(n)
	return NUM

g = gNum(n)

for x in g:
	if x % 2 == 1:
		print(x)
