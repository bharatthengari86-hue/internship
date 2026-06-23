my_list=[10,20,30,40,50]
print(my_list[2])
print("lenth of list=",len(my_list))
if not my_list:
    print("list is empty")
else:
    print("list is not empty")


y_list=[10,20,30,40,50]
print(y_list.insert(1,200))
print(y_list)
y_list.append(600)
print(y_list)
y_list.insert(2,300)
print(y_list)
y_list.remove(600)
print(y_list)
y_list.pop(0)
print(y_list)


my_list=[10,20,30,40,50]
total=sum(my_list)
average=total/len(my_list)
print("sum=",total)
print("average=",average)



a=[8,2,15,1,9]
print("smallest number:=",min(a))
print("largest number=",max(a)) 

sports=["cricket","football","hockey","football","tennis"]
print("number of accurance of fotball=",sports.count("football"))


list_a=[1,2]
list_b=[3,4]
list_a.extend(list_b)
print(list_a)


list1=[10,20,[300,400,[5000,6000],500],30,40]
list1[2][2].append(7000)
print(list1)


num=[23,34,"hello",32,56]
b=len(num)
print("total items in list=",b) 

num=[23,34,"hello",32,56]
print("reverse list=",num[::-1])


list1=[5,10,15,20,25,50,20]
print(list1)
print(20 in list1)
list1.insert(3,200)
print(list1)
