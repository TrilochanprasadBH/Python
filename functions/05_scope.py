# scope - the region where a variable is recognized
# think of scope like a concentric circle, inner circle can access outer circle but outer circle cannot access inner circle
my_global = "trilochan"

def my_function():
    my_enclosing = "karki"
    def my_inner_function():
        my_local = "hello"
        print("Local:", my_local)
        print("Enclosing:", my_enclosing)
        print("Global:", my_global)
    my_inner_function()
    print("Enclosing main function indside, outsid inner:", my_enclosing)

my_function()