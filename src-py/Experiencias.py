n = int(input())

animais = {'ratos': [], 'sapo': [], 'coelhos': []}
total = 0

for c in range(0, n):
	animal = str(input())
	animalsplit = animal.split()
	
	if animalsplit[1].upper() == 'R':
		animais['ratos'].append(int(animalsplit[0]))
		
	elif animalsplit[1].upper() == 'S':
		animais['sapo'].append(int(animalsplit[0]))
		
	else: 
		animais['coelhos'].append(int(animalsplit[0]))
	
	total += int(animalsplit[0])
	
animais['total'] = total 
x = int(sum(animais["coelhos"]))*100
y = int(sum(animais["ratos"]))*100
z = int(sum(animais["sapo"]))*100

print(f'Total: {animais["total"]} cobaias')
print(f'Total de coelhos: {sum(animais["coelhos"])}')
print(f'Total de ratos: {sum(animais["ratos"])}')
print(f'Total de sapos: {sum(animais["sapo"])}')
print(f'Percentual de coelhos: {x/animais["total"]:.2f} %')
print(f'Percentual de ratos: {y/animais["total"]:.2f} %')
print(f'Percentual de sapos: {z/animais["total"]:.2f} %')
