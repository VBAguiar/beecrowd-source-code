n = list(map(float, input().split()))

n1, n2, n3, n4 = n[0], n[1], n[2], n[3]

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)
print(f'Media: {media:.1f}')

if media >= 7.0:
	print("Aluno aprovado.")
elif media < 5.0:
	print("Aluno reprovado.")
else:
	print('Aluno em exame.')
	exame = float(input())
	print(f'Nota do exame: {exame}')
	media = (media + exame) / 2
	
	if media >= 5.0:
		print("Aluno aprovado.")
	else:
		print('Aluno reprovado.')
	
	print(f'Media final: {media:.1f}')
	
