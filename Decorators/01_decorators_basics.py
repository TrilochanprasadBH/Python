#primary agenda is decoration/wrapping , that is something done on top of something 
#decorator is like a high level function , which takes other functions as parameters 

from functools import wraps

def my_decorator(func):
   
    @wraps(func) #adding this line gives us same name 'greet' instead of wrapper when we do print greet.__name__ 
    #wraps(func) preserves the data , this is important
    def wrapper():
        print('before param func execution')
        func()
        print('before param func execution')
    return wrapper

#syntax to call the function by passing as param, we dont call/ send param like this (send here), but as seen below 
#things written below @my_decorator automatically get passed as argument to the my_decorator function

@my_decorator
def greet():
    print('hey this is greeting by trilochanprasad')

greet() 
#output is : 

# before param func execution
# hey this is greeting by trilochanprasad
# before param func execution

print(greet.__name__) #wrapper is the output where as name is greet , to overcome this we use wraps 