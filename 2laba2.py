def division235 (spisok):
	d2 = []
	d3 = []
	d5 = []
	for i in spisok:
		if i % 2 == 0: d2.append(i)
		if i % 3 == 0: d3.append(i)
		if i % 5 == 0: d5.append(i)
	return [d2, d3, d5]

x = division235([int(j) for j in input('Введите список: ').split()])
print(x)