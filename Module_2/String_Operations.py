print('Hello from Module 2 Practice.py!')


# Escape Sequences
print("Hello, World!\nThis is a new line.")  #\n-- New line
print("Hello, World!\tThis is a tab space.")  #\t-- Tab space
print("Hello, \"World\"!")  # \" -- Double quote
print('Hello, \'World\'!')  # \' -- Single quote
print("Hello, \\World\\!")  # \\ -- Backslash




# String Operations
# String Length
s = "Hello, World!"
print("String Length:", len(s))  # Output: 13


# String to Upper Case
print("Upper Case:", s.upper())  # Output: HELLO, WORLD!


# String to Lower Case
print("Lower Case:", s.lower())  # Output: hello, world!


# String Replacement
print("Replaced String:", s.replace("World", "Python"))  # Output: Hello, Python!
print("Replaced String:", s.replace("l", "L",2))  # Output: HeLLo, World!
print("Replaced String:", s.replace("l", "L",1))  # Output: HeLlo, World!



# String Splitting
print("Split String:", s.split(","))  # Output: ['Hello', ' World!']


# String Joining
words = ['Hello', 'World']
print("Joined String:", ' '.join(words))  # Output: Hello World


# String Formatting
name = "Alice"
age = 30
print("Formatted String: My name is {} and I am {} years old.".format(name, age)) # Output: My name is Alice and I am 30 years old.
print(f"Formatted String with f-string: My name is {name} and I am {age} years old.") # Output: My name is Alice and I am 30 years old.


# String Stripping
s_with_spaces = "   Hello, World!   "
print("Stripped String:", s_with_spaces.strip())  # Output: Hello, World!



# String Indexing and Slicing
# String Indexing
print("First Character:", s[0])  # Output: H
print("Last Character:", s[-1])  # Output: !


# Slicing
s1= "Hello World! How are you?"
print("Sliced String:", s1[0:5])  # Output: Hello
print("Sliced String with Step:", s1[0:20:2])  # Output: Hlo ol! o r o
print("Sliced String with Negative Index:", s1[-5:])  # Output: you?


# String Concatenation
s2 = "Python"
s3 = "Programming"
print("Concatenated String:", s2 + " " + s3)  # Output: Python Programming

# String Reversal
reversed_s = s[::-1]
print("Reversed String:", reversed_s)  # Output: !dlroW ,olleH

# String Count
print("Count of 'o':", s.count('o'))  # Output: 2


# String Find   
print("Index of 'World':", s.find('World'))  # Output: 7
print("Index of 'Python':", s.find('Python'))  # Output: -1 (not found)

# String Startswith
print("Starts with 'Hello':", s.startswith('Hello'))
# Output: True
print("Starts with 'World':", s.startswith('World'))
# Output: False

# String Endswith
print("Ends with '!':", s.endswith('!'))
# Output: True
print("Ends with 'World':", s.endswith('World'))
# Output: False

# String Isdigit
print("Is '12345' a digit?:", '12345'.isdigit())  # Output: True
print("Is 'Hello' a digit?:", 'Hello'.isdigit())  # Output: False

# String Isalpha
print("Is 'Hello' alphabetic?:", 'Hello'.isalpha())  # Output: True
print("Is 'Hello123' alphabetic?:", 'Hello123'.isalpha())  # Output: False

# String Isalnum
print("Is 'Hello123' alphanumeric?:", 'Hello123'.isalnum())  # Output: True
print("Is 'Hello 123' alphanumeric?:", 'Hello 123'.isalnum())  # Output: False
print("Is '12345' alphanumeric?:", '12345'.isalnum())  # Output: True
print("Is 'Hello!' alphanumeric?:", 'Hello!'.isalnum())  # Output: False

# String Islower
print("Is 'hello' lowercase?:", 'hello'.islower())# Output: True
print("Is 'Hello' lowercase?:", 'Hello'.islower())  # Output: False
print("Is 'HELLO' lowercase?:", 'HELLO'.islower())  # Output: False

# String Isupper   
print("Is 'HELLO' uppercase?:", 'HELLO'.isupper())  # Output: True
print("Is 'Hello' uppercase?:", 'Hello'.isupper())  # Output: False
print("Is 'hello' uppercase?:", 'hello'.isupper())  # Output: False



# String Isspace
print("Is '   ' whitespace?:", '   '.isspace())  # Output: True
print("Is 'Hello' whitespace?:", 'Hello'.isspace())  # Output: False

# String Isprintable
print("Is 'Hello' printable?:", 'Hello'.isprintable())  # Output: True
print("Is 'Hello\n' printable?:", 'Hello\n'.isprintable())  # Output: False (contains newline) 

# String Isidentifier
print("Is 'my_variable' a valid identifier?:", 'my_variable'.isidentifier())  # Output: True
print("Is '2nd_variable' a valid identifier?:", '2nd_variable'.isidentifier())  # Output: False (starts with a digit)
print("Is 'my-variable' a valid identifier?:", 'my-variable'.isidentifier())  # Output: False (contains hyphen)

# String Swapcase
print("Swapcase:", s.swapcase())  # Output: hELLO, wORLD!   

# String Title
print("Title Case:", s.title())  # Output: Hello, World!

# String Capitalize
print("Capitalized String:", s.capitalize())  # Output: Hello, world!


