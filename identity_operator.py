# check weather variables refers to the same object
num1=65
num2=78
print(num1,num2)
print("num1 is num2 ",num1 is num2)
print("num1 is not num2 ",num1 is not num2)


#compare two lists using == and is
list1=[10,20,30]
list2=[10,20,30]
print(list1)
print(list2)
print("list1 == list2 ",list1==list2)
print("list1 is list2 ",list1 is list2)