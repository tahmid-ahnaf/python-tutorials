# Scenario: A shop offers discounts based on the total purchase amount:
#
# 10% discount if the total amount is greater than or equal to $100
# 5% discount if the total amount is greater than or equal to $50 but less than $100
# 2% discount if the total amount is greater than or equal to $30 but less than $50
# No discount otherwise

# Task: Write a Python program that takes the total purchase amount as input and prints the discounted price and the discount amount.

total_amount = float(input("enter total amount: "))

if total_amount >= 100 :
    discount = total_amount*0.1
    discounted_price = total_amount-discount

elif total_amount >= 50 :
    discount = total_amount*0.05
    discounted_price = total_amount-discount

elif total_amount >= 30 :
    discount = total_amount*0.02
    discounted_price = total_amount-discount
else :
    discount = 0
    discounted_price = total_amount

print("Discount ", discount)
print("Discounted Price ", discounted_price)











