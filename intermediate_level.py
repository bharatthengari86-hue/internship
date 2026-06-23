 #create a simple calculator
a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
print("1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("enter the choice which operaton do you want to perform:-"))

match choice:
    case 1:
        print("Addition=",a+b)
    case 2:
        print("Substraction=",a-b)
    case 3:
        print("multiplication=",a*b)
    case 4:
        print("Division=",a*b)
    
    case _:
        print("invalid choice") 


 # check weather a year is leap year
year=int(input("enter the year"))
if(year%4==0):
    print("leap year")
else:
    print("not leap year")



#check divisibility by 3,5,or both
a=int(input("enter a number :-"))
if(a%3==0 and a%5==0):
    print(a,"divisible by 3 and 5")
elif(a%3==0):
    print(a,"divisible by 3")
elif(a%5==0):
    print(a,"divisible by 5")
else:
    print("not divisible by 3 ,5 or both") 



#create a salary bonous calculator
#Example: If salary is ₹30,000 or more, employee gets 10% bonus, otherwise 5% bonus.
salary=float(input("enter a salary"))
if(salary>=30000):
    bonous=salary*0.10
else:
    bonous=salary*0.5

total_salary = salary+bonous
print("bonous=",bonous)
print("total salary=",total_salary)