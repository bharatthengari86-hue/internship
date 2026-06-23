#check whether two number are equal
a=6
b=4
print("a==b :",a==b)


 #find the larger number
c=int(input("enter 1st number:-"))
d=int(input("enter 2nd number:-"))
e=int(input("enter 3rd number:-"))
if c>d & c>e:
    print(c," is greater")
elif d>e & c<d:
    print(d," is greater")
else:
    print(e," is greater")

 #check pass fail(pass marks=40)
m1=int(input("enter marks of subject 1:"))
m2=int(input("enter marks of subject 2:"))
m3=int(input("enter marks of subject 3:"))
m4=int(input("enter marks of subject 4:"))
m5=int(input("enter marks of subject 5:"))
total=m1+m2+m3+m4+m5
per=total/5
print("total=",total)
print("percentage=",per)
if(per>=75):
    print("first class with distinction")
elif(per<75 & per>65):
    print("first class")
elif(per>50 & per<65):
    print("second class")
else:
    print("fail")



#check voting eligibility(age>=18)
age=int(input("enter the age:- "))
if(age>=18):
    print("person is eligible for voting")
else:
    print("person is not eligible for voting")



