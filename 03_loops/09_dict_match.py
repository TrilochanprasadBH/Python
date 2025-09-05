users = [
    {"id":1, "name":"Alice", "age":30, "coupon":"DISCOUNT10", "total":100},
    {"id":2, "name":"Bob", "age":25, "coupon":"DISCOUNT20", "total":200},
    {"id":3, "name":"Charlie", "age":35, "coupon":"DISCOUNT30", "total":300}
]

discounts = {
    "DISCOUNT10": (0.2,10),
    "DISCOUNT20": (0.4,20),
    "DISCOUNT30": (0.6,30)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent +fixed
    print(f"User {user['name']} gets a discount of {discount}")