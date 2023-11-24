#Dundedunder methods, short for "double underscore" methods, are special methods in Python that have double underscores at the beginning and end of their names.
#These methods are also known as magic methods or special methods. They define how objects of a class behave in various situations.

class MyClass:
    def __init__(self, value):
        self.value = value

    # Dunder method for string representation of the object
    def __str__(self):
        return f"MyClass instance with value: {self.value}"

    # Dunder method for the length of the object
    def __len__(self):
        return len(str(self.value))

    # Dunder method for addition
    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        else:
            raise ValueError("Unsupported operand type")

# Create instances of the class
obj1 = MyClass(10)
obj2 = MyClass(20)

# Using dunder method for string representation
print(obj1)  # Output: MyClass instance with value: 10

# Using dunder method for addition
result = obj1 + obj2
print(result)  # Output: MyClass instance with value: 30

# Using dunder method for length
length = len(obj1)
print(length)  # Output: 2 (length of the string representation "10")


# `__init__`: This is not strictly a dunder method, but it's commonly used for initializing objects when they are created.

# `__str__`: This dunder method is called by the built-in `str()` function and provides a string representation of the object.

# `__len__`: This dunder method is called by the built-in `len()` function and provides the length of the object.

# `__add__`: This dunder method is called when the `+` operator is used with instances of the class.

#Dunder methods allow you to define the behavior of your objects in a way that integrates seamlessly with Python's built-in functions and operators.