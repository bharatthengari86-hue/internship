""" #6
class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display(self):
        print("Name =", self.__name)
        print("Marks =", self.__marks)

s = Student("Bharat", 95)
s.display() """


""" #7
class Employee:

    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e = Employee()
e.set_salary(50000)
print("Salary =", e.get_salary()) """



""" #8
class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance =", self.__balance)

b = BankAccount()
b.deposit(1000)
b.withdraw(300)
b.show_balance() """



""" #9
class Mobile:

    def __init__(self):
        self.__price = 0

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

m = Mobile()
m.set_price(15000)
print("Price =", m.get_price())
 """



""" #10
class ATM:

    def __init__(self):
        self.__pin = 1234
        self.__balance = 5000

    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance =", self.__balance)
        else:
            print("Wrong PIN")

a = ATM()
a.check_balance(1234) """