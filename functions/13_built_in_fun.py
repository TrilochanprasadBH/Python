def my_built_in_fun(flavour="chai"): 
    # check = "random"
    """this is docu line, should always be at top in function,
    and this is used to document what this function does"""
    return flavour

print_this =my_built_in_fun()
print(my_built_in_fun.__name__)
print(my_built_in_fun.__doc__)   # if there is anything above """ line in func, then this prints none 
# if there is nothign then this prints the  text in """ line 