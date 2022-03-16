#Zip

list1 = [1, 2 , 4, 5,]
list2 = ["apple", "ball", "pencil", "juice", "egg"]
list3 = ["R$2,00", "R$10,00", "R$1,00", "R$3,00", "R$5,00"]

for number, name, value in zip(list1, list2, list3):
	print(number, name, value)