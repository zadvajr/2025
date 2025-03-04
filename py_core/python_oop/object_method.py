"""Object methods"""
# Objects can also contain methods.
# Methods in objects are functions that belong to the object.
# Let's create a class with a method.
# Example:
class Person():
    """A simple class to represent a person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    
    def info(self):
        """Prints the name and age of the person"""
        print(f"{self.name} is {self.age} years old")

# Create an object of the class Person
p1 = Person("Zadva", 36)

# Call the method info() on the object p1
p1.info() # Output: Zadva is 36 years old

# Note: The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
