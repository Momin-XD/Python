print('hello world')

# Arithmetic Operations
# comparitive operations
a=10
b=20
print("Is a equal to b?", a == b)  # "==" compares two quantities,  Output: False
print("Is a not equal to b?", a != b)  # "!=" checks if two quantities are not equal, Output: True
print("Is a greater than b?", a > b)  # ">" checks if a is greater than b, Output: False
print("Is a less than b?", a < b)  # "<" checks if a is less than b, Output: True
print("Is a greater than or equal to b?", a >= b)  # ">=" checks if a is greater than or equal to b, Output: False
print("Is a less than or equal to b?", a <= b)  # "<=" checks if a is less than or equal to b, Output: True

# logical operations
print("Is a equal to 10 and b equal to 20?", a == 10 and b == 20)  # Output: True
print("Is a equal to 10 or b equal to 30?", a == 10 or b == 30)  # Output: True
print("Is not a equal to 10?", not a == 10)  # Output: False






# This script performs basic arithmetic operations on two numbers provided by the user.

# Uncomment the following lines to convert Celsius to Fahrenheit
c=float(input('Enter a number: '))
F=(c*9/5) + 32
print('Fahrenheit:', F)


# Uncomment the following lines to convert Fahrenheit to Celsius
f=float(input('Enter a number: '))
C=(f-32)*5/9
print('Celsius:', C)


# SI calculator --- EQN: SI = (P * R * T)/100
P = float(input('Enter Principal amount: '))
R = float(input('Enter Rate of interest: '))
T = float(input('Enter Time in years: '))
SI = (P * R * T) / 100
print('Simple Interest:', SI)


# principal amount calculator --- EQN: P = (SI * 100) / (R * T)
SI = float(input('Enter Simple Interest: '))
R = float(input('Enter Rate of interest: '))
T = float(input('Enter Time in years: '))
P = (SI * 100) / (R * T)
print('Principal Amount:', P)


# Area of triangle --- EQN: Area = (base * height) / 2
print('Area of Triangle Calculator')
base = float(input('Enter base of triangle: '))
height = float(input('Enter height of triangle: '))
area = (base * height) / 2
print('Area of Triangle:', area)


# Area of triangle using Heron's formula --- EQN: Area = sqrt(s * (s - a) * (s - b) * (s - c))
print('Area of Triangle using Heron\'s formula')
a= float(input('Enter side a: '))
b= float(input('Enter side b: '))
c= float(input('Enter side c: '))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('Area of Triangle:', round(area,2))

