a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))

print("1. Arithmetic Operators")
print("2. Relational Operators")
print("3. Bitwise Operators")
print("4. Logical Operators")
print("5. Assignment Operator")
print("6. Membership Operators")
print("7. Identity Operators")

choice = int(input("Enter your choice (1-7): "))

match choice:

    case 1:
        print("\n* Arithmetic Operators *")
        print("Addition =", a + b)
        print("Subtraction =", a - b)
        print("Multiplication =", a * b)
        print("Division =", a / b)
        print("Floor Division =", a // b)
        print("Modulus =", a % b)
        print("Power =", a ** b)

    case 2:
        print("\n* Relational Operators *")
        print("Greater than =", a > b)
        print("Less than =", a < b)
        print("Less than or equal to =", a <= b)
        print("Greater than or equal to =", a >= b)
        print("Equal to =", a == b)
        print("Not equal to =", a != b)

    case 3:
        print("\n* Bitwise Operators *")
        print("a & b =", a & b)
        print("a | b =", a | b)
        print("a ^ b =", a ^ b)
        print("~a =", ~a)
        print("a << 1 =", a << 1)
        print("a >> 1 =", a >> 1)

    case 4:
        print("\n* Logical Operators *")
        print("Logical AND =", a > b and b < 5)
        print("Logical OR =", a == b or b > a)
        print("Logical NOT =", not (a > b))

    case 5:
        print("\n* Assignment Operators *")

        c = a
        c += b
        print("a += b :", c)

        c = a
        c -= b
        print("a -= b :", c)

        c = a
        c *= b
        print("a *= b :", c)

        c = a
        c /= b
        print("a /= b :", c)

    case 6:
        print("\n* Membership Operators *")

        my_list = [10, 20, 30, 40, 50]
        print(my_list)

        num = int(input("Enter a number to check membership: "))
        print(num, "in list :", num in my_list)
        print(num, "not in list :", num not in my_list)

    case 7:
        print("\n* Identity Operators *")

        p = [1, 2, 3]
        q = p
        r = [1, 2, 3]

        print("p is q :", p is q)
        print("p is r :", p is r)
        print("p is not r :", p is not r)

    case _:
        print("Invalid Choice")