# -*- coding: utf-8 -*-

#Examples of Dictionary
#Estructure: dictionary = {"key":"value"}

dictionary1 = {"fruit":"apple", "vehicle":"car", "animal":"dog"} 
print("To print the element, pass the key and its value will appear in print") 
print(dictionary1["fruit"])
print("------------------------------------------------\n\n")

print("Command for with dictionary")
for key in dictionary1:
	print(key+" - "+dictionary1[key])
print("------------------------------------------------\n\n")

print("Convert and print dictionary in format of tuple")
for i in dictionary1.items():
	print(i)
print("------------------------------------------------\n\n")

print("Return the values of dictionary")
for i in dictionary1.values():
	print(i)
print("------------------------------------------------\n\n")

print("Return the keys of dictionary")
for i in dictionary1.items():
	print(i)
print("------------------------------------------------\n\n")



