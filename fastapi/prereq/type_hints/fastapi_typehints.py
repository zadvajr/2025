"""Pyhon Type Hints"""
#Python has support for optional type hints also called type annotations
#The type hints or annotations are special syntax that allow declaring the type of a variable
#By declaring the type of your variables, editors and tools can give your better support
# FastAPI is all based on these type hints, they give it many advantages and benefits.

#Motivation
#Let's start with a simple example
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("daniel", "zadva Jnr"))

#calling this program will output: Daniel Zadva Jnr
# The function does the following:
# Takes a first_name and last_name.
# Converts the first letter of each one to upper case with title().
# Concatenates them with a space in the middle.
