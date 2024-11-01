sum = 2
max = 4000000
a = 1
b = 2
fibo = 0

while True:
	fibo = a + b
	if fibo >= max:
		break
	if fibo % 2 == 0:
		sum += fibo
	a = b
	b = fibo

print(sum)
