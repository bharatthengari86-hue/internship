#inheritance
#1
""" class person:
    def __init__(self):
        self.name="bharat"
    
    def display(self):
        print("person name=",self.name)

class student(person):
    def __init__(self):
        person.__init__(self)
        self.sname="xyz"

    def show(self):
        print("student name=",self.sname)
       
s=student()
s.display()
s.show() """


""" #2
class vehical:
    def __init__(self):
        self.vname="BMW"

    def display(self):
        print("vehical name=",self.vname)
        
class car(vehical):
    def __init__(self):
        vehical.__init__(self)
        self.price="10000000"
    
    def display_car(self):
        print("car price=",self.price)
        
c=car()
c.display()
c.display_car() """


""" #3
class employee:
    def __init__(self):
        self.ename="xyz"

    def display(self):
        print("employee name=",self.ename)

class manager(employee):
    def __init__(self):
        employee.__init__(self)
        self.mname="bharat"
    
    def show(self):
        print("manager name=",self.mname)

m=manager()
m.display()
m.show() """


""" #4
class Animal:
    def __init__(self):
        self.a="animal make sound"
    
    def display(self):
        print("here is",self.a)
    
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.sound="dog sound is bark"
    
    def display2(self):
        print("here",self.sound)

d=Dog()
d.display()
d.display2() """



""" #5
class BankAccount:

    def __init__(self, account_no):
        self.account_no = account_no

    def display(self):
        print("Account No:", self.account_no)

class SavingsAccount(BankAccount):

    def __init__(self, account_no, balance):
        BankAccount.__init__(self,account_no)
        self.balance = balance

    def display(self):
        BankAccount.display(self)
        print("Balance:", self.balance)

s = SavingsAccount(101, 5000)
s.display()
 """

