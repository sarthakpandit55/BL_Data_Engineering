class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def displayAddress(self):
        print(self.address.city, self.address.state, self.address.pin)

class Address:
    def __init__(self, city, pin, state):
            self.city = city
            self.pin = pin
            self.state = state

add = Address("Mathura", 281004, "Uttar Pradesh")

cust = Customer("Sarthak", 5, add)

cust.displayAddress()