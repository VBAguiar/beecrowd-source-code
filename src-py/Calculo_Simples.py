v1 = list(map(str, input().split()))
v2 = list(map(str, input().split()))


VALOR  = (float(v1[1]) * float(v1[2])) + (float(v2[1]) * float(v2[2]))

print(f'VALOR A PAGAR: R$ {VALOR:.2f}')
