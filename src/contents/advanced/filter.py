#Filter

def pairs(i):
	if i % 2 == 0:
		return i

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listPairs = filter(pairs, list1)
print(list(listPairs))
