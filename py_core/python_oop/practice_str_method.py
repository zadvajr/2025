"""__str__() Method"""
# The __str__() method controls what should be returned when the class object is represented as a string.
# If the __str__() method is not defined in the class, the string representation of the object is returned.
# Example
class Person:
    """A simple example class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Person Class"


p1 = Person("John", 36)
print(p1)
