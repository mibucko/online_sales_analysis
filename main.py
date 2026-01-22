from product import Product
from product_manager import ProductManager

p1 = Product("Audi", 1200, 15)
p2 = Product("Lamborgini", 20, 50)
p3 = Product("Fica", 250, 5)
p4 = Product("Lancia", 2150, 45)
p5 = Product("Skoda", 3, 3000)

pm = ProductManager()
pm.add_product(p1)
pm.add_product(p2)
pm.add_product(p3)
pm.add_product(p4)
pm.add_product(p5)

p3.set_quantity(44)     # Testing of function for changing product quantity.
pm.display_all_products()
print()
pm.total_value()        # Total inventory value
