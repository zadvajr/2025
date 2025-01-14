# Annotating with complex data structures
#Python 3.9+
from typing import Union, List

x: List[Union[int, float]] = [2.5, 3, 3.5, 4, 4.5]

#newer syntax in python 3.10+
x: list[int | float] = [2.5, 3, 3.5, 4, 4.5]

#use case
def inr_to_usd(value:float) -> Union[float,None]:
    try:
        conversion_factor = 75
        value = value/conversion_factor
        return value
    except TypeError:
        return None

inr_to_usd('23')