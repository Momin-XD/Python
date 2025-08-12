'''
A for loop in Python is used to repeat a block of code a specific number of times, usually by iterating over a sequence like a list, tuple, string, or range.

For Loops in Python
The for loop is used to iterate over a sequence (like a list, tuple, or string) or a range of numbers.
'''


# Example with a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) 

# Here is another example of for loop
fruit='apple'
for f in fruit:
    print(f)

# We can also nested loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) 
    for f in fruit:
        print(f)


# Example with a range:
for i in range(5):
    print(i)




'''
While Loops in Python
A while loop repeatedly executes a block of code as long as a given condition is True.

Syntax:
while condition:
    # code block

Example:
'''

count = 0 #we have to initialise a conditional value
while count < 5:
    print("Count is:", count)
    count += 1 #here we have to increment/decrement the value

