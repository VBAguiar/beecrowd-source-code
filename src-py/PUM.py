n = int(input())
num = 1

for c in range(0, n):
	linha = 0
	while True: 
		if linha >= 3:
			print("PUM")
			num += 1
			break
		
		print(num, end=' ')
		num += 1
		linha += 1
	linha = 0
