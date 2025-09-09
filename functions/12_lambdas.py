mylist = ['a','b','c','d','e']

new_list = list(filter(lambda char: char!="a",mylist))
print(new_list)


# not_a , this is the role lambda plays , its simple.  we use lambda when we need to use inline function , simple one for filter sort ,map ,minmax etc. 
# if we need re usable code then we use below type. both have its own usage. 
def not_a(ch):
    return ch != 'a'

my_filtered = list(filter(not_a, my_list))
