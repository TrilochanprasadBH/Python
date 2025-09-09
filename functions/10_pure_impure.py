#pure functions 
# these functions always return the same output for the same input and do not have side effects

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

#impure functions
# these functions may return different outputs for the same input or have side effects

global_counter = 0
def increment_counter(num):
   
    global global_counter
    global_counter += 1
    num+= 1+global_counter
    return global_counter , num 

global_counter, num = increment_counter(1)
print(global_counter, num)  # Output: 1, 2  

#in above impure functions the output depends on NOT JUST THE INPUT but also the OTHER variable ie - global variable
