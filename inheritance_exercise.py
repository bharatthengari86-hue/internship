""" #1
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name=",self.name)
        print("age=",self.age)

s=student("bharat",17)
s.display() """


""" #2
class employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.id=emp_id
        self.salary=salary

    def show_details(self):
        print("employee name=",self.name)
        print("empolyee id=",self.id)
        print("employee salary=",self.salary)

a=input("enter a employee name:-")
b=int(input("enter employee id:- "))
c=float(input("enter employee salary:-"))
e=employee(a,b,c)
e.show_details()
 """

""" #3
class car:
    def __init__(self):
        self.brand="BMW"
        self.model=2022
        self.price=100000

    def display_car(self):
        print("Brand name=",self.brand)
        print("model year=",self.model)
        print("price=",self.price)

c=car()
c.display_car()  """      


""" #4
class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def book_info(self):
        print("book title name=",self.title)
        print("book author name=",self.author)
        print("book price=",self.price)

b=book("mahabharat","xyz",500)
b.book_info() """


""" #5
class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    
    def calculate_area(self):
        area=self.length*self.breadth
        print("area of rectangel=",area)

a=int(input("enter length:-"))
b=int(input("enter breadth:-"))
r=rectangle(a,b)
r.calculate_area()
 """


""" #6
class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def calculate_area(self):
        area=3.14*self.radius*self.radius
        print("area of circle=",area)

a=int(input("enter radius of circle:-"))
c=circle(a)
c.calculate_area() """


""" #7
class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.account_number=acc_no
        self.name=name
        self.balance=balance

    def deposit(self):

        a=int(input("enter amount to deposit:-"))
        self.balance+=a
        print(a,"deposited succesfully")
    
    def withdraw(self):
        b=int(input("enter amount to withdraw:-"))
        if b>=self.balance:
            print("you can not widraw money")
        else:
            self.balance-=b
            print(b,"withdrawl succesfully")

    def check_balance(self):
        print("current balance=",self.balance)


a=int(input("enter account number:- "))
c=input("enter name:-")
b=BankAccount(a,c,50000) 

while True:
    print("1.deposit")
    print("2.withdraw")
    print("3.check_balance")
    print("4.exit")
    choice=int(input("enter your choice:-"))
    match choice:
        case 1:
            b.deposit()
        case 2:
            b.withdraw()
        case 3:
            b.check_balance()
        case 4:
            exit(0)
        case _:
            print("invalid choice")

 """



#8
""" class Product:
    def __init__(self, product_id, product_name, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def add_stock(self):
        stock = int(input("Enter quantity to add: "))
        self.quantity += stock
        print(stock, "items added successfully")

    def remove_stock(self):
        stock = int(input("Enter quantity to remove: "))
        
        if stock > self.quantity:
            print("Not enough stock available")
        else:
            self.quantity -= stock
            print(stock, "items removed successfully")

    def display_product(self):
        print("\nProduct Details")
        print("Product ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Quantity     :", self.quantity)
        print("Price        :", self.price)


# Create Product Object
pid = int(input("Enter Product ID: "))
pname = input("Enter Product Name: ")
qty = int(input("Enter Quantity: "))
price = float(input("Enter Price: "))

p = Product(pid, pname, qty, price)

while True:
    print("\n1. Add Stock")
    print("2. Remove Stock")
    print("3. Display Product")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            p.add_stock()

        case 2:
            p.remove_stock()

        case 3:
            p.display_product()

        case 4:
            exit(0)

        case _:
            print("Invalid Choice") """


""" #9
class mobile:
    def __init__(self,brand,model,ram,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.price=price

    def display_specs(self):
        print("brand name=",self.brand)
        print("model =",self.model)
        print("ram=",self.ram)
        print("price=",self.price)

m=mobile("moto",2021,"6gb",13000)
m.display_specs() """



""" #10
class LibraryBook:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def issue_book(self):
        a=int(input("enter number of copies you want:-"))
        if self.available_copies > 0:
            self.available_copies -= a
            print("Book issued successfully")
        else:
            print("No copies available")

    def return_book(self):
        c=int(input("enter how many copies isuue :-"))
        self.available_copies += c
        print("Book returned successfully")

    def display_details(self):
        print("Book ID =", self.book_id)
        print("Title =", self.title)
        print("Author =", self.author)
        print("Available Copies =", self.available_copies)


book_id = int(input("Enter book ID: "))
title = input("Enter book title: ")
author = input("Enter author name: ")
copies = int(input("Enter available copies: "))

book = LibraryBook(book_id, title, author, copies)

while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Display Details")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            book.issue_book()

        case 2:
            book.return_book()

        case 3:
            book.display_details()

        case 4:
            exit(0)

        case _:
            print("Invalid Choice") """