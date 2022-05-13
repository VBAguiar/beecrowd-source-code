segundos = int(input())

horas, segundos = divmod(segundos, 3600)
minutos, segundos = divmod(segundos, 60)

print(f'{horas:.0f}:{minutos:.0f}:{segundos:.0f}')
