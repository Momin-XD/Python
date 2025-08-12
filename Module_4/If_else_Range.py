# If-Else Statements in Python

# The if-else statement is used to execute code based on a condition.

x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# You can also use elif for multiple conditions:

y = 3

if y > 5:
    print("y is greater than 5")
elif y == 5:
    print("y is equal to 5")
else:
    print("y is less than 5")

# Example with user input:

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# another example with if-else statements:

age=input("Enter your age: ") 

if int(age)>=18:
    print('congrats! you are an adult.')
elif int(age) < 18 and int(age) >= 13:
    print('You are a teenager.')
else: 
    print('Sorry! you are under age')


# nested if-else statements:

score = int(input("Enter your score: "))   
if score>=60:
    print("Congrats! You passed the exam.")
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
else:
    print("You failed the exam.")



# Range function
# Range function starts from the given point and ends at (endpoint-1)
# Like the following function's range is from 1 to (11-1) that is 10
n=list(range(1, 11))  # Creates a list of numbers from 1 to 10
print("List of numbers from 1 to 10:", n)