#here we learn importance of indentation in if else statements 

flavours = ['chocolate', 'vanilla', 'strawberry', 'mint', 'bad', 'very bad', 'cadbury']

for flavour in flavours:
    if flavour == 'bad':
        continue
    if flavour == 'very bad':
        break
    print("I like " + flavour + " ice cream")

print("out of loop") 
# observe above - if if and print are in same indentation line, it means they are independent statements not inside each other. 
# so after 2 ifs , loop comes out,but it is still inside for loop and hence it prints.  