
""" #begginear level

 #1
i=1
while i<=10:
    print(i)
    i+=1


#2
i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1


#3
i=1
while i<=50:
    if i%2!=0:
        print(i)
    i+=1

#4
i=1
sum=0
while i<=10:
    sum=sum+i
    i+=1
print("sum=",sum)

#5
a=int(input("enter the number :-"))
i=1
while i<=10:
    print(a*i)
    i+=1
 

 #6
b=int(input("enter a number"))
count=0
while b>0:
    b=b//10
    count=count+1
print("number of digit=",count) 

#7
no=int(input("enter a number:-"))
rev=0
while(no>0):
    digit=no%10
    rev=rev*10+digit
    no=no//10
print("reverse of number:-",rev)


#8
a=int(input("enter a number:-"))
fact=1
i=1
while i<=a:
    fact=fact*i
    i+=1
print("factorial is=",fact)




# imediate level

#1
i=1
while i<=10:
    if i==6:
        break
    else:
        print(i)
        i+=1


#2
i=1
while i<=10:
    if i==5:
       i+=1
       continue
    print(i)
    i+=1



#3
i=1
while i<=20:
    if i%2==0:
       i+=1
       continue
    print(i)
    i+=1



#4
list1=[1,2,3,4,5,6,7,8,9]
num=int(input("enter a number to search:-"))
print(list1)
i=0
while i<len(list1):
    if list1[i]==num:
        print("number found at index",i)
        break
    i+=1
    if i==len(list1):
        print("element not found in ") 


#5
while True:
    num=int(input("enter an number(0 to stop):-"))
    if num==0:
        print("loop stopped")
        break
    print("you enterd ",num)
 """


#6
i=1
while i<=10:
    if(i%3==0):
        pass
    print(i)
    i+=1


""" #7
password="Admin@123"
while True:
    pass1=input("enter password:-")
    if(pass1==password):
        print("you enterd correct password")
        break
    else:
        print("you enterd wrong password")



#8
count=0
while True:
    num=int(input("enter  number (0 for stop) :-"))
    if num==0:
        break
    count=count+1
print("total number enterd =",count)


#9
balance = 10000

while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(amount,"Amount deposited successfully.")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(amount,"withdrawl succefully")
        else:
            print("Insufficient balance ! you can not withdrawl amount")


#10
i = 1
while i <= 10:
    if i == 3:
        pass    # Does nothing
        
    elif i == 5:
        i += 1
        continue  # Skip 5
   
    elif i == 8:
        break      # Stop the loop

    print(i)
    i += 1  """