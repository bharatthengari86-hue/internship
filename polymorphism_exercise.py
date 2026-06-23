#11
""" import math
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        l = 10
        b = 5
        print("Area of Rectangle =", l * b)

class Circle(Shape):
    def area(self):
        r = 7
        print("Area of Circle =", math.pi * r * r)

class Triangle(Shape):
    def area(self):
        b = 8
        h = 4
        print("Area of Triangle =", 0.5 * b * h)

r = Rectangle()
c = Circle()
t = Triangle()

r.area()
c.area()
t.area() """



""" #12
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says Woof")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

class Cow(Animal):
    def sound(self):
        print("Cow says Moo")

d = Dog()
c = Cat()
cw = Cow()

d.sound()
c.sound()
cw.sound() """



""" #13
class Payment:
    def make_payment(self):
        pass

class CreditCard(Payment):
    def make_payment(self):
        print("Payment through Credit Card")

class UPI(Payment):
    def make_payment(self):
        print("Payment through UPI")

class NetBanking(Payment):
    def make_payment(self):
        print("Payment through Net Banking")

c = CreditCard()
u = UPI()
n = NetBanking()

c.make_payment()
u.make_payment()
n.make_payment() """



""" #14
class Notification:
    def send_notification(self):
        pass

class Email(Notification):
    def send_notification(self):
        print("Email Notification Sent")

class SMS(Notification):
    def send_notification(self):
        print("SMS Notification Sent")

class WhatsApp(Notification):
    def send_notification(self):
        print("WhatsApp Notification Sent")

e = Email()
s = SMS()
w = WhatsApp()

e.send_notification()
s.send_notification()
w.send_notification() """


""" #15
class Employee:
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def calculate_bonus(self):
        print("Manager Bonus = 10000")

class Developer(Employee):
    def calculate_bonus(self):
        print("Developer Bonus = 5000")

class Tester(Employee):
    def calculate_bonus(self):
        print("Tester Bonus = 3000")

m = Manager()
d = Developer()
t = Tester()

m.calculate_bonus()
d.calculate_bonus()
t.calculate_bonus() """