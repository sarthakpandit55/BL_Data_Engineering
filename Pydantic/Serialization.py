from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    username:str
    address: Address

address1 = Address(**{"street":"Sonkh Road", "city":"Mathura", "postal_code":"12345"})
user1 = User(**{"id":1, "username":"Sarthak", "address":address1})

print(user1)
print(user1.model_dump())
print(user1.model_dump_json())