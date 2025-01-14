# filename typehints.py

def total_price(price_1:int,price_2:int):
    return f"Your total bill is USD {price_1+price_2}"
        
# price = total_price('30','40') #error if you run it with type hint
price = total_price(30, 40)
print(price)


