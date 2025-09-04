order_amount =  int(input("Enter the order amount: "));
print(type(order_amount))

# normal if-else statement

# if order_amount > 300:
#     delivery_fee = 0
# else:
#     delivery_fee = 30


# ternary operator 

delivery_fee = 0 if order_amount > 300 else 30
print(f"Delivery fee is: {delivery_fee}")