# Define the base class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # The base class does not provide a specific implementation for speaking


# Define a subclass (derived class) that inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


# Define another subclass (derived class) that also inherits from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


# Create instances of the subclasses
dog_instance = Dog("fluffy")
cat_instance = Cat("blacky")

# Accessing methods from the base class and subclasses
print(f"{dog_instance.name} is an animal.")
print(dog_instance.speak())

print(f"{cat_instance.name} is an animal.")
print(cat_instance.speak())
