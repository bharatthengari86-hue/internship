#Basic Level

""" #1
def add_numbers(a,b):
    return a+b

sum=add_numbers(5,2)
print("sum=",sum) """


""" #2
def is_even(num):
    if num%2==0:
       print("even")
    else:
        print("odd")

is_even(5) """


""" #3
def find_square(n):
    return n*n

num=int(input("enter number:-"))
square=find_square(num)
print("square=",square) """


""" #4
def greet(name):
    print("hello",name)

a=input("enter name:-")
greet(a) """


""" #5
def max_of_two(a,b):
    if a>b:
        print(a,"is greater")
    else:
        print(b,"is greater")

a,b=map(int,input("enter two number").split())
max_of_two(a,b) """



#intermediate Level

""" #6
def factorial(n):
    i=n
    fact=1
    while i>0:
        fact*=i
        i-=1
    return fact

num=int(input("enter a number:-"))
f=factorial(num)
print("factorial of ",num,"is =",f) """



""" #7
def count_vowels(s):
    count=0
    for i in s:
        if i in "aeiouAEIOU":
            count+=1
    return count
    
string=input("enter a string:-")
v=count_vowels(string)
print("number of vower in ",string,"=",v)
 """


""" #8
def reverse_string(s):
    return s[::-1]

a=input("enter a string:-")
reverse=reverse_string(a)
print("reverse of ",a,"=",reverse) """



""" #9
def check_prime(n):
    if n<=1:
        print(n,"is not prime number")
        return
    else:
        for i in range(2,n):
            if i%2==0:
                print(n,"is not prime number")
                break
            else:
                print(n,"is prime number")

a=int(input("enter a number:-"))
check_prime(a) """


""" #10
def sum_list(lst):
    return sum(lst)

b=[1,2,3,4,5,6,7,8,9,10]
addition=sum_list(b)
print("sum of",b,"is =",addition)
 """


#List and string based

""" #11
def find_max(lst):
    return max(lst)

b=[55,32,78,59,25]
maxium=find_max(b)
print("maxium from ",b,"=",maxium) """



""" #12
def remove_duplicates(lst):
    return set(lst)

c=[10,56,10,89,73,89,5,1,5]
print("original list=",c)
duplicate=list(remove_duplicates(c))
print("after removing duplicates from list=",duplicate)
 """


""" #13
def word_count(sentence):
    count=0
    for i in sentence:
        count+=1
    return count

sentence=input("enter a sentence:-")
s=word_count(sentence)
print("total words in sentence=",s) """


""" #14
def palindrome(s):
    if s==s[::-1]:
        print(s,"is palindrome")
    else:
        print(s,"is not palindrome")

text=input("enter a string:-")
palindrome(text)
 """


#15
""" def common_element(list1,list2):
    common=[]
    for i in list1:
        if i in list2:
            common.append(i)
    return common

a=[10,20,30,40,50]
b=[20,10,30,50,15]
print("list1=",a)
print("list 2=",b)
c=common_element(a,b)
print("common element=",c) """


#Advanced Level

""" #16
def calculator(a,b,choice):
    if choice==1:
        print("addition=",a+b)
    elif choice==2:
        print("substraction=",a-b)
    elif choice==3:
        print("mutliplication=",a*b)
    elif choice==4:
        print("division=",a/b)
    else:
        print("invali choice")

print("* calculator *")
print("1.addition")
print("2.substration")
print("3.multiplication")
print("4.division")
a,b=map(int,input("enter two number:-").split())
choice=int(input("enetr your choice:-"))
calculator(a,b,choice)
 """


""" #17
def fibonacii(pos):
    no1=0
    no2=1
    count=0
    while count<pos:
        print(no1)
        no3=no1+no2
        no1=no2
        no2=no3
        count+=1

pos=int(input(("enter a position:-")))
c=fibonacii(pos) """


""" #18
def char_frequency(n,char):
        return n.count(char)

a=input("enter a string:-")
char=input("enter characte to count:-")
c=char_frequency(a,char)  
print("frequency of",char,"is=",c)   


 """


""" #19
def is_amatrong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10      
        sum = sum + digit**3  
        temp = temp // 10      
    if sum == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

num = int(input("Enter a number: "))
is_amatrong(num) """


""" #20
def sort_dict_by_value(d):
    values = list(d.values())
    values.sort()
    for v in values:
        for key in d:
            if d[key] == v:
                print(key, ":", v)

data = {
    "A": 50,
    "B": 20,
    "C": 30
}
sort_dict_by_value(data) """


""" #21
def password_strength(pwd):
    if len(pwd)>=8 and "@"in pwd:
        print("password set succesfully")
    else:
        print("password is week ! password atlist contain minium 8 character and special symbol")

text=input("enter a strong password:-")
password_strength(text) """


""" #22
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD =", gcd(num1, num2)) """


""" #23
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print(s1,",",s2,","," are anagrams")
    else:
        print(s1,",",s2,",","are not anagrams")

s1,s2 = input("enter Two strings:-").split()
anagram(s1,s2)
 """

#24
def decimal_to_binary(n):
    binary=""
    while n>0:
        remainder=n%2
        binary=str(remainder)+binary
        n=n//2
    return binary

num=int(input("enter any decimal number:-"))
c=decimal_to_binary(num)
print("binary of ",num,"is =",c)


#25
def flatten_nested_list(lst):
    result = []

    for item in lst:
        if type(item) == list:
            for x in item:
                result.append(x)
        else:
            result.append(item)
    return result

data = [1, [2, 3], [4, 5], 6]
print(flatten_nested_list(data))
    
    