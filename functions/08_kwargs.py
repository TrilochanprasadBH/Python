#kwargs is used to pass multiple keyword arguments to a function - named or positional 

def my_function(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("\nExtras:",extras)

my_function("cheese", "tomato", "mushrooms", sauce="pesto", drink="coke")

#output 
# Ingredients: ('cheese', 'tomato', 'mushrooms') in tuple form 

# Extras: {'sauce': 'pesto', 'drink': 'coke'} in object form 


# AVOID DEFAULT TRAP , commonsense to use None as default value for mutable data types - IMPORTANT 

def add_to_list( my_list=None):
    if my_list is None:
        my_list = []
    print(f"my_list: {my_list}")

add_to_list()


def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    # my_list.append(value)
    print(f"value: {value}, my_list: {my_list}")

add_to_list(1)