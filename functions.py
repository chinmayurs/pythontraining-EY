#In Python, 'map', 'reduce', 'filter', 'apply', 'zip', and 'lambda' are all functions or concepts commonly used in functional programming.

#1. 'map' function:

#The 'map' function applies a given function to all items in an input list (or any iterable) and returns an iterator of the results.

# Example
numbers = [1, 2, 3, 4, 5]

# Using map to square each number
squared_numbers = map(lambda x: x**2, numbers)

# Converting the result to a list
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)
# Output: [1, 4, 9, 16, 25]

------------------------------------------------------------------------------

#2. 'reduce' function:

#The 'reduce' function performs a cumulative operation on the items of an iterable, from left to right, to reduce the iterable to a single accumulated result.

from functools import reduce

# Example
numbers = [1, 2, 3, 4, 5]

# Using reduce to find the product of all numbers
product = reduce(lambda x, y: x * y, numbers)

print(product)
# Output: 120 (1 * 2 * 3 * 4 * 5)

------------------------------------------------------------------------------

#3. 'filter' function:

#The 'filter' function filters elements from an iterable based on a function that returns 'True' or 'False'.

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using filter to get even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Converting the result to a list
even_numbers_list = list(even_numbers)

print(even_numbers_list)
# Output: [2, 4, 6, 8]

------------------------------------------------------------------------------

#4. 'zip' function:

#The 'zip' function combines multiple iterables element-wise.

# Example
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Using zip to combine names and ages
combined = zip(names, ages)

# Converting the result to a list
combined_list = list(combined)

print(combined_list)
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

------------------------------------------------------------------------------

#5. 'lambda' function:

#A 'lambda' function is an anonymous function defined with the 'lambda' keyword. It's often used for short, simple operations.

# Example
add = lambda x, y: x + y

result = add(3, 4)
print(result)
# Output: 7
