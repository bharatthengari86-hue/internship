""" #1
try:
    a=10
    b=0
    c=a/b
    print("division =",c)
except ZeroDivisionError:
    print("can not divisible by 0")
     """


""" #2
try:
    a=int(input("enter value:-"))
    print(a)
except ValueError:
    print("please enter integer number") """


""" #3
try:
    lst=[10,20,30,40,50,60,70,80,90,100]
    print(lst[12])
except IndexError:
    print("particular item is not present at given index") """


""" #5
try:
    employee={"id":1,"name":"bharat"}
    print(employee["city"])
except KeyError:
    print("particular key is not present in given dictonary")

 """



""" #6
try:
    a="bharat"
    b=10
    c=a+b
    print(c)
except TypeError:
    print("cannot add string and integer") """



""" #7
import math
try:
    a=int(input("enter number :-"))
    print("square root=",math.sqrt(a))
except ValueError:
    print("invalid input") 
except:
    print("square root can not be found") """


""" #8
try:
    a=int(input("enter value:-"))
    print(a)
except ValueError:
    print("this conversion is not possible")

 """


""" #9
try:
    a=(1,2,3,4,5)
    print(a[6])
except IndexError:
    print("particular item is not present at given index") """


""" #11
try:
    a=[10,50,80,441,420]
    c=max(a)
    print(c)
except TypeError:
    print("no one larger number")
    

         """


""" #12
try:
    lst=[1,2,3,4,5,6]
    print(lst.remove(8))
except ValueError:
    print("particular element is not present at given index")
 """


""" #13
try:
    a=int(input("enter first number:-"))
    b=int(input("enter second number:-"))
    print("addition=",a+b)
    print("substraction=",a-b)
    print("multiplication=",a*b)
    print("Division=",a/b)
except TypeError:
    print("error is handle here")

except ZeroDivisionError:
    print("cannot divide by zero")
 """


""" #14
try:
    sum=0
    for i in range(5):
        n=int(input("enter a number:-"))
        sum=sum+n
    print("sum=",sum)
except ValueError:
    print("please enter integer value only") """


""" #15
try:
    a=input("enter a string:-")
    c=a[::-1]
    print(c)
except AttributeError:
    print("enter string value only") """


""" #16
try:
    a=int(input("enter length:-"))
    b=int(input("enter breadth:-"))
    area=a*b
    print("area of rectangle=",area)
except ValueError:
    print("please enterb integer value only") """


""" #18
try:
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    mobile = input("Enter Mobile Number: ")

    if age < 18:
        print("Invalid Age")

    elif "@" not in email or "." not in email:
        print("Invalid Email")

    elif len(mobile) != 10 or not mobile.isdigit():
        print("Invalid Mobile Number")

    else:
        print("Registration Successful")

except ValueError:
    print("Invalid Input") """