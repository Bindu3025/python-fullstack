class student:
    def display(self):
        print("AIDS are good students")
s1=student()
s1.display()

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

s1=student("Bindu",20)
s1.display()

class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)

s1=student("Bindu",20,"AIDS")
s1.display()

###inhertiance
###single level inhertance
class parent:
    def display(self):
        print("This is parent class")
class child(parent):
    def display1(self):
        print("This is child class")
s1=child()
s1.display()
s1.display1()

#multilevel inhertance
class parent:
    def display(self):
        print("This is parent class")
class child(parent):
    def display1(self):
        print("This is child class")
class grandchild(child):
    def display2(self):
        print("This is grandchild class")
s1=grandchild()
s1.display()    
s1.display1()
s1.display2()

# multiple inhertance
class father:
    def skills(self):
        print("father:driving")
class mother:
    def talent(self):
        print("mother:cooking")
class child(father,mother):
    def hobby(self):
        print("child:painting")
c=child()
c.skills()
c.talent()
c.hobby()

######hierarchical inhertance
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Cat(Animal):
    def meow(self):
        print("Cat meows")
d = Dog()
d.eat()
d.bark()
c = Cat()
c.eat()
c.meow()

##########hybrid inhertance
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Cat(Animal):
    def meow(self):
        print("Cat meows")
class Puppy(Dog,Cat):
    def play(self):
        print("Puppy plays")
p=Puppy()

p.eat()
p.bark()
p.meow()
p.play()

###polymorphism
class car:
    def move(self):
        print("car is moving")
class boat:
    def move(self):
        print("boat is sailing")
class plane:
    def move(self):
        print("plane is flying")
vehicles = [car(),boat(),plane()]
for vehicle in vehicles:
    vehicle.move()

from abc import ABC,abstractmethod

class vehicle(ABC):
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car starts with a key")

class bike(vehicle):
    def start(self):
        print("bike starts with a button")
car = car()
bike = bike()
car.start()
bike.start()

from abc import ABC,abstractmethod

class Animals(ABC):
    def start(self):
        pass
class squirrel(Animals):
    def start(self):
        print("squirrel is starts by jumping")

class Lion(Animals):
    def start(self):
        print("Lion starts by roaring")
Lion= Lion()
squirrel = squirrel()
squirrel.start()
Lion.start()

 ##################################encapsulation

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
students=student("revu",98)
print(students.name)
print(students.marks)
students.marks=100
print(students.marks)

# ####encapsulation####

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")
student = Student("Mahi", 90)
print(student.get_marks())
student.set_marks(80)
print(student.get_marks())
print

#####min project#####

from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())


# Inheritance
class Developer(Employee):

    def calculate_salary(self):
        # Developer gets 10% bonus
        bonus = self.get_salary() * 0.10
        return self.get_salary() + bonus


# Inheritance
class Manager(Employee):

    def calculate_salary(self):
        # Manager gets 20% bonus
        bonus = self.get_salary() * 0.20
        return self.get_salary() + bonus


# Creating objects
developer = Developer("Bindu", 50000)
manager = Manager("Anu", 60000)

developer.display()
manager.display()

