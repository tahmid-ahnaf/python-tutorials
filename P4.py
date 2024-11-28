# online store
# you have to calculate the total price of items in customer's cart
# each item has a quantity and price

cart = [
    {"category": "T-shirt", "quantity": 2, "price": 15.99},
    {"category": "Jeans", "quantity": 1, "price": 49.99},
    {"category": "Shoes", "quantity": 1, "price": 79.99}
]

total_price = 0

for item in cart:
    quantity = item["quantity"]
    price = item["price"]
    total_price = total_price + quantity*price

print("Total price for the cart: ", total_price )