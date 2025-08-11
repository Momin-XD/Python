'''
Tuple basics in Python
A tuple is a built-in data structure in Python that can store a collection of items.
Tuples are ordered, immutable (cannot be changed), and can contain elements of different types.
'''

# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements
first_item = my_tuple[0]
last_item = my_tuple[-1]
print("First item:", first_item)
print("Last item:", last_item)

# Tuples are immutable
# my_tuple[0] = 10  # This will raise a TypeError

# Tuple unpacking
a, b, c, d, e = my_tuple

# Length of a tuple
length = len(my_tuple)
print("Length:", length)

# Tuple methods
count_apples = my_tuple.count("apple")
index_banana = my_tuple.index("banana")

print("Count of 'apple':", count_apples)
print("Index of 'banana':", index_banana)

# converting a tuple to a list
tuple_to_list = list(my_tuple)
print("Tuple to List:", tuple_to_list)

# Tuple concatenation
my_tuple = (1, 2, 3, "apple", "banana")
another_tuple = (4, 5, 6)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated Tuple:", concatenated_tuple)

# Tuple slicing
sliced_tuple = my_tuple[1:4]
print("Sliced Tuple:", sliced_tuple)

# Tuple membership
is_apple_in_tuple = "apple" in my_tuple 
print("Is 'apple' in tuple?", is_apple_in_tuple)

# reversing a tuple
reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)

# repetion of tuples
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)

# min and max in tuples
# Note: min and max only work with numeric values
t= (1, 2, 3, 4, 5)
min_value = min(t)  # Only considering numeric values
max_value = max(t)  # Only considering numeric values
print("Min value in numeric part of tuple:", min_value)
print("Max value in numeric part of tuple:", max_value)

# Tuple sorting (requires conversion to a list)
sorted_tuple = tuple(sorted(my_tuple[:3]))
print("Sorted Tuple (numeric part):", sorted_tuple)







'''
Set basics in Python
A set is a built-in data structure in Python that can store a collection of unique items.
Sets are *unordered*, mutable (can be changed), and *do not allow duplicate elements*.
'''


# Creating a set
my_set = {1, 2, 3, "apple", "banana"}

# Accessing elements
# Sets do not support indexing, but you can iterate through them
for item in my_set:
    print("Item in set:", item)


# Adding elements to a set
my_set.add("orange")
print("Set after adding 'orange':", my_set) # Output: {1, 2, 3, 'apple', 'banana', 'orange'}

# Removing elements from a set
my_set.remove("banana")
print("Set after removing 'banana':", my_set)  # Output: {1, 2, 3, 'apple', 'orange'}

# Discarding elements from a set (does not raise an error if the element is not found)
my_set.discard("apple")
print("Set after discarding 'apple':", my_set)  # Output: {1, 2, 3, 'orange'}


# Set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of sets:", union_set)  # Output: {1, 2, 3, 4, 5}

# Set intersection
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)  # Output: {3}

# Set difference
difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)  # Output: {1, 2}

# Set symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of sets:", symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Set length
set_length = len(my_set)
print("Length of set:", set_length)  # Output: 4


# Set membership
is_apple_in_set = "apple" in my_set
print("Is 'apple' in set?", is_apple_in_set)  # Output: False


# Set conversion from list
list_to_set = set([1, 2, 3, 4, 5])
print("List to Set:", list_to_set)  # Output: {1, 2, 3, 4, 5}




# frozenset
# A frozenset is an immutable version of a set.
frozen_set = frozenset([1, 2, 3, "apple", "banana"])
print("Frozen Set:", frozen_set)  # Output: frozenset({1, 2, 3, 'apple', 'banana'})
# Attempting to add an element to a frozenset will raise an error
# frozen_set.add("orange")  # This will raise an AttributeError
