"""Week 6 exercises"""
from product import Product

# ON_SALE_INDEX = 2
#
# products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
# on_sale_products = [product for product in products if product[ON_SALE_INDEX]]
#
# print(on_sale_products)


products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]

on_sale_products = [product for product in products if product.is_on_sale]
print(on_sale_products)
