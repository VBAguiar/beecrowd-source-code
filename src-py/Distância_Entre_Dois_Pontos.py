from math import sqrt

n1 = list(map(float, input().split()))
n2 = list(map(float, input().split()))

x1, y1 = n1[0], n1[1]
x2, y2 = n2[0], n2[1]


formula = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f'{formula:.4f}')
