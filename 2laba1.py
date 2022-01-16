def palindrom (x):
	neg = x < 0
	if neg:
		x *= -1
	z = 0
	y = x
	while x > 0: 
		o = x % 10
		z = z * 10 + o
		x = x // 10
	return z == y
print (palindrom(int(input("Введите число (предоплагаемый палиндром): "))))