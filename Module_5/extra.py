'''

# This script generates a multiplication table for a given number.
a = int(input('Enter a number: '))
for i in range(1,11):
    print(f'{a} X {i} = {a*i}')


# Add two numbers
a= int(input('Enter first number: '))
b= int(input('Enter second number: '))
print(f'The Sum of {a} and {b} is {a+b}')


# Finding the remainder
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(f'The Remainder of {a} divided by {b} is {a % b}')


# Average of three numbers
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
avg=(a+b+c)/3
print(f'The Average of {a}, {b}, and {c} is {avg}')


# fechting the current date and time

from datetime import datetime
name = input('Enter your name: ')
now = datetime.now()
print(f'Dear {name},\nYou are Selected!\n{now.strftime("%Y-%m-%d %H:%M:%S")}')



s="My name  is momin"
print(s)
print("  " in s)
print(s.replace("  ",' '))



# This script collects fruit names from the user and stores them in a list.
l=[]
for i in range(1,8):
    if i==1:
        a= input("Enter the fruit name: ")
        l.append(a)
        continue
    else:
        a= input("Enter the next fruit name: ")
        l.append(a)
print(l)


# 
l=[3,6,9,12,15,18,21,24,27,30]
a=0
for i in l:
    a+=i
print(f'The sum of the list is {a}')


l=[3,6,9,12,15,18,21,24,27,30]
print(tuple(l))


# 
from googletrans import Translator

def dict(eword):

    translator = Translator()
    result = translator.translate(eword, src='en', dest='hi')
    return(result.text)
print('Dictionary: Eng -> Hindi')
eword=input("Enetr your word: ")
hword=dict(eword)
print(hword)


# 
math=int(input("Enter Maths marks: "))
physics=int(input("Eneter Physics marks: "))
chem=int(input("Eneter Chemistry marks: "))

total_percentage=100*(math+physics+chem)/300

if total_percentage>=40 and math>=33 and physics>=33 and chem>=33:
    print("You are eligable")
else:
    print('You are not eligable')

# 
i=0
l=['Rahul','Chaube','Ritika','Chandan','Maz']
while i<len(l):
    print(l[i])
    i+=1


# 
for i in range(6):
    print(i)
else:
    print('done')

# 
for i in range(40):
    if i==25:
        break
    print(i)

# 
num=int(input('Enter the number: '))
for i in range(1,11):
    print(f'{num} X {i} = {num*i}')

    
# 
l=['Rahul','Chaube','Ritika','Chandan','Maz']
for i in l:
    if i.startswith('C'):
        print('Hello, '+i)
    else:
        print('Hello')

# 
i=1
num=int(input('Enter the number: '))
while i<=10:
        print(f'{num} X {i} = {num*i}')
        i+=1

# 
a=0
n=int(input('Enter the value of n to find the sum of n numbers: '))
i=1
while i<=n:
    a+=i
    i+=1
print(f"Sum first {n} numbers is {a}")


# 
num=int(input('Enter the number: '))
fact=1
for i in range(1,num+1):
    fact*=i
print(f'Factorial of {num} is {fact}')


# 
num=int(input('Enter the number: '))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    print("*"*(2*i-1),end="")
    print('')

# 
n=int(input('Enter the number: '))
for i in range(1,n+1):
    print("*"*i)


'''
# 
n=int(input('Enter the number: '))
for i in range(1,n+1):
    if (i==1) or (i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")
