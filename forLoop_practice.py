#1
a=int(input("enter a position:-"))
for i in range(1,a+1):
    print(i)


#2
b=int(input("enter the position:-"))
sum=0
for i in range(1,b+1):
    sum=sum+i
    i+=1
print("sum=",sum)


 #3
num=int(input("enter a number:-"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

#4
a=int(input("enter position:-"))
count=0
for i in range(1,a+1):
    if i%2==0:
        count+=1
print("count=",count)


#5
a=int(input("enter a number:-"))
fact=1
for i in range(a,0,-1):
    fact=fact*i
print("factorial=",fact)



#6
b=int(input("enter a number:-"))
for i in range(b,0,-1):
    print(i)


#7
string=input("enter a string:-")
count=0
for i in string:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels=",count)


#8
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


#9
a=[5,90,8,7,20]
max_no=a[0]
for i in a:
    if i>max_no:
        max_no=i
        print("maxium number:-",max_no)


#10
a=int(input("enter a position:" ))
for i in range(1,a+1):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)