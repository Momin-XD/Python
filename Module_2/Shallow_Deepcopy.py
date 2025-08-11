import copy

"""
Shallow and Deep Copy in Python

In Python, copying objects can be done in two ways: shallow copy and deep copy.

1. Shallow Copy:
    - A shallow copy creates a new object, but does not create copies of nested objects.
    - The new object references the same nested objects as the original.
    - Changes to nested objects in either the original or the copy will affect both.

    Example:
"""


original_list = [[1, 2], [3, 4]]
shallow_copied_list = copy.copy(original_list)

shallow_copied_list[0][0] = 99
print("Original List after shallow copy modification:", original_list)
# Output: [[99, 2], [3, 4]]

"""
2. Deep Copy:
    - A deep copy creates a new object and recursively copies all nested objects.
    - The new object and its nested objects are completely independent of the original.
    - Changes to nested objects in the copy do not affect the original.

    Example:
"""

deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[0][0] = 42
print("Original List after deep copy modification:", original_list)
# Output: [[99, 2], [3, 4]]

"""
Summary:
- Use shallow copy when you want a new object but shared nested objects.
- Use deep copy when you want a completely independent copy, including all nested objects.
"""