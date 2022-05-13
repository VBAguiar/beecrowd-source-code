dias = int(input())

ano, dias = divmod(dias, 365)
meses, dias = divmod(dias, 30)

print(f'{ano:.0f} ano(s)')
print(f'{meses:.0f} mes(es)')
print(f'{dias:.0f} dia(s)')
