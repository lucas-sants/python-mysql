#Reduce function
from functools import reduce

def sum(x, y):
	return x+y

list1 = [1, 3, 5, 10, 20]

sum = reduce(sum, list1)
print(sum)