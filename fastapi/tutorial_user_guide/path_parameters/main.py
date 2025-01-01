#Path Parameters
#You can declare path parameters or variables with the same python format strings
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}") #item_id: is a path parameter
async def read_item(item_id):
    return {"item_id": item_id}

#The value of the path parameter item_id will be passed to the path operation function
#as argument item_id

#So if you run this code and go to http://127.0.0.1:8000/items/foo
#You will get a response of {"item_id":"foo"}

#Path parameters with type
#You can declare the type of a path parameter in the function using python standard type annotations
@app.get("/books/{book_id}")
async def read_book(book_id: int): #the type of the path parameter book_id is declared to be of type int
    return {"book_id": book_id}

#Predefined path parameter type values.
#if you have a path operation that receives path parameter, 
#but you want the possible valid path parameter values to be predefined, 
# you can use a standard Python Enum.
#to achieve that
#1. import enum and create a subclass that inherits from str and Enum
#2. Then create class attributes with fixed values, which will be the available valid values:
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name is ModelName.resnet:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
