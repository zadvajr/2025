#The __str__() function
# The __string__() function controls what is returned when class object is represented as a string
# if the __string__() method is not set, the string representation of the object is returned
#Example
# The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

# Example
# The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)