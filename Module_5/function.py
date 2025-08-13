'''
Functions in Python are reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs easier to read and maintain.

You define a function using the def keyword.
'''

# Example of a simple function
def greet(name): # 
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# def keyword is used to define a function
# greet is the name of the function
# name is a parameter that the function takes
# we call the function by its name and pass an argument to it


# Function with return value
def add(a, b):
    return a + b  # Returns the sum of a and b

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
result = add(a, b)
print(f"The sum of {a} and {b} is: {result}")  # Output: The sum is: 8



# Passing multiple arguments
def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product

result = multiply(2, 3, 4)
print(f"The product is: {result}")  # Output: The product is: 24


# Function with default parameters
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")
greet_with_default()  # Output: Hello, Guest!  When no argument is passed
greet_with_default("Bob")  # Output: Hello, Bob!




# Functions as arguments
def apply_function(func, value):
    return func(value)
def square(x):
    return x * x
result = apply_function(square, 5)
print(f"The square of 5 is: {result}")  # Output: The square of 5 is: 25


def add(a, b):
    return multiply(a + b)
def square(a):
    return a * a
result = square(add(2, 3))
print(f"The result of adding 2 and 3, then squaring it is: {result}")  # Output: The result of adding 2 and 3, then squaring it is: 25