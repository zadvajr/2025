"""The self Parameter"""
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

# Example
# Use the words me and myself instead of self:
class Person:
    def __init__(me, name, age):
        me.name = name
        me.age = age
    def info(myself):
        print(f"{myself.name} is {myself.age} years old")

p1 = Person("John", 36)
p1.info() # Output: John is 36 years old