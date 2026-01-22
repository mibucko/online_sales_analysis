from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []  
        
    def add_to_cart(self, p: Product):
        self.cart_items.append(p) 
    
    def display_info(self):
        print("The basket content:")
        for p in self.cart_items:
            print(f"Product:{p.name}, price: {p.price}")
        print(f"Money spent: {sum(p.price for p in self.cart_items)}")