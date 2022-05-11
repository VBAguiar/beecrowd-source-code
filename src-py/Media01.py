A = float(input(''))
B = float(input(''))


MEDIA = (A * 3.5 + B * 7.5) / (3.5 + 7.5)

if MEDIA >= 10:
	MEDIA = 10
print(f'MEDIA = {MEDIA:.5f}')
