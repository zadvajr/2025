# Annotating with simple data structures.
#In python 3.9+
from typing import List, Tuple, Dict

#List
prices: List[int] = [200, 300, 400]

#Tuple
immutable_prices: Tuple[int, int, int] = (450, 350, 250)

#Dict
price_dict: Dict[str, int] = {
    "item1": 200,
    "item2": 250,
    "item3": 300
}


#Newer version of python 3.10+
#You donn't need to import typing
new_price: list[int] = [14,902,898]
new_immutable_price: tuple[int,int,int] = (388,392,299)
new_price_dict: dict[str,int] = {
    "item_1":240,
    "item_2":490,
}