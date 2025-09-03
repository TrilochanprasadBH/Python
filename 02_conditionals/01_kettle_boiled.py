#learning if statement. 
is_kettle_boiled = True

if is_kettle_boiled:
    print(f"The kettle is boiled : {is_kettle_boiled}");


# 'if' condition returns/prints only if condition is True, so the below code will not print anything
is_kettle_boiled_2 = False 

if is_kettle_boiled_2:
    print(f"The kettle is not boiled : {is_kettle_boiled_2}");

num = 0
if num >= 0:
    print(f"{num} is a positive number");


#learning if-else statement
num = -10;
 
if num >= 0:
    print(f"{num} is a positive number");
else:
    print(f"{num} is a negative number");