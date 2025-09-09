def this_is_recursion(n):
    if n==0:
        return "recursion ends here, base case"
    elif n>0:
        return this_is_recursion(n-1)   
    else:
        return "n should be a non-negative integer"

when_n_is_5 = print(this_is_recursion(5))
print(this_is_recursion(-1))
