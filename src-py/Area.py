inputC = list(map(float, input().split()))

A, B, C, PI = inputC[0], inputC[1], inputC[2], 3.14159
tr = A * C / 2
ac = PI * pow(C, 2)
t = (A + B) * C / 2
q = pow(B, 2)
r = A * B
print(f'TRIANGULO: {tr:.3f}')
print(f'CIRCULO: {ac:.3f}')
print(f'TRAPEZIO: {t:.3f}')
print(f'QUADRADO: {q:.3f}')
print(f'RETANGULO: {r:.3f}')
