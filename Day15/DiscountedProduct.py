class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        super().__init__(name, price)
        self.discount_percent = discount_percent

    def get_discounted_price(self):
        discount_amount = (self.price * self.discount_percent) / 100
        return float(self.price - discount_amount)

p1 = DiscountedProduct("Phone", 10000, 10)
print(p1.get_discounted_price())
