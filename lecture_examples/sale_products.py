"""
Week 6 Lecture 1 Example
"""

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]

products_on_sale = [product[0] for product in products if product[2]]
print(products_on_sale)
