'''
Introduction to Lists in Python

A list is a built-in data structure in Python that can store a collection of items.
Lists are ordered, mutable (can be changed), and can contain elements of different types.
'''
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']



# Basic Operations On Lists
# Type of list
print(type(fruits))  # Output: <class 'list'>

# List length
print(len(fruits))  # Output: 3


# Lists can contain different data types
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)  # Output: [1, 'hello', 3.14, True]


# Accessing elements (indexing starts at 0)
print(fruits[0])  # Output: apple


# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']


# REMOVING ELEMENTS FROM LISTS
# Lists can have elements removed using various methods.
# Using the del statement
del fruits[1]
print(fruits)  # Output: ['apple', 'cherry']

# Removing elements
# First occurrence of an element will be removed
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']


# popping elements
popped_fruit = fruits.pop(2)
print(popped_fruit)  # Output: cherry
print(fruits)  # Output: ['apple', 'blueberry', 'kiwi', 'mango']




# ADDING ELEMENTS TO LISTS
# Lists can be extended or elements can be added using various methods.
# Extending element
fruits.extend(["kiwi", "mango"])
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'kiwi', 'mango']

# Adding elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']


# Inserting elements
fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange']


# List Concatenation
fruits2 = ["pear", "peach"]
print(fruits + fruits2)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange', 'pear', 'peach']




# List Repetition
print(fruits * 2)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange', 'apple', 'grape', 'blueberry', 'cherry', 'orange']





# Slicing Lists
# Slicing allows you to access a portion of the list.
Fruits=['Orange', 'Grape', 'Guava', 'Lemon', 'Apple', 'Mango', 'Kivi', 'Banana']
print(Fruits[1:5])  # Output: ['Grape', 'Guava', 'Lemon', 'Apple']
print(Fruits[:3])  # Output: ['Orange', 'Grape', 'Guava']
print(Fruits[3:])  # Output: ['Lemon', 'Apple', 'Mango', 'Kivi', 'Banana']
print(Fruits[-3:])  # Output: ['Mango', 'Kivi', 'Banana']
print(Fruits[-5:-2])  # Output: ['Lemon', 'Apple', 'Mango']
print(Fruits[::2])  # Output: ['Orange', 'Guava', 'Apple', 'Kivi']
print(Fruits[::-1])  # Output: ['Banana', 'Kivi', 'Mango', 'Apple', 'Lemon', 'Guava', 'Grape', 'Orange']





# List Methods
# Lists have several built-in methods for various operations.
# Sorting a list
Fruits.sort()
print(Fruits)  # Output: ['Apple', 'Banana', 'Grape', 'Guava', 'Kivi', 'Lemon', 'Mango', 'Orange']  

# Reversing a list
Fruits.reverse()
print(Fruits)  # Output: ['Orange', 'Mango', 'Lemon', 'Kivi', 'Guava', 'Grape', 'Banana', 'Apple']

# Finding the index of an element
print(Fruits.index('Mango'))  # Output: 1 (index of 'Mango')

# Checking if an element exists in the list
print('Apple' in Fruits)  # Output: True (checks if 'Apple' is in the list)

# Counting occurrences of an element
print(Fruits.count('Apple'))  # Output: 1 (count of 'Apple')

# Copying a list
Fruits_copy = Fruits.copy()
print(Fruits_copy)  # Output: ['Orange', 'Mango', 'Lemon', 'Kivi', 'Guava', 'Grape', 'Banana', 'Apple']



# Nested Lists
# Lists can contain other lists, creating a nested structure.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
print(nested_list[0][1])  # Output: 2 (second element of the first list)

# sorting a nested list
n=[5,3,8,2,6,1,4,7]
n.sort()
print(n)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]



'''
numerical operations on lists
Lists can also be used for numerical operations, such as finding the sum or average.
'''
numbers = [10, 20, 30, 40, 50]

# Finding the sum of elements in a list
total = sum(numbers)
print("Sum of numbers:", total)  # Output: Sum of numbers: 150


# Finding the average of elements in a list
average = total / len(numbers)
print("Average of numbers:", average)  # Output: Average of numbers: 30.0


# Finding the maximum and minimum values in a list
max_value = max(numbers)
min_value = min(numbers)
print("Maximum value:", max_value)  # Output: Maximum value: 50
print("Minimum value:", min_value)  # Output: Minimum value: 10
