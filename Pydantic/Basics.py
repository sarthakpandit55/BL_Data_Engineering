from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool

input_data = {'id':1, 'name': "Sarthak", 'is_active': True}
user = User(**input_data)
print(user)

product_one = Product(**{'id': 2, 'name':'Sarthak', 'price': 3.99, 'in_stock': True })
print(product_one)

