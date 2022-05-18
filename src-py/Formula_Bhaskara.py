from math import sqrt

n = list(map(float, input().split()))

a, b, c = n[0], n[1], n[2]

try:
	formula01 = (-b+sqrt(pow(b, 2) - 4*a*c)) / (2*a); formula02 = (-b-sqrt(pow(b, 2) - 4*a*c)) / (2*a)
	print(f'R1 = {formula01:.5f}')
	print(f'R2 = {formula02:.5f}')
except Exception:
	print('Impossivel calcular')
