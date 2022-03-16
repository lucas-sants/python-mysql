#Map

#Without Map
def double(x):
	return x*2

value = [1, 2, 3, 4, 5]
print(double(value))

#With Map
def double2(x):
	return x*2

value2 = [1, 2, 3, 4, 5]

doubleValue = map(double2, value2)
doubleValue = list(doubleValue)
print(doubleValue)