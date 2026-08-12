########gobal scope
name="nibba"

def student():
    print(name)
student()

print(name)

name="nibbi"

def student():
    print(name)
student()

print(name)
  
######local scope
def student():
    age = 20
    print(age)
student()

###local and global scope

name = "nibba"
def student():
    age=20
    print(name)
    print(age)
student()

name = "bindu"
def student():
    name = "revanth"
    print(name)
student()
print(name)

name="bindu"
name="revanth"
def display():
    name="revanth"
    name="bindu"
    print(name)
display()
print(name)

######lambda function
square = lambda x: x*x
print(square(3))

cube= lambda x: x*x*x
print(cube(7))

multiplication= lambda x,y: x*y
print(multiplication(5,6))

division=lambda x,y: x/y
print(division(10,2))

addition=lambda x,y: x+y
print(addition(10,20))

subraction=lambda x,y: x-y
print(subraction(30,4))

###largest number
large=lambda a,b: a if a>b else b
print(large(5,6))

###recursion

recursion=lambda x: 1 if x==0 else x*recursion(x-1)
print(recursion(5))

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(7)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
print(power(2, 3))

def primenumber(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return primenumber(n, i + 1)
print(primenumber(7))

def wholenumber(n):
    if n == 0:
        return True
    elif n < 0:
        return False
    else:
        return wholenumber(n - 1)
print(wholenumber(5/3))

def even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return even(n - 2)
print(even(30))

def odd(n):
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        return odd(n - 2)
print(odd(3))
 
