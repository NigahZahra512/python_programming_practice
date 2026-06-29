import json
import os


class Product:
    def __init__(self, sku, name, category, price):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self.image_url = None

    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "image_url": self.image_url
        }


class CloudStorageManager:
    def upload_image(self, file_name, file_size_mb):
        if not (file_name.endswith(".jpg") or file_name.endswith(".png")):
            raise ValueError("Only .jpg and .png files are allowed!")
        if file_size_mb >= 2:
            raise ValueError("File size must be under 2 MB!")
        return "https://cdn.cloudstorage.com/images/" + file_name


class StoreDatabase:
    def __init__(self):
        self.db_file = "catalog.json"
        self.products = []
        self.load_database()

    def load_database(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                self.products = json.load(f)
            print(f"Database loaded! Products found: {len(self.products)}")
        else:
            self.products = []
            print("No existing database found. Starting fresh!")

    def add_product(self, product_obj):
        for existing in self.products:
            if existing["sku"] == product_obj.sku:
                raise ValueError(f"SKU '{product_obj.sku}' already exists!")
        self.products.append(product_obj.to_dict())
        print(f"Product '{product_obj.name}' added successfully!")

    def save_database(self):
        with open(self.db_file, "w") as f:
            json.dump(self.products, f, indent=4)
        print("Database saved to", self.db_file)



def main():
    db = StoreDatabase()
    cloud = CloudStorageManager()

    while True:
        print("\n" + "="*40)
        print("      ADD NEW PRODUCT TO STORE")
        print("="*40)

        
        name     = input("Enter product name     : ")
        category = input("Enter product category : ")
        sku      = input("Enter product SKU      : ")

        try:
            price = float(input("Enter product price    : "))
        except ValueError:
            print("Invalid price! Please enter a number.")
            continue         

        
        file_name    = input("Enter image file name  : ")
        
        try:
            file_size = float(input("Enter image size (MB)  : "))
        except ValueError:
            print("Invalid file size! Please enter a number.")
            continue

      
        try:
            url = cloud.upload_image(file_name, file_size)
            print(f"Image uploaded! URL: {url}")
        except ValueError as e:
            print(f"Image Upload Error: {e}")
            continue          

        product = Product(sku, name, category, price)
        product.image_url = url

        try:
            db.add_product(product)
            db.save_database()
        except ValueError as e:
            print(f"Database Error: {e}")

        again = input("\nAdd another product? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting... Goodbye!")
            break


main()