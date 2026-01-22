from product import Product
from product_manager import ProductManager
from cart import Cart
import random

p1 = Product("Audi", 100, 10)
p2 = Product("Lamborgini", 200, 20)
p3 = Product("Fica", 300, 30)
p4 = Product("Lancia", 400, 40)
p5 = Product("Skoda", 500, 50)
products = (p1, p2, p3, p4, p5)

pm = ProductManager()
c = Cart()

for p in products:      # Adding all products to the list
    pm.add_product(p)

random_items = random.sample(pm.products, 3)
for i in random_items:
    c.add_to_cart(i)    # Adding some items to the shopping list

p3.set_quantity(44)     # Testing of function for changing product quantity.
pm.display_info()
print()
pm.total_value()        # Total inventory value
pm.item_remove("Fica")  # Testing of function for removing product.
print()
pm.display_info()       # Product list with removed item.
print()
c.display_info()        # List of purchased items and money spent
