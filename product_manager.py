from product import Product

class ProductManager:
    def __init__(self):
        self.products = [] 
    
    def add_product(self, p: Product):
        self.products.append(p) 
    
    def display_info(self):
        print("Summary of all our products:")
        for p in self.products:
            print(p.display_info())
        
    def total_value(self):
        print(f"Total value of all our products is {sum(p.price * p.quantity for p in self.products)}")
    
    def item_remove(self, item):
        for p in self.products:
            if p.name == item:
                self.products.remove(p)
        return p
        return None
        