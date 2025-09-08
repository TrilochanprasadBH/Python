#single return 

def add(a, b):
    return a + b
print(add(2, 3))

def adding(a,b):
    return a+b
sum = adding(5,6)
print(sum)

def checkit():
    print('printing from function')
return_value = checkit()
print("return_value",return_value) #when function returns nothing, then it return None. this is deafult behaviour of python


#MULTIPLE RETURN based on conditions 

def check_num(num):
    if num == 0:
        return "zero" 
    return "non-zero"
print(check_num(0))
print(check_num(5))
print(check_num(-3))


#returning multiple values and handling absence of one or more return values 

def return_multiple():
    return 10,20,100 

x,y,_= return_multiple() #z will be assigned None as i am using _ to ignore the third return value
print(x)
print(y)
#print(z) #this will give error as z is not assigned any value