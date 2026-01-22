class Product:
    def __init__(self, name, price, quantity):
        self.name = name  
        self.price = price  
        self.quantity = quantity 
    
    def display_info(self):
        return f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}"   
    
    def set_quantity(self, quantity):
        if quantity >= 0:
            self.quantity = quantity  
        else:
            print(f"Please enter correct value for {self.name} quantity.")
