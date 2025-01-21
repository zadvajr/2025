#Getting Started
#This section is about static and dynamic type checking in python

#Installing and Running mypy
#To install - python -m pip install mypy
#once it is installed you run it using the mypy tool as follows
#mypy filename.py

#Inorder to enjoy mypy you must add type annotations to your code. that is type hints

# Dynamic vs static typing
# A function without type annotations is considered to be dynamically typed by mypy:

# def greeting(name):
#     return 'Hello ' + name

# By default, mypy will not type check dynamically typed functions.
# This means that with a few exceptions, mypy will not report any errors with regular unannotated Python.

# This is the case even if you misuse the function!
def greeting(name):
    return 'Hello ' + name

# These calls will fail when the program runs, but mypy does not report an error
# because "greeting" does not have type annotations.
greeting(123)
greeting(b"Alice")

# We can get mypy to detect these kinds of bugs by adding type annotations (also known as type hints).
# For example, you can tell mypy that greeting both accepts and returns a string like so:

# The "name: str" annotation says that the "name" argument should be a string
# The "-> str" annotation says that "greeting" will return a string
def greeting(name: str) -> str:
    return 'Hello ' + name

# This function is now statically typed: mypy will use the provided type hints to detect incorrect use of 
# the greeting function and incorrect use of variables within the greeting function. For example:
def greeting(name: str) -> str:
    return 'Hello ' + name

greeting(3)         # Argument 1 to "greeting" has incompatible type "int"; expected "str"
greeting(b'Alice')  # Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
greeting("World!")  # No error

def bad_greeting(name: str) -> str:
    return 'Hello ' * name  # Unsupported operand types for * ("str" and "str")