
x = 0
list = list()

def Count(number) :
	for x in range(1, number):
		x += 1
		if x % 3 == 0 or x % 5 == 0 :
			list.append(x)
	print sum(list)