'''
Basic usage of Python dictionaries
A dictionary is a built-in data structure in Python that can store a collection of key-value pairs.
Dictionaries are unordered, mutable (can be changed), and can contain elements of different types.
They are defined using curly braces {} with key-value pairs separated by colons (:).
it does not allow duplicate keys, but allows duplicate values.
it does not have indexing like lists or tuples, but you can access values using keys.
'''



# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: Alice

# getting a value using the get method
print(person.get("age"))  # Output: 30
print(person.get("country", "USA"))  # Output: USA (default value if key not found)

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Updating a value
person["age"] = 31

# Removing a key-value pair
del person["city"]



# Checking if a key exists
if "email" in person:
    print("Email is present.")

# Getting all keys and values
keys = list(person.keys())
values = list(person.values())
print("Keys:", keys) # Output: Keys: ['name', 'age', 'email']
print("Values:", values) # Output: Values: ['Alice', 31, 'alice@example.com']


# membership test
is_name_present = "name" in person
print("Is 'name' present in dictionary?", is_name_present)  # Output: True
not_present = "country" not in person
print("Is 'country' not present in dictionary?", not_present)  # Output: True\

# updating multiple key-value pairs
person.update({"city": "Los Angeles", "phone": "123-456-7890"})
print("Updated Dictionary:", person)  # Output: Updated Dictionary: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com', 'city': 'Los Angeles', 'phone': '123-456-7890'}

# pop a key-value pair
popped_value = person.pop("phone") 
print("Popped Value:", popped_value)  # Output: Popped Value: 123-456-7890
print("Dictionary after pop:", person)  # Output: Dictionary after pop: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com', 'city': 'Los Angeles'}


'''
we can use tuples,bool,int,floar,string as keys in a dictionary, but they must be immutable. and we can use lists as values in a dictionary, but not as keys.'''

# Example of using a tuple as a key
coordinates = {(10, 20): "Point A", (30, 40): "Point B"}
print(coordinates[(10, 20)])  # Output: Point A

# Example of using a boolean as a key
bool_dict = {True: "Yes", False: "No"}
print(bool_dict[True])  # Output: Yes

# Example of using an integer as a key
int_dict = {1: "One", 2: "Two"}
print(int_dict[1])  # Output: One

# Example of using a float as a key
float_dict = {3.14: "Pi", 2.71: "Euler's Number"}
print(float_dict[3.14])  # Output: Pi

# Example of using a string as a key
string_dict = {"name": "Alice", "age": 30}
print(string_dict["name"])  # Output: Alice


# Example of using a list as a value
list_value_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "broccoli"]
}
print(list_value_dict["fruits"])  # Output: ['apple', 'banana', 'cherry']


# nested dictionaries
nested_dict = {
    "person": {
        "name": "Bob",
        "age": 25,
        "address": {
            "city": "San Francisco",   
            "state": "CA"
        }
    },
    "hobbies": ["reading", "traveling"]
}
print(nested_dict["person"]["name"])  # Output: Bob
print(nested_dict["person"]["address"]["city"])  # Output: San Francisco


# items method
print("Items in dictionary:", person.items())  # Output: Items in dictionary: dict_items([('name', 'Alice'), ('age', 31), ('email', 'alice@example.com'), ('city', 'Los Angeles')])