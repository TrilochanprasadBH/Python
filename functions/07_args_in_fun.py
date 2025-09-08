#immutable object as argument , cant be chagned by function
chai = "darjeling"

def tea(kind):
    print("I like", kind)
tea(chai)

# mutable object as argument , can be changed by function
fruits = ["apple", "banana", "cherry"]

def add_fruit(fruit_list):
    fruit_list.append("orange")
    print("Inside function:", fruit_list)
add_fruit(fruits)
print("Outside function:", fruits)

numbers = [1,2,3,4]

def modify_list(numbers):
    numbers[0] = 10
    print("Inside function:", numbers)  
modify_list(numbers)
print("Outside function:", numbers)

#passing arguments by position 

def argby_position(a,b,c):
    print("a:", a)
    print("b:", b)
    print("c:", c) 
argby_position(1,2,3) 

#passing arguments by name /keywords 

def argby_position(a,b,c):
    print("a:", a)
    print("b:", b)
    print("c:", c) 
argby_position(a=10,c=90,b=3)  # observe how order of arguments can be changed but still parameters are assigned correctly

