class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        # Using super() to initialize name and price from the base class
        super().__init__(name, price)
        self.discount_percent = discount_percent

    def get_discounted_price(self):
        # Logic: Price - (Price * (Discount / 100))
        discount_amount = self.price * (self.discount_percent / 100)
        return float(self.price - discount_amount)

# Example usage provided in the prompt
p1 = DiscountedProduct("Phone", 10000, 10)
print(p1.get_discounted_price())