class Product:
    def __init__(self, sku, name, category, price):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self.image_url = None   # Default value

    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "image_url": self.image_url
        }


# Testing
p1 = Product("P101", "Blue Shirt", "clothing", 2500)
p2 = Product("P102" ,"white shoes" , "footwear" ,1500 )

print(p1.to_dict())
print(p2.to_dict())