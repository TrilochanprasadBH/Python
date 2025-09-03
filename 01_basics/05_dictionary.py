# one way to create a dictionary is this 
maggie_snack = dict(base='maggie', topping='peanut butter', size='large')
print(f"maggie_snack = {maggie_snack}")

# another way to create a dictionary is this {}

maggie_food = {}
maggie_food['base'] = 'maggie'
maggie_food['topping'] = 'peanut butter'
maggie_food['size'] = 'large'
print(f"maggie_food = {maggie_food}");

maggie_food['sugar'] = 'high'
print(f"maggie_food = {maggie_food}");

#delete key 
del maggie_food['sugar']
print(f"maggie_food = {maggie_food}");

print(f" is sugar present in maggie foos? : {'sugar' in maggie_food}");
#check if a key is present in dictionary
print(f"is base present in maggie foos? : {'base' in maggie_food}");

#check and iterate over keys to print them. 
print(f"printing keys in maggie_food dictionary: {maggie_food.keys()}");

# printing values in dictionary
print(f"Iterating over keys in maggie_food dictionary: {maggie_food.values()}")

# printing items in dictionary, they are same but key value come in tuple form  
print(f"print items: {maggie_food.items()}")

#remove last item in dictionary

remove_last_item = maggie_food.popitem();  
print(f"removed last item: {remove_last_item}, maggie_food = {maggie_food}")

maggie_food.update({"rank":'1', "cadre": 'IAS'})
print(f"maggie_food after update = {maggie_food}")

# when trying to get a key or value from key , if it is not present it will throw an error, so , use get method with safe fallback 
customer_note = maggie_food.get('note', 'no note found'); 
# APP WONT CRASH  if this safe practise is followed. 
print(f"customer_note = {customer_note}")
