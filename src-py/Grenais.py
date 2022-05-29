

def grenais():
	GRENAIS = EMPATES = INTERVITORIAS = GREMIOVITORIAS = 0
	while True:
		Inter, Gremio = list(map(int, input().split()))
		
		if Inter == Gremio:
			EMPATES += 1
		elif Inter > Gremio:
			INTERVITORIAS += 1
		else:
			GREMIOVITORIAS += 1
		
		GRENAIS += 1
		continuar = ' '
		
		while continuar not in '12':
			continuar = str(input('Novo grenal (1-sim 2-nao)\n')).strip()[0]
		
		if continuar == '2':
			break
	
	lista = [GRENAIS, EMPATES, INTERVITORIAS, GREMIOVITORIAS] 
	return lista

g = grenais()
print(f'{g[0]} grenais')
print(f'Inter:{g[2]}')
print(f'Gremio:{g[3]}')
print(f'Empates:{g[1]}')

if  g[2] > g[3]:
	print('Inter venceu mais')
elif g[3] > g[2]:
	print('Gremio venceu mais')
else:
	print('Nao houve vencedor')
