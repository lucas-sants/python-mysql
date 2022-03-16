# -*- coding: utf-8 -*-

#List of strings
list1 = ["apple", "banana", "orange"]

#List of numbers
list2 = [10, 20, 30]

#List of differents types
list3 = ["apple", 1, 5.90, True]

#Print the especific position of list
print(list1[0])

#Printing itens of list 
for item in list2:
	print(item)

#Check size of list
sizeOfList = len(list1)
print(sizeOfList)

#Add elements on list
list1.append("lemon")
print(list1)

#Verify if item exist on list
if 30 in list2:
	print("30 exist on list")

#Delete item of list
#On this example, delete items after item 2
del list1[2:]
print(list1)
#Delete this all list
del list1[:] 

#Sort/order list
list4 = [124,54,12,1,6,90,43,23,7]
list4.sort()
print(list4)
#Sort descending
list4.sort(reverse=True)
print(list4)
#Inverse list
list4.reverse()







