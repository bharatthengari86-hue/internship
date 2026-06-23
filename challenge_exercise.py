""" # swap two numbers without a third variable
a=14
b=15
a,b=b,a
print("a=",a)
print("b=",b)



# check weather a number is even or odd
a=int(input("enter a number"))
if(a%2==0):
    print(a,"is even number")
else:
    print(a,"is odd number")
 """


#validate a password (minium 8 character and contain @)
password=(input("enter a password :- "))
length=len(password)
if(length >=8 and '@'in password):
    print("password is validate")
else:
    print(" password must be conatin 8, @")



""" #create a login varification system
username=input("enter a username :-")
password=input("enter a password :-")
if(username=="Bharat" and password=="admin@123"):
    print("login succesfull")
else:
    print("login unsuccesfull")



# build a mini ATM program
balance=45000
accno=input("enter account number:-")
password=input("enter a password :-")
if(accno=="123456789" and password=="Bank@123"):
    withdrawl=int(input("enter a amount to withdraw :-"))
    if(withdrawl>balance):
        print("you can not withdrawl amount")
    else:
        balance-=withdrawl
        print("withdrawl succesfull")
        print("Remaining balance=",balance)
else:
    print("invalid details") """