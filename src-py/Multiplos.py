n = list(map(int, input().split()))

A, B = n[0], n[1]


if A % B == 0 or B % A == 0:
	print('Sao Multiplos')
else:
	print('Nao sao Multiplos')
