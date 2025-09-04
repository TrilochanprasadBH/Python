# print 1-10 using a loop.

for token in range(1,11):
    print(f"value of token is : {token}")

# print all list items 

my_list = ["apple", "banana", "cherry"]

for items in my_list:
    print(f"item is : {items}") 

#print index and item
for index, items in enumerate(my_list):
    print(f"index is : {index} and item is : {items}")


# print all list items in reverse order
for items in reversed(my_list):
    print(f"item is : {items}")

