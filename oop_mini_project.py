""" #1 school management system
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks

    def display(self):
        super().display()
        print("Marks:", self.__marks)

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        super().display()
        print("Subject:", self.subject)


s = Student("Bharat", 95)
t = Teacher("kharakate mam", "DSU")

print("Student Details")
s.display()

print("\nTeacher Details")
t.display() """


""" #2 hospital management system
class Person:
    def __init__(self, name):
        self.name = name

class Patient(Person):
    def __init__(self, name, disease):
        super().__init__(name)
        self.disease = disease

    def display(self):
        print("Patient:", self.name)
        print("Disease:", self.disease)

class Doctor(Person):
    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization

    def display(self):
        print("Doctor:", self.name)
        print("Specialization:", self.specialization)


p = Patient("Rahul", "Fever")
d = Doctor("Sharma", "Cardiology")

p.display()
print()
d.display() """


""" #3 Banking System
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print("Balance =", self.__balance)


b = BankAccount()
b.deposit(5000)
b.withdraw(1000)
b.show_balance() """



""" #4
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)


class Electronics(Product):
    pass


p = Electronics("Laptop", 50000)
p.display() """



""" #5
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def display(self):
        print("Car Brand:", self.brand)


class Bike(Vehicle):
    def display(self):
        print("Bike Brand:", self.brand)


c = Car("Toyota")
b = Bike("Honda")
c.display()
b.display() """


""" #challange exercise

class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price      # Encapsulation

    def show(self):
        print("Title:", self.title)
        print("Price:", self.__price)


class StoryBook(Book):            # Inheritance
    def show(self):               # Polymorphism
        print("\nStory Book")
        super().show()


class AcademicBook(Book):         # Inheritance
    def show(self):               # Polymorphism
        print("\nAcademic Book")
        super().show()


b1 = StoryBook("Harry Potter", 500)
b2 = AcademicBook("Python", 300)

b1.show()
b2.show() """