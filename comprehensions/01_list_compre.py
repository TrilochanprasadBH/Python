my_food = [
    "cheese burger",
    "cheese samosa",
    "cheese parota",
    "paneer cubes",
    "paneer masala",
    "aloo bonda",
    "aloo kachori"
]

# syntax for list comprehension 
# item for item in iterable if condition 

list_compre = [oota for oota in my_food if "cheese" in oota]
print(list_compre)

list_compre = [oota for oota in my_food if len(oota)>10]
print(list_compre)

