#1
""" while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Thank You")
            break

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Addition =", a + b)

        elif choice == 2:
            print("Subtraction =", a - b)

        elif choice == 3:
            print("Multiplication =", a * b)

        elif choice == 4:
            print("Division =", a / b)

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter integer only")

    except ZeroDivisionError:
        print("Cannot divide by zero")

 """


""" #2
def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Invalid Index"

numbers = [10, 20, 30, 40]
print(get_element(numbers, 2))  
print(get_element(numbers, 5))   """



""" #3
def get_value(dict1,key):
    try:
        return dict1[key]
    except KeyError:
        print("particular key not found")
    
dict1={"name":"bharat","age":17,"address":"chandrapur"}
print(get_value(dict1,"name"))
print(get_value(dict1,"city"))
 """


""" #4
while True:
    try:
        a=int(input("enter value:-"))
        if a==int(a):
            break
        
    except ValueError:
        print("please enter valid integer")
    
 """


#5
try:
    print("1. Value Error")
    num = int(input("Enter a number: "))

    print("2. Type Error")
    result = num + "10"

    print("3. Key Error")
    d = {"name": "Bharat"}
    print(d["age"])

    print("4. Index Error")
    l = [10, 20, 30]
    print(l[5])

    print("5. Zero Division Error")
    print(10 / 0)

except ValueError:
    print("Value Error: Invalid number entered")

except TypeError:
    print("Type Error: Different data types cannot be added")

except KeyError:
    print("Key Error: Key not found in dictionary")

except IndexError:
    print("Index Error: List index out of range")

except ZeroDivisionError:
    print("Zero Division Error: Cannot divide by zero")

