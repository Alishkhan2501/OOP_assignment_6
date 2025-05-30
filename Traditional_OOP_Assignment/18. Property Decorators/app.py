# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price can't be negative")
    
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(100)
print(p.price)  
p.price = 150   
del p.price     

