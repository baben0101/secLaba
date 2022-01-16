def backnum (x):
	neg = x < 0
	if neg:
		x *= -1
	y = 0
	while x > 0:
		z = x % 10
		y = y * 10 + z
		x = x // 10
	if neg:
		y *= -1
	return y 
print (backnum(int(input("Введите число: "))))