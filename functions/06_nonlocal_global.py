# non local vs global variable
# A nonlocal variable is one that is not local to the function but also not global.
# It is used in nested functions where the variable is defined in the enclosing function.

# Global variable
# A global variable is defined outside of any function and can be accessed from any function in the same module.
# It is declared using the 'global' keyword.

#non local example 1

outer_variable = "I am a global variable"

def outer_function():
    outter_variable = "I am an outter variable"
    def inner_function():
        nonlocal outter_variable
        outter_variable= "I am a modified outter variable in inner function"
    inner_function()
    print(f"i am a modified outter variable in inner function: {outter_variable}")
outer_function()

#here print wont print, the outer_variable written globally, because it is not in the scope of inner_function, 
# its chain of consideration starts from inner_function to outer_function to global scope 
# but due to nonlocal keyword it will print the modified value of outter_variable




# global example 1

global_variable = "I am a global variable"

def modify_global():
    def inner_function():
        global global_variable
        global_variable = "I am a modified global variable in inner function"
    inner_function()

modify_global()
print(f"i am a modified global variable in inner function: {global_variable}")
