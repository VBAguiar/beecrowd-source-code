n = list(map(float, input().split()))

A, B, C = n[0], n[1], n[2]
somaDoisLados = A + B + C
trapezio = (A + B) * C / 2

if A < B + C and B < A + C and C < B + A:
	print(f'Perimetro = {somaDoisLados}')
else:
	print(f'Area = {trapezio}')
