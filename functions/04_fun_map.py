def  add_vat(price, vat_rate):
    total_price = price * (100 + vat_rate)/100
    return total_price


orders = [100, 200, 300]
vat_rate = [5, 10, 15]

for price in orders:
    final_price = add_vat(price, vat_rate[orders.index(price)])
    print(f"Price: {price}, Final Price with VAT: {final_price}")

#another way to do it  combing both lists into a zip. nice 
new  = zip(orders, vat_rate)

for order, vat in new:
    final_price = add_vat(order, vat)
    print(f"Price: {order}, Final Price with VAT is: {final_price}")
