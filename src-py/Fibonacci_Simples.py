num = int(input())

fib = 0
for cont in range(1, num-1):
	if fib == 0:
		a = fib
		print(fib, end=' ')
		fib += 1
		print(fib, end=' ')
	
	if cont == num-2:
		print('{}'.format(a + fib))
		break
	else:
		print(a + fib, end=' ')
	temp = a
	a = fib
	fib += temp
